# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'LSBMainWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.3.2
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QFormLayout, QFrame,
    QGroupBox, QHBoxLayout, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QSpacerItem,
    QSplitter, QTabWidget, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(808, 567)
        MainWindow.setDocumentMode(False)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_11 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.Embed_tab = QWidget()
        self.Embed_tab.setObjectName(u"Embed_tab")
        self.horizontalLayout_3 = QHBoxLayout(self.Embed_tab)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.Embed_tab_splitter = QSplitter(self.Embed_tab)
        self.Embed_tab_splitter.setObjectName(u"Embed_tab_splitter")
        self.Embed_tab_splitter.setBaseSize(QSize(0, 0))
        self.Embed_tab_splitter.setOrientation(Qt.Horizontal)
        self.Controls_frame = QFrame(self.Embed_tab_splitter)
        self.Controls_frame.setObjectName(u"Controls_frame")
        self.verticalLayout_3 = QVBoxLayout(self.Controls_frame)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.Container_groupBox = QGroupBox(self.Controls_frame)
        self.Container_groupBox.setObjectName(u"Container_groupBox")
        self.verticalLayout = QVBoxLayout(self.Container_groupBox)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.Container_file_horizontalLayout = QHBoxLayout()
        self.Container_file_horizontalLayout.setObjectName(u"Container_file_horizontalLayout")
        self.Container_fileChoose_button = QPushButton(self.Container_groupBox)
        self.Container_fileChoose_button.setObjectName(u"Container_fileChoose_button")

        self.Container_file_horizontalLayout.addWidget(self.Container_fileChoose_button)

        self.Container_filePath_line = QLineEdit(self.Container_groupBox)
        self.Container_filePath_line.setObjectName(u"Container_filePath_line")

        self.Container_file_horizontalLayout.addWidget(self.Container_filePath_line)


        self.verticalLayout.addLayout(self.Container_file_horizontalLayout)


        self.verticalLayout_3.addWidget(self.Container_groupBox)

        self.Message_groupBox = QGroupBox(self.Controls_frame)
        self.Message_groupBox.setObjectName(u"Message_groupBox")
        self.verticalLayout_2 = QVBoxLayout(self.Message_groupBox)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.Message_file_horizontalLayout = QHBoxLayout()
        self.Message_file_horizontalLayout.setObjectName(u"Message_file_horizontalLayout")
        self.Message_fileChoose_button = QPushButton(self.Message_groupBox)
        self.Message_fileChoose_button.setObjectName(u"Message_fileChoose_button")

        self.Message_file_horizontalLayout.addWidget(self.Message_fileChoose_button)

        self.Message_filePath_line = QLineEdit(self.Message_groupBox)
        self.Message_filePath_line.setObjectName(u"Message_filePath_line")

        self.Message_file_horizontalLayout.addWidget(self.Message_filePath_line)


        self.verticalLayout_2.addLayout(self.Message_file_horizontalLayout)

        self.Message_hammingCode_checkBox = QCheckBox(self.Message_groupBox)
        self.Message_hammingCode_checkBox.setObjectName(u"Message_hammingCode_checkBox")

        self.verticalLayout_2.addWidget(self.Message_hammingCode_checkBox)


        self.verticalLayout_3.addWidget(self.Message_groupBox)

        self.Metrics_groupBox = QGroupBox(self.Controls_frame)
        self.Metrics_groupBox.setObjectName(u"Metrics_groupBox")
        self.formLayout = QFormLayout(self.Metrics_groupBox)
        self.formLayout.setObjectName(u"formLayout")
        self.PSNR_label = QLabel(self.Metrics_groupBox)
        self.PSNR_label.setObjectName(u"PSNR_label")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.PSNR_label)

        self.PSNR_info = QLabel(self.Metrics_groupBox)
        self.PSNR_info.setObjectName(u"PSNR_info")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.PSNR_info)

        self.SSIM_label = QLabel(self.Metrics_groupBox)
        self.SSIM_label.setObjectName(u"SSIM_label")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.SSIM_label)

        self.SSIM_info = QLabel(self.Metrics_groupBox)
        self.SSIM_info.setObjectName(u"SSIM_info")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.SSIM_info)

        self.Metric1_label = QLabel(self.Metrics_groupBox)
        self.Metric1_label.setObjectName(u"Metric1_label")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.Metric1_label)

        self.Metric1_info = QLabel(self.Metrics_groupBox)
        self.Metric1_info.setObjectName(u"Metric1_info")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.Metric1_info)

        self.Metric2_label = QLabel(self.Metrics_groupBox)
        self.Metric2_label.setObjectName(u"Metric2_label")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.Metric2_label)

        self.Metric2_info = QLabel(self.Metrics_groupBox)
        self.Metric2_info.setObjectName(u"Metric2_info")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.Metric2_info)

        self.Metric3_label = QLabel(self.Metrics_groupBox)
        self.Metric3_label.setObjectName(u"Metric3_label")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.Metric3_label)

        self.Metric3_info = QLabel(self.Metrics_groupBox)
        self.Metric3_info.setObjectName(u"Metric3_info")

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.Metric3_info)


        self.verticalLayout_3.addWidget(self.Metrics_groupBox)

        self.Controls_verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.Controls_verticalSpacer)

        self.Embed_button = QPushButton(self.Controls_frame)
        self.Embed_button.setObjectName(u"Embed_button")

        self.verticalLayout_3.addWidget(self.Embed_button)

        self.Embed_tab_splitter.addWidget(self.Controls_frame)
        self.ShowImage_widget = QWidget(self.Embed_tab_splitter)
        self.ShowImage_widget.setObjectName(u"ShowImage_widget")
        self.horizontalLayout = QHBoxLayout(self.ShowImage_widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.ShowImage_label = QLabel(self.ShowImage_widget)
        self.ShowImage_label.setObjectName(u"ShowImage_label")
        self.ShowImage_label.setBaseSize(QSize(0, 0))

        self.horizontalLayout.addWidget(self.ShowImage_label)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.Embed_tab_splitter.addWidget(self.ShowImage_widget)

        self.horizontalLayout_3.addWidget(self.Embed_tab_splitter)

        self.tabWidget.addTab(self.Embed_tab, "")
        self.Extract_tab = QWidget()
        self.Extract_tab.setObjectName(u"Extract_tab")
        self.horizontalLayout_5 = QHBoxLayout(self.Extract_tab)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.Extract_tab_splitter = QSplitter(self.Extract_tab)
        self.Extract_tab_splitter.setObjectName(u"Extract_tab_splitter")
        self.Extract_tab_splitter.setOrientation(Qt.Horizontal)
        self.Controls_frame_ext = QFrame(self.Extract_tab_splitter)
        self.Controls_frame_ext.setObjectName(u"Controls_frame_ext")
        self.verticalLayout_7 = QVBoxLayout(self.Controls_frame_ext)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.Container_groupBox_ext = QGroupBox(self.Controls_frame_ext)
        self.Container_groupBox_ext.setObjectName(u"Container_groupBox_ext")
        self.verticalLayout_8 = QVBoxLayout(self.Container_groupBox_ext)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.Container_file_horizontalLayout_ext = QHBoxLayout()
        self.Container_file_horizontalLayout_ext.setObjectName(u"Container_file_horizontalLayout_ext")
        self.Container_fileChoose_button_ext = QPushButton(self.Container_groupBox_ext)
        self.Container_fileChoose_button_ext.setObjectName(u"Container_fileChoose_button_ext")

        self.Container_file_horizontalLayout_ext.addWidget(self.Container_fileChoose_button_ext)

        self.Container_filePath_line_ext = QLineEdit(self.Container_groupBox_ext)
        self.Container_filePath_line_ext.setObjectName(u"Container_filePath_line_ext")

        self.Container_file_horizontalLayout_ext.addWidget(self.Container_filePath_line_ext)


        self.verticalLayout_8.addLayout(self.Container_file_horizontalLayout_ext)


        self.verticalLayout_7.addWidget(self.Container_groupBox_ext)

        self.Message_groupBox_ext = QGroupBox(self.Controls_frame_ext)
        self.Message_groupBox_ext.setObjectName(u"Message_groupBox_ext")
        self.verticalLayout_9 = QVBoxLayout(self.Message_groupBox_ext)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.Message_file_horizontalLayout_ext = QHBoxLayout()
        self.Message_file_horizontalLayout_ext.setObjectName(u"Message_file_horizontalLayout_ext")
        self.Message_fileChoose_button_ext = QPushButton(self.Message_groupBox_ext)
        self.Message_fileChoose_button_ext.setObjectName(u"Message_fileChoose_button_ext")

        self.Message_file_horizontalLayout_ext.addWidget(self.Message_fileChoose_button_ext)

        self.Message_filePath_line_ext = QLineEdit(self.Message_groupBox_ext)
        self.Message_filePath_line_ext.setObjectName(u"Message_filePath_line_ext")

        self.Message_file_horizontalLayout_ext.addWidget(self.Message_filePath_line_ext)


        self.verticalLayout_9.addLayout(self.Message_file_horizontalLayout_ext)

        self.Message_hammingCode_checkBox_ext = QCheckBox(self.Message_groupBox_ext)
        self.Message_hammingCode_checkBox_ext.setObjectName(u"Message_hammingCode_checkBox_ext")

        self.verticalLayout_9.addWidget(self.Message_hammingCode_checkBox_ext)


        self.verticalLayout_7.addWidget(self.Message_groupBox_ext)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer)

        self.Extract_button = QPushButton(self.Controls_frame_ext)
        self.Extract_button.setObjectName(u"Extract_button")

        self.verticalLayout_7.addWidget(self.Extract_button)

        self.Extract_tab_splitter.addWidget(self.Controls_frame_ext)
        self.ShowImage_widget_ext = QWidget(self.Extract_tab_splitter)
        self.ShowImage_widget_ext.setObjectName(u"ShowImage_widget_ext")
        self.horizontalLayout_2 = QHBoxLayout(self.ShowImage_widget_ext)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_3)

        self.ShowImage_label_ext = QLabel(self.ShowImage_widget_ext)
        self.ShowImage_label_ext.setObjectName(u"ShowImage_label_ext")

        self.horizontalLayout_2.addWidget(self.ShowImage_label_ext)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_4)

        self.Extract_tab_splitter.addWidget(self.ShowImage_widget_ext)

        self.horizontalLayout_5.addWidget(self.Extract_tab_splitter)

        self.tabWidget.addTab(self.Extract_tab, "")

        self.verticalLayout_11.addWidget(self.tabWidget)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"LSB", None))
        self.Container_groupBox.setTitle(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043d\u0442\u0435\u0439\u043d\u0435\u0440", None))
        self.Container_fileChoose_button.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u043e\u0440 \u0444\u0430\u0439\u043b\u0430", None))
        self.Container_filePath_line.setText("")
        self.Message_groupBox.setTitle(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u043e\u0431\u0449\u0435\u043d\u0438\u0435", None))
        self.Message_fileChoose_button.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u043e\u0440 \u0444\u0430\u0439\u043b\u0430", None))
        self.Message_filePath_line.setText("")
        self.Message_hammingCode_checkBox.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u0434 \u0425\u044d\u043c\u043c\u0438\u043d\u0433\u0430", None))
        self.Metrics_groupBox.setTitle(QCoreApplication.translate("MainWindow", u"\u041c\u0435\u0442\u0440\u0438\u043a\u0438", None))
        self.PSNR_label.setText(QCoreApplication.translate("MainWindow", u"PSNR:", None))
        self.PSNR_info.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.SSIM_label.setText(QCoreApplication.translate("MainWindow", u"SSIM:", None))
        self.SSIM_info.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.Metric1_label.setText(QCoreApplication.translate("MainWindow", u"UQI:", None))
        self.Metric1_info.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.Metric2_label.setText(QCoreApplication.translate("MainWindow", u"SSC:", None))
        self.Metric2_info.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.Metric3_label.setText(QCoreApplication.translate("MainWindow", u"MSE:", None))
        self.Metric3_info.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.Embed_button.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0441\u0442\u0440\u043e\u0438\u0442\u044c", None))
        self.ShowImage_label.setText(QCoreApplication.translate("MainWindow", u"\u0418\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435 \u043d\u0435 \u0432\u044b\u0431\u0440\u0430\u043d\u043e", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Embed_tab), QCoreApplication.translate("MainWindow", u"\u0412\u0441\u0442\u0440\u0430\u0438\u0432\u0430\u043d\u0438\u0435", None))
        self.Container_groupBox_ext.setTitle(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043d\u0442\u0435\u0439\u043d\u0435\u0440", None))
        self.Container_fileChoose_button_ext.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u043e\u0440 \u0444\u0430\u0439\u043b\u0430", None))
        self.Container_filePath_line_ext.setText("")
        self.Message_groupBox_ext.setTitle(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u043e\u0431\u0449\u0435\u043d\u0438\u0435", None))
        self.Message_fileChoose_button_ext.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u043e\u0440 \u0444\u0430\u0439\u043b\u0430", None))
        self.Message_filePath_line_ext.setText("")
        self.Message_hammingCode_checkBox_ext.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u0434 \u0425\u044d\u043c\u043c\u0438\u043d\u0433\u0430", None))
        self.Extract_button.setText(QCoreApplication.translate("MainWindow", u"\u0418\u0437\u0432\u043b\u0435\u0447\u044c", None))
        self.ShowImage_label_ext.setText(QCoreApplication.translate("MainWindow", u"\u0418\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435 \u043d\u0435 \u0432\u044b\u0431\u0440\u0430\u043d\u043e", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Extract_tab), QCoreApplication.translate("MainWindow", u"\u0418\u0437\u0432\u043b\u0435\u0447\u0435\u043d\u0438\u0435", None))
    # retranslateUi

