from torch.utils.data import DataLoader
import numpy as np
import torch
from torch import nn, optim

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

def predict_with_model(model, dataset, pb, device=None, batch_size=32, num_workers=0, return_labels=False):
    """
    :param model: torch.nn.Module - обученная модель
    :param dataset: torch.utils.data.Dataset - данные для применения модели
    :param device: cuda/cpu - устройство, на котором выполнять вычисления
    :param batch_size: количество примеров, обрабатываемых моделью за одну итерацию
    :return: numpy.array размерности len(dataset) x *
    """
    if device is None:
        device = 'cuda' if torch.cuda.is_available() else 'cpu'
    results_by_batch = []

    device = torch.device(device)
    model.to(device)
    model.eval()

    dataloader = DataLoader(dataset, batch_size=batch_size, shuffle=False, num_workers=num_workers)
    labels = []
    with torch.no_grad():
        counter = 1
        total = (len(dataset) / batch_size)
        for batch_x, batch_y in dataloader:
            batch_x = copy_data_to_device(batch_x, device)

            if return_labels:
                labels.append(batch_y.numpy())

            batch_pred = model(batch_x)
            results_by_batch.append(batch_pred.detach().cpu().numpy())

            counter += 1
            pb.setValue(int((counter/total)*100))

    if return_labels:
        return np.concatenate(results_by_batch, 0), np.concatenate(labels, 0)
    else:
        return np.concatenate(results_by_batch, 0)


def copy_data_to_device(data, device):
    if torch.is_tensor(data):
        return data.to(device)
    elif isinstance(data, (list, tuple)):
        return [copy_data_to_device(elem, device) for elem in data]
    raise ValueError('Недопустимый тип данных {}'.format(type(data)))


def print_grad_stats(model):
    mean = 0
    std = 0
    norm = 1e-5
    for param in model.parameters():
        grad = getattr(param, 'grad', None)
        if grad is not None:
            mean += grad.data.abs().mean()
            std += grad.data.std()
            norm += 1
    mean /= norm
    std /= norm
    print(f'Mean grad {mean}, std {std}, n {norm}')


class CNN1d(nn.Module):
    def __init__(self, channels_in = 6, ws = 400):
        super(CNN1d, self).__init__()
        self.act = nn.GELU()
        self.conv11 = nn.Conv1d(in_channels=channels_in,
                               out_channels=64,
                               kernel_size=101,
                               padding=50,
                               padding_mode='circular',
                               bias=False)
        self.bn11 = nn.BatchNorm1d(64)
        self.pool = nn.MaxPool1d(kernel_size=2, stride=2)
        self.conv22 = nn.Conv1d(in_channels=64,
                               out_channels=128,
                               kernel_size=3,
                               padding=1,
                               padding_mode='zeros',
                               bias=False)
        self.bn22 = nn.BatchNorm1d(128)
        self.adaptive_pool = nn.AvgPool1d(kernel_size=200)
        self.fc = nn.Linear(128, 4)

        self.wavelets = nn.Sequential(
            self.conv11,
            self.act,
            self.bn11
        )

        self.encoder = nn.Sequential(
            self.conv22,
            self.act,
            self.pool,
            self.bn22,
            self.adaptive_pool
        )

    def forward(self, data):
        x = self.wavelets(data.permute(0, 2, 1))
        x = self.encoder(x)
        x = x.view(x.size(0), -1)
        x = self.fc(x)
        return x
