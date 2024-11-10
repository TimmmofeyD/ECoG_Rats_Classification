import datetime
import os
import plotly.graph_objects as go
from src.ui_interface import *
from src.ui_functions import *
from src.model import *
from src.time_series_class import TimeSeriesDataset
from Custom_Widgets import *
from Custom_Widgets.QAppSettings import QAppSettings
from PySide6.QtCore import QUrl
from PySide6.QtWidgets import QFileDialog, QTableWidgetItem, QTableWidget, QMessageBox
from PySide6.QtWebEngineWidgets import QWebEngineView
from pyedflib import highlevel
import numpy as np
import pandas as pd
import torch
import random


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.source_data = None
        self.time = None
        self.graphics = False
        self.signals = None
        self.signal_headers = None
        self.header = None
        self.filename = None
        self.labels_predict = None
        self.label_prob = None

        self.initFuncs()

        self.spacer_index = -1

        for index in range(self.ui.verticalLayout_9.count()):
            layout_item = self.ui.verticalLayout_9.itemAt(index)
            if layout_item.widget() == self.ui.verticalSpacer_3:
                self.spacer_index = index

        # json files path/name
        loadJsonStyle(self, self.ui, jsonFiles={
            "json-styles/style.json"
        })
        self.show()

        QAppSettings.updateAppSettings(self)
        self.app_functions = GuiFunctions(self)

    def initFuncs(self):
        self.falseVisible()
        self.ui.downloadFile.clicked.connect(self.load_file)
        self.ui.startBtn.clicked.connect(self.start_model)
        self.ui.saveBtn.clicked.connect(self.save_result)
        self.ui.classBtn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.ECS))
        self.ui.analysisBtn.clicked.connect(self.analysis_pages)
        self.ui.settingsBtn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.settings))
        self.ui.probBtn.clicked.connect(self.download_prob)

    def falseVisible(self):
        self.ui.sourceData.setVisible(False)
        self.ui.startBtn.setVisible(False)
        self.ui.model_done_frame.setVisible(False)
        self.ui.download_part.setVisible(False)
        self.ui.sourceData.setEditTriggers(QTableWidget.NoEditTriggers)

    def load_file(self):
        file = QFileDialog.getOpenFileName(None, "Выберите файл", "",
                                           "All files (*);;European Data Format (*.edf)",
                                           "European Data Format (*.edf)")[0]
        if file:
            self.falseVisible()
            self.toggle_spacer(drop=False)
            self.graphics = False
            self.ui.progressBar.setValue(0)
            self.filename = os.path.abspath(file)
            self.ui.lineFile.setText(self.filename)
            try:
                self.signals, self.signal_headers, self.header = highlevel.read_edf(self.filename)
                self.ui.labelError.setText("Образ загруженного файла:")
                self.ui.downloadFile.setText("Выбрать другой")
                self.show_data(self.signals)
            except:
                self.ui.sourceData.setVisible(False)
                self.ui.labelError.setText("<html><head/><body><p><span style=' color:#772a8f;'>Файл не прочитан, "
                                           "повторите попытку</span></p></body></html>")

    def analysis_pages(self):
        if self.graphics:
            self.ui.stackedWidget.setCurrentWidget(self.ui.graphics)
        else:
            self.ui.stackedWidget.setCurrentWidget(self.ui.none_graphics)

    def toggle_spacer(self, drop=True):
        if drop:
            self.ui.verticalLayout_9.removeItem(self.ui.verticalSpacer_3)
        else:
            self.ui.verticalLayout_9.insertItem(self.spacer_index, self.ui.verticalSpacer_3)

    def show_data(self, signals):
        self.toggle_spacer()
        sample_rate = 400
        self.time = np.arange(signals.shape[1]) / sample_rate
        self.source_data = pd.DataFrame({"time": self.time, "FrL": signals[0], "FrR": signals[1], "OcR": signals[2]})

        rows = pd.concat([self.source_data.head(25), self.source_data.tail(25)]).reset_index()

        self.ui.sourceData.setRowCount(len(rows))
        self.ui.sourceData.setColumnCount(len(rows.columns))
        self.ui.sourceData.setHorizontalHeaderLabels(rows.columns)

        for row_index, row in rows.iterrows():
            for col_index, value in enumerate(row):
                item = QTableWidgetItem(str(value))
                self.ui.sourceData.setItem(row_index, col_index, item)

        self.ui.sourceData.setVisible(True)
        self.ui.startBtn.setVisible(True)

        self.ui.sourceData.horizontalHeader().setMinimumSectionSize(180)

    def start_model(self):
        self.ui.model_done_frame.setVisible(False)
        self.graphics = False
        dataset = TimeSeriesDataset(self.source_data, ws=400, fourier=200)
        device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
        model = torch.load('src/best_model_400.pth', weights_only=False, map_location=device)

        self.labels_predict = predict_with_model(model, dataset, pb=self.ui.progressBar, return_labels=False)
        self.result_data(self.labels_predict)
        if self.ui.progressBar.value() > 98:
            self.ui.progressBar.setValue(100)
            self.model_done()

    def result_data(self, labels_predict):
        preds = np.argmax(labels_predict, axis=1)
        metky = np.repeat(preds, 400)

        preds_df = pd.DataFrame({'time': self.time})
        preds_df = preds_df.iloc[len(preds_df) - len(metky):, :].reset_index(drop=True)
        preds_df["pred"] = metky

        preds_df['pred_shift_fwd'] = preds_df['pred'].shift(-1).ffill()
        preds_df['pred_shift_back'] = preds_df['pred'].shift(1).bfill()
        preds_df.loc[preds_df['pred'] != preds_df['pred_shift_fwd'], ['pred_end_fl']] = 1
        preds_df.loc[preds_df['pred'] != preds_df['pred_shift_back'], ['pred_start_fl']] = 1

        preds_df.loc[(preds_df['pred_start_fl'] == 1) & (preds_df['pred'] == 0), ['pred_start_fl']] = 'swd1'
        preds_df.loc[(preds_df['pred_start_fl'] == 1) & (preds_df['pred'] == 2), ['pred_start_fl']] = 'is1'
        preds_df.loc[(preds_df['pred_start_fl'] == 1) & (preds_df['pred'] == 1), ['pred_start_fl']] = 'ds1'

        preds_df.loc[(preds_df['pred_end_fl'] == 1) & (preds_df['pred'] == 0), ['pred_end_fl']] = 'swd2'
        preds_df.loc[(preds_df['pred_end_fl'] == 1) & (preds_df['pred'] == 2), ['pred_end_fl']] = 'is2'
        preds_df.loc[(preds_df['pred_end_fl'] == 1) & (preds_df['pred'] == 1), ['pred_end_fl']] = 'ds2'

        preds_df['tick'] = preds_df['pred_start_fl']
        preds_df['tick'] = preds_df['tick'].fillna(preds_df['pred_end_fl'])
        preds_df['tick'] = np.where(preds_df['tick'] == 1, np.nan, preds_df['tick'])

        if preds_df.iloc[0]['pred'] == 0:
            preds_df.loc[0, 'tick'] = 'swd1'

        elif preds_df.iloc[0]['pred'] == 1:
            preds_df.loc[0, 'tick'] = 'ds1'

        elif preds_df.iloc[0]['pred'] == 2:
            preds_df.loc[0, 'tick'] = 'is1'

        headers_preds_df = preds_df[['time', 'tick']].loc[~preds_df['tick'].isna()]
        headers_preds_df['duration'] = -1
        headers_preds_df = headers_preds_df[['time', 'duration', 'tick']]

        self.header['annotations'] = headers_preds_df.values.tolist()

        for dct in self.signal_headers:
            dct['physical_max'] = round(self.signals.max(), 7)
            dct['physical_min'] = round(self.signals.min(), 7)

    def model_done(self):
        self.ui.model_done_frame.setVisible(True)
        self.ui.download_part.setVisible(True)
        self.graphics = True
        self.make_graphics()

    def make_graphics(self):
        min_val = np.min(self.labels_predict)
        max_val = np.max(self.labels_predict)
        normalized_labels_predict = (self.labels_predict - min_val) / (max_val - min_val)

        normalized_labels_predict = np.repeat(normalized_labels_predict, 400, axis=0)
        self.label_prob = pd.DataFrame(data=normalized_labels_predict, columns=['swd', 'ds', 'is', 'noise'])

        lb = self.label_prob.sample(50)

        self.ui.table_prob.setRowCount(len(lb))
        self.ui.table_prob.setColumnCount(len(lb.columns))
        self.ui.table_prob.setHorizontalHeaderLabels(lb.columns)

        for row_index, row in lb.iterrows():
            for col_index, value in enumerate(row):
                item = QTableWidgetItem(str(round(value, 3)))
                self.ui.table_prob.setItem(row_index, col_index, item)

        self.ui.table_prob.horizontalHeader().setMinimumSectionSize(80)


        counts = {'swd': 0, 'ds': 0, 'is': 0}
        swds = []
        dss = []
        iss = []
        for h in self.header['annotations']:
            counts[h[2][:-1]] += 1
        for i in range(0, len(self.header['annotations'])-2, 2):
            if self.header['annotations'][i][2] == 'swd1':
                swds.append((self.header['annotations'][i][0], self.header['annotations'][i+1][0]))
            if self.header['annotations'][i][2] == 'ds1':
                dss.append((self.header['annotations'][i][0], self.header['annotations'][i+1][0]))
            if self.header['annotations'][i][2] == 'is1':
                iss.append((self.header['annotations'][i][0], self.header['annotations'][i+1][0]))

        counts['swd'] /= 2
        counts['ds'] /= 2
        counts['is'] /= 2
