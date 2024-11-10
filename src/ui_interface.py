# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'new_interface.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QHeaderView,
    QLabel, QLineEdit, QMainWindow, QProgressBar,
    QPushButton, QSizePolicy, QSpacerItem, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)

from Custom_Widgets.QCustomQStackedWidget import QCustomQStackedWidget
from Custom_Widgets.QCustomSlideMenu import QCustomSlideMenu
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1080, 720)
        MainWindow.setMinimumSize(QSize(1080, 720))
        font = QFont()
        font.setPointSize(8)
        MainWindow.setFont(font)
        icon = QIcon()
        icon.addFile(u":/appIcon/free-icon-research-7243666 (2).png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, 0, -1, -1)
        self.leftMenu = QCustomSlideMenu(self.centralwidget)
        self.leftMenu.setObjectName(u"leftMenu")
        self.verticalLayout = QVBoxLayout(self.leftMenu)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 5, 5, 5)
        self.widget = QWidget(self.leftMenu)
        self.widget.setObjectName(u"widget")
        self.widget.setMinimumSize(QSize(0, 50))
        self.verticalLayout_3 = QVBoxLayout(self.widget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(16, 30, -1, 36)
        self.menuButton = QPushButton(self.widget)
        self.menuButton.setObjectName(u"menuButton")
        icon1 = QIcon()
        icon1.addFile(u":/logos/Icons/feather/menu.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.menuButton.setIcon(icon1)
        self.menuButton.setIconSize(QSize(18, 18))

        self.verticalLayout_3.addWidget(self.menuButton)


        self.verticalLayout.addWidget(self.widget, 0, Qt.AlignLeft|Qt.AlignTop)

        self.widget_3 = QWidget(self.leftMenu)
        self.widget_3.setObjectName(u"widget_3")
        self.verticalLayout_2 = QVBoxLayout(self.widget_3)
        self.verticalLayout_2.setSpacing(12)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(5, 5, 11, 5)
        self.classBtn = QPushButton(self.widget_3)
        self.classBtn.setObjectName(u"classBtn")
        self.classBtn.setMinimumSize(QSize(190, 37))
        font1 = QFont()
        font1.setFamilies([u"Yu Gothic UI Semibold"])
        font1.setPointSize(12)
        font1.setBold(True)
        self.classBtn.setFont(font1)
        icon2 = QIcon()
        icon2.addFile(u":/logos/Icons/feather/activity.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.classBtn.setIcon(icon2)
        self.classBtn.setIconSize(QSize(20, 20))

        self.verticalLayout_2.addWidget(self.classBtn, 0, Qt.AlignLeft)

        self.analysisBtn = QPushButton(self.widget_3)
        self.analysisBtn.setObjectName(u"analysisBtn")
        self.analysisBtn.setMinimumSize(QSize(230, 37))
        self.analysisBtn.setFont(font1)
        icon3 = QIcon()
        icon3.addFile(u":/logos/Icons/font_awesome/solid/chart-column.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.analysisBtn.setIcon(icon3)
        self.analysisBtn.setIconSize(QSize(20, 20))

        self.verticalLayout_2.addWidget(self.analysisBtn, 0, Qt.AlignLeft)

        self.settingsBtn = QPushButton(self.widget_3)
        self.settingsBtn.setObjectName(u"settingsBtn")
        self.settingsBtn.setMinimumSize(QSize(222, 37))
        self.settingsBtn.setFont(font1)
        icon4 = QIcon()
        icon4.addFile(u":/logos/Icons/material_design/auto_fix_high.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.settingsBtn.setIcon(icon4)
        self.settingsBtn.setIconSize(QSize(20, 20))

        self.verticalLayout_2.addWidget(self.settingsBtn, 0, Qt.AlignLeft)


        self.verticalLayout.addWidget(self.widget_3, 0, Qt.AlignLeft|Qt.AlignTop)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.horizontalLayout.addWidget(self.leftMenu, 0, Qt.AlignLeft)

        self.mainBody = QWidget(self.centralwidget)
        self.mainBody.setObjectName(u"mainBody")
        self.verticalLayout_4 = QVBoxLayout(self.mainBody)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.header = QWidget(self.mainBody)
        self.header.setObjectName(u"header")
        self.horizontalLayout_4 = QHBoxLayout(self.header)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(-1, 0, -1, -1)
        self.frame_2 = QFrame(self.header)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_2)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(-1, 16, -1, -1)
        self.label = QLabel(self.frame_2)
        self.label.setObjectName(u"label")
        font2 = QFont()
        font2.setFamilies([u"Yu Gothic UI Semibold"])
        font2.setPointSize(18)
        font2.setBold(True)
        self.label.setFont(font2)

        self.verticalLayout_6.addWidget(self.label)


        self.horizontalLayout_4.addWidget(self.frame_2)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_2)

        self.frame_3 = QFrame(self.header)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_5.setSpacing(5)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(5, 0, 0, 5)
        self.minimizeBtn = QPushButton(self.frame_3)
        self.minimizeBtn.setObjectName(u"minimizeBtn")
        icon5 = QIcon()
        icon5.addFile(u":/logos/Icons/font_awesome/solid/minus.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.minimizeBtn.setIcon(icon5)
        self.minimizeBtn.setIconSize(QSize(14, 14))

        self.horizontalLayout_5.addWidget(self.minimizeBtn)

        self.resizeBtn = QPushButton(self.frame_3)
        self.resizeBtn.setObjectName(u"resizeBtn")
        icon6 = QIcon()
        icon6.addFile(u":/logos/Icons/feather/square.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.resizeBtn.setIcon(icon6)
        self.resizeBtn.setIconSize(QSize(14, 14))

        self.horizontalLayout_5.addWidget(self.resizeBtn)

        self.closeBtn = QPushButton(self.frame_3)
        self.closeBtn.setObjectName(u"closeBtn")
        icon7 = QIcon()
        icon7.addFile(u":/logos/Icons/font_awesome/solid/xmark.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.closeBtn.setIcon(icon7)
        self.closeBtn.setIconSize(QSize(14, 14))

        self.horizontalLayout_5.addWidget(self.closeBtn)


        self.horizontalLayout_4.addWidget(self.frame_3)


        self.verticalLayout_4.addWidget(self.header, 0, Qt.AlignTop)

        self.mainContent = QWidget(self.mainBody)
        self.mainContent.setObjectName(u"mainContent")
        self.verticalLayout_5 = QVBoxLayout(self.mainContent)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(5, 5, 5, 5)
        self.stackedWidget = QCustomQStackedWidget(self.mainContent)
        self.stackedWidget.setObjectName(u"stackedWidget")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stackedWidget.sizePolicy().hasHeightForWidth())
        self.stackedWidget.setSizePolicy(sizePolicy)
        self.stackedWidget.setMinimumSize(QSize(768, 528))
        self.stackedWidget.setLineWidth(0)
        self.ECS = QWidget()
        self.ECS.setObjectName(u"ECS")
        self.verticalLayout_9 = QVBoxLayout(self.ECS)
        self.verticalLayout_9.setSpacing(14)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(20, 20, -1, -1)
        self.label_4 = QLabel(self.ECS)
        self.label_4.setObjectName(u"label_4")
        font3 = QFont()
        font3.setFamilies([u"Yu Gothic UI Semibold"])
        font3.setPointSize(14)
        font3.setBold(True)
        self.label_4.setFont(font3)

        self.verticalLayout_9.addWidget(self.label_4, 0, Qt.AlignLeft|Qt.AlignTop)

        self.frame_4 = QFrame(self.ECS)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_6.setSpacing(10)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 10, 0, 5)
        self.lineFile = QLineEdit(self.frame_4)
        self.lineFile.setObjectName(u"lineFile")
        self.lineFile.setEnabled(True)
        self.lineFile.setMinimumSize(QSize(540, 32))
        font4 = QFont()
        font4.setPointSize(10)
        self.lineFile.setFont(font4)
        self.lineFile.setMouseTracking(True)
        self.lineFile.setReadOnly(True)

        self.horizontalLayout_6.addWidget(self.lineFile)

        self.downloadFile = QPushButton(self.frame_4)
        self.downloadFile.setObjectName(u"downloadFile")
        font5 = QFont()
        font5.setFamilies([u"Yu Gothic UI Semibold"])
        font5.setPointSize(10)
        font5.setBold(True)
        self.downloadFile.setFont(font5)

        self.horizontalLayout_6.addWidget(self.downloadFile)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_3)


        self.verticalLayout_9.addWidget(self.frame_4, 0, Qt.AlignLeft|Qt.AlignTop)

        self.labelError = QLabel(self.ECS)
        self.labelError.setObjectName(u"labelError")
        self.labelError.setFont(font1)

        self.verticalLayout_9.addWidget(self.labelError, 0, Qt.AlignLeft|Qt.AlignTop)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_9.addItem(self.verticalSpacer_3)

        self.sourceData = QTableWidget(self.ECS)
        self.sourceData.setObjectName(u"sourceData")

        self.verticalLayout_9.addWidget(self.sourceData)

        self.startBtn = QPushButton(self.ECS)
        self.startBtn.setObjectName(u"startBtn")
        self.startBtn.setFont(font1)

        self.verticalLayout_9.addWidget(self.startBtn)

        self.model_done_frame = QFrame(self.ECS)
        self.model_done_frame.setObjectName(u"model_done_frame")
        self.model_done_frame.setFrameShape(QFrame.StyledPanel)
        self.model_done_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.model_done_frame)
        self.verticalLayout_11.setSpacing(5)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(5, 5, 5, 5)
        self.label_7 = QLabel(self.model_done_frame)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font3)

        self.verticalLayout_11.addWidget(self.label_7)

        self.label_9 = QLabel(self.model_done_frame)
        self.label_9.setObjectName(u"label_9")
        font6 = QFont()
        font6.setFamilies([u"Yu Gothic UI"])
        font6.setPointSize(14)
        self.label_9.setFont(font6)

        self.verticalLayout_11.addWidget(self.label_9)


        self.verticalLayout_9.addWidget(self.model_done_frame, 0, Qt.AlignLeft|Qt.AlignBottom)

        self.download_part = QFrame(self.ECS)
        self.download_part.setObjectName(u"download_part")
        self.download_part.setFrameShape(QFrame.StyledPanel)
        self.download_part.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.download_part)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(5, -1, -1, -1)
        self.label_8 = QLabel(self.download_part)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font1)

        self.horizontalLayout_9.addWidget(self.label_8)

        self.saveBtn = QPushButton(self.download_part)
        self.saveBtn.setObjectName(u"saveBtn")
        self.saveBtn.setFont(font5)

        self.horizontalLayout_9.addWidget(self.saveBtn)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_4)


        self.verticalLayout_9.addWidget(self.download_part, 0, Qt.AlignLeft|Qt.AlignBottom)

        self.stackedWidget.addWidget(self.ECS)
        self.graphics = QWidget()
        self.graphics.setObjectName(u"graphics")
        self.verticalLayout_10 = QVBoxLayout(self.graphics)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(20, 20, -1, -1)
        self.label_5 = QLabel(self.graphics)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font3)

        self.verticalLayout_10.addWidget(self.label_5, 0, Qt.AlignLeft|Qt.AlignTop)

        self.layout_width = QVBoxLayout()
        self.layout_width.setObjectName(u"layout_width")
        self.layout_up = QHBoxLayout()
        self.layout_up.setObjectName(u"layout_up")
        self.frame_6 = QFrame(self.graphics)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.frame_6)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.tableStats = QTableWidget(self.frame_6)
        self.tableStats.setObjectName(u"tableStats")

        self.verticalLayout_13.addWidget(self.tableStats)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_13.addItem(self.verticalSpacer_4)

        self.pushButton = QPushButton(self.frame_6)
        self.pushButton.setObjectName(u"pushButton")

        self.verticalLayout_13.addWidget(self.pushButton)


        self.layout_up.addWidget(self.frame_6)

        self.frame_5 = QFrame(self.graphics)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.frame_5)
        self.verticalLayout_12.setSpacing(12)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.label_prob = QLabel(self.frame_5)
        self.label_prob.setObjectName(u"label_prob")
        font7 = QFont()
        font7.setFamilies([u"Yu Gothic UI"])
        font7.setPointSize(12)
        self.label_prob.setFont(font7)

        self.verticalLayout_12.addWidget(self.label_prob, 0, Qt.AlignHCenter|Qt.AlignTop)

        self.table_prob = QTableWidget(self.frame_5)
        self.table_prob.setObjectName(u"table_prob")

        self.verticalLayout_12.addWidget(self.table_prob)

        self.probBtn = QPushButton(self.frame_5)
        self.probBtn.setObjectName(u"probBtn")

        self.verticalLayout_12.addWidget(self.probBtn)


        self.layout_up.addWidget(self.frame_5, 0, Qt.AlignLeft)


        self.layout_width.addLayout(self.layout_up)


        self.verticalLayout_10.addLayout(self.layout_width)

        self.stackedWidget.addWidget(self.graphics)
        self.none_graphics = QWidget()
        self.none_graphics.setObjectName(u"none_graphics")
        self.verticalLayout_7 = QVBoxLayout(self.none_graphics)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(20, 20, -1, -1)
        self.label_2 = QLabel(self.none_graphics)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font1)
        self.label_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.verticalLayout_7.addWidget(self.label_2)

        self.label_3 = QLabel(self.none_graphics)
        self.label_3.setObjectName(u"label_3")
        font8 = QFont()
        font8.setFamilies([u"Yu Gothic UI"])
        font8.setPointSize(10)
        self.label_3.setFont(font8)
        self.label_3.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.verticalLayout_7.addWidget(self.label_3)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer_2)

        self.stackedWidget.addWidget(self.none_graphics)
        self.settings = QWidget()
        self.settings.setObjectName(u"settings")
        self.verticalLayout_8 = QVBoxLayout(self.settings)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_6 = QLabel(self.settings)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font8)
        self.label_6.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.label_6)

        self.stackedWidget.addWidget(self.settings)

        self.verticalLayout_5.addWidget(self.stackedWidget)


        self.verticalLayout_4.addWidget(self.mainContent)

        self.footer = QWidget(self.mainBody)
        self.footer.setObjectName(u"footer")
        self.horizontalLayout_2 = QHBoxLayout(self.footer)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(5, 5, 5, 5)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.frame = QFrame(self.footer)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(-1, -1, 24, -1)
        self.proccess = QLabel(self.frame)
        self.proccess.setObjectName(u"proccess")
        font9 = QFont()
        font9.setFamilies([u"Yu Gothic UI"])
        font9.setPointSize(9)
        self.proccess.setFont(font9)

        self.horizontalLayout_3.addWidget(self.proccess)

        self.progressBar = QProgressBar(self.frame)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setMinimumSize(QSize(220, 0))
        self.progressBar.setMaximumSize(QSize(16777215, 12))
        font10 = QFont()
        font10.setFamilies([u"Yu Gothic UI"])
        font10.setPointSize(8)
        self.progressBar.setFont(font10)
        self.progressBar.setValue(0)
        self.progressBar.setTextVisible(True)
        self.progressBar.setOrientation(Qt.Horizontal)
        self.progressBar.setInvertedAppearance(False)

        self.horizontalLayout_3.addWidget(self.progressBar, 0, Qt.AlignHCenter)


        self.horizontalLayout_2.addWidget(self.frame)

        self.sizeGrip = QFrame(self.footer)
        self.sizeGrip.setObjectName(u"sizeGrip")
        self.sizeGrip.setMinimumSize(QSize(20, 20))
        self.sizeGrip.setMaximumSize(QSize(20, 20))
        self.sizeGrip.setFrameShape(QFrame.StyledPanel)
        self.sizeGrip.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_2.addWidget(self.sizeGrip, 0, Qt.AlignRight|Qt.AlignBottom)


        self.verticalLayout_4.addWidget(self.footer, 0, Qt.AlignBottom)


        self.horizontalLayout.addWidget(self.mainBody)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle("")
        self.menuButton.setText("")
        self.classBtn.setText(QCoreApplication.translate("MainWindow", u"   \u041a\u043b\u0430\u0441\u0441\u0438\u0444\u0438\u043a\u0430\u0446\u0438\u044f", None))
        self.analysisBtn.setText(QCoreApplication.translate("MainWindow", u"  \u0410\u043d\u0430\u043b\u0438\u0437 \u0440\u0435\u0437\u0443\u043b\u044c\u0442\u0430\u0442\u043e\u0432", None))
        self.settingsBtn.setText(QCoreApplication.translate("MainWindow", u"  \u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0430 \u043c\u043e\u0434\u0435\u043b\u0438", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<span style=\"color: white;\">\u0421\u0438\u0441\u0442\u0435\u043c\u0430 \u043a\u043b\u0430\u0441\u0441\u0438\u0444\u0438\u043a\u0430\u0446\u0438\u0438 </span> <span style=\"color: #772a8f;\">\u044d\u043b\u0435\u043a\u0442\u0440\u043e\u043a\u043e\u0440\u0442\u0438\u043a\u043e\u0433\u0440\u0430\u043c\u043c</span>\n"
"\n"
"", None))
        self.minimizeBtn.setText("")
        self.resizeBtn.setText("")
        self.closeBtn.setText("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0433\u0440\u0443\u0437\u0438\u0442\u0435 .edf-\u0444\u0430\u0439\u043b \u0434\u043b\u044f \u0440\u0430\u0437\u043c\u0435\u0442\u043a\u0438", None))
        self.lineFile.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u0444\u0430\u0439\u043b...", None))
        self.downloadFile.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0433\u0440\u0443\u0437\u0438\u0442\u044c \u0444\u0430\u0439\u043b", None))
        self.labelError.setText("")
        self.startBtn.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u043f\u0443\u0441\u0442\u0438\u0442\u044c \u043c\u043e\u0434\u0435\u043b\u044c", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=' color:#772a8f;'>\u041c\u043e\u0434\u0435\u043b\u044c \u0443\u0441\u043f\u0435\u0448\u043d\u043e \u0437\u0430\u0432\u0435\u0440\u0448\u0438\u043b\u0430 \u0440\u0430\u0431\u043e\u0442\u0443.</span></p></body></html>", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u0447\u0451\u0442 \u043f\u043e \u0440\u0435\u0437\u0443\u043b\u044c\u0442\u0430\u0442\u0443 \u043a\u043b\u0430\u0441\u0441\u0438\u0444\u0438\u043a\u0430\u0446\u0438\u0438 \u043f\u0440\u0435\u0434\u0441\u0442\u0430\u0432\u043b\u0435\u043d \u043d\u0430 \u0432\u043a\u043b\u0430\u0434\u043a\u0435 \"\u0410\u043d\u0430\u043b\u0438\u0437 \u0440\u0435\u0437\u0443\u043b\u044c\u0442\u0430\u0442\u043e\u0432\".", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0430\u043a\u0436\u0435 \u0432\u044b \u043c\u043e\u0436\u0435\u0442\u0435 \u0441\u043a\u0430\u0447\u0430\u0442\u044c \u0440\u0430\u0437\u043c\u0435\u0447\u0435\u043d\u043d\u044b\u0435 \u0434\u0430\u043d\u043d\u044b\u0435:", None))
        self.saveBtn.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043a\u0430\u0447\u0430\u0442\u044c \u0434\u0430\u043d\u043d\u044b\u0435", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0435\u0437\u0443\u043b\u044c\u0442\u0430\u0442\u044b \u043a\u043b\u0430\u0441\u0441\u0438\u0444\u0438\u043a\u0430\u0446\u0438\u0438", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0431\u043d\u043e\u0432\u0438\u0442\u044c \u0433\u0440\u0430\u0444\u0438\u043a\u0438", None))
        self.label_prob.setText(QCoreApplication.translate("MainWindow", u"csv-\u0444\u0430\u0439\u043b \u0441 \u0432\u0435\u0440\u043e\u044f\u0442\u043d\u043e\u0441\u0442\u044f\u043c\u0438 \u043e\u0442\u043d\u043e\u0448\u0435\u043d\u0438\u044f \u0437\u0430\u043f\u0438\u0441\u0438 \u043a \u043a\u043b\u0430\u0441\u0441\u0430\u043c", None))
        self.probBtn.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043a\u0430\u0447\u0430\u0442\u044c \u043e\u0446\u0435\u043d\u043a\u0443 \u0434\u043e\u0441\u0442\u043e\u0432\u0435\u0440\u043d\u043e\u0441\u0442\u0438", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0434\u0435\u0441\u044c \u043f\u043e\u043a\u0430 \u043d\u0435\u0442 \u0440\u0435\u0437\u0443\u043b\u044c\u0442\u0430\u0442\u043e\u0432", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0433\u0440\u0443\u0437\u0438\u0442\u0435 \u0434\u0430\u043d\u043d\u044b\u0435 \u0438 \u0432\u043e\u0441\u043f\u043e\u043b\u044c\u0437\u0443\u0439\u0442\u0435\u0441\u044c \u043c\u043e\u0434\u0435\u043b\u044c\u044e", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0434\u0435\u0441\u044c \u0432\u044b \u0441\u043c\u043e\u0436\u0435\u0442\u0435 \u0434\u043e\u043e\u0431\u0443\u0447\u0438\u0442\u044c \u043c\u043e\u0434\u0435\u043b\u044c \u043d\u0430 \u043d\u043e\u0432\u044b\u0445 \u0434\u0430\u043d\u043d\u044b\u0445", None))
        self.proccess.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u043f\u043e\u043b\u043d\u0435\u043d\u0438\u0435", None))
    # retranslateUi

