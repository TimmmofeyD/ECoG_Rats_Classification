import numpy as np
import torch
from torch.utils.data import Dataset
from scipy.fft import fft, ifft


class TimeSeriesDataset(Dataset):
    def __init__(self, df, ws, fourier):
        self.df = df
        self.ws = ws
        self.fourier = fourier

        # Извлекаем временные ряды и метки
        self.time_series = df.iloc[:, 1:4].values
        self.labels = df.iloc[:, 4:].values

        # Определяем количество окон
        self.num_windows = (len(self.time_series) - ws) // ws + 1

    def __len__(self):
        return self.num_windows

    def __getitem__(self, idx):
        start_idx = idx * self.ws
        end_idx = start_idx + self.ws

        # Извлекаем окно временного ряда
        window = self.time_series[start_idx:end_idx, :]
        abs_fft_window = np.concatenate([np.abs(fft(window[:, i])) for i in range(3)], axis=0)

        # Скользящее среднее и фильтрация частоты 50 Гц
        filtered_window = []
        for i in range(3):
            channel = self.time_series[start_idx:end_idx + 1, i]
            moving_avg = np.convolve(channel, np.ones(2) / 2, mode='valid')
            fft_moving_avg = fft(moving_avg)
            fft_moving_avg[8] = 0  # Зануляем частоту 50 Гц
            filtered_signal = ifft(fft_moving_avg).real
            filtered_window.append(filtered_signal)

        filtered_window = np.array(filtered_window).T

        # Объединяем все части данных
        # combined_data = np.concatenate((window,
        #                                 abs_fft_window.reshape(-1, 3), filtered_window), axis=1)
        combined_data = np.concatenate((window,
                                        abs_fft_window.reshape(-1, 3)), axis=1)

        # Определяем метку для окна методом голосования
        window_labels = self.labels[start_idx:end_idx]
        majority_label = window_labels[-1]

        return torch.tensor(combined_data, dtype=torch.float32), torch.tensor(majority_label, dtype=torch.float32)