8
        stats = pd.DataFrame(counts, columns=['count']).reset_index()
        self.ui.tableStats.setRowCount(len(stats))
        self.ui.tableStats.setColumnCount(len(stats.columns))
        self.ui.tableStats.setHorizontalHeaderLabels(stats.columns)

        for row_index, row in stats.iterrows():
            for col_index, value in enumerate(row):
                item = QTableWidgetItem(str(value))
                self.ui.tableStats.setItem(row_index, col_index, item)

        select_swd = random.choice(swds)
        select_ds = random.choice(dss)
        select_is = random.choice(iss)

        self.random_classes_graphs(select_swd, select_ds, select_is)

    def random_classes_graphs(self, swd, ds, iss):
        pass
        # swd_data = self.
        # ds_data =
        # is_data =

        '''
        fig = go.Figure(data=go.Scatter(x=[1, 2, 3], y=[3, 1, 6], mode='markers'))
        fig.update_layout(title="Interactive Plotly Graph")

        file_path = "plotly_graph.html"
        fig.write_html(file_path)

        self.web_view = QWebEngineView()
        self.web_view.setUrl(QUrl(f"file:///{file_path}"))

        # self.ui.layout_width.addWidget(self.web_view)
        '''

    def download_prob(self):
        name = QFileDialog.getSaveFileName(None, "Сохранить файл", "",
                                           "Comma-Separated Values (*.csv)")[0]
        name = os.path.abspath(name)
        if name:
            self.label_prob.to_csv(name, index=False, sep=',')
            QMessageBox.information(self, "Сохранено", f"Файл успешно сохранен по пути {name}")

    def save_result(self):
        name = QFileDialog.getSaveFileName(None, "Сохранить файл", "",
                                           "European Data Format (*.edf)")[0]
        name = os.path.abspath(name)
        if name:
            highlevel.write_edf(name, self.signals,
                                signal_headers=self.signal_headers,
                                header=self.header)
            QMessageBox.information(self, "Сохранено", f"Файл успешно сохранен по пути {name}")
