# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_widget.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QButtonGroup, QGroupBox,
    QHBoxLayout, QLabel, QLineEdit, QListView,
    QListWidget, QListWidgetItem, QPushButton, QRadioButton,
    QSizePolicy, QSpacerItem, QTabWidget, QTextEdit,
    QVBoxLayout, QWidget)

class Ui_Form1(object):
    def setupUi(self, Form1):
        if not Form1.objectName():
            Form1.setObjectName(u"Form1")
        Form1.resize(587, 511)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(100)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form1.sizePolicy().hasHeightForWidth())
        Form1.setSizePolicy(sizePolicy)
        self.tabWidget = QTabWidget(Form1)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(0, 0, 591, 521))
        self.tab_scan = QWidget()
        self.tab_scan.setObjectName(u"tab_scan")
        self.layoutWidget = QWidget(self.tab_scan)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 20, 521, 391))
        self.verticalLayout_5 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.lineEdit_scan_input = QLineEdit(self.layoutWidget)
        self.lineEdit_scan_input.setObjectName(u"lineEdit_scan_input")

        self.verticalLayout_5.addWidget(self.lineEdit_scan_input)

        self.listWidget_scan_show = QListWidget(self.layoutWidget)
        self.listWidget_scan_show.setObjectName(u"listWidget_scan_show")
        self.listWidget_scan_show.setMaximumSize(QSize(16777215, 351))
        self.listWidget_scan_show.setEditTriggers(QAbstractItemView.DoubleClicked|QAbstractItemView.EditKeyPressed)
        self.listWidget_scan_show.setDragEnabled(True)
        self.listWidget_scan_show.setDragDropMode(QAbstractItemView.DropOnly)
        self.listWidget_scan_show.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.listWidget_scan_show.setSelectionBehavior(QAbstractItemView.SelectItems)
        self.listWidget_scan_show.setVerticalScrollMode(QAbstractItemView.ScrollPerItem)
        self.listWidget_scan_show.setMovement(QListView.Static)
        self.listWidget_scan_show.setResizeMode(QListView.Fixed)
        self.listWidget_scan_show.setViewMode(QListView.ListMode)

        self.verticalLayout_5.addWidget(self.listWidget_scan_show)

        self.pushButton_scan_delete = QPushButton(self.layoutWidget)
        self.pushButton_scan_delete.setObjectName(u"pushButton_scan_delete")

        self.verticalLayout_5.addWidget(self.pushButton_scan_delete)

        self.pushButton_save_list = QPushButton(self.layoutWidget)
        self.pushButton_save_list.setObjectName(u"pushButton_save_list")

        self.verticalLayout_5.addWidget(self.pushButton_save_list)

        self.textEdit_quantity = QTextEdit(self.tab_scan)
        self.textEdit_quantity.setObjectName(u"textEdit_quantity")
        self.textEdit_quantity.setGeometry(QRect(370, 420, 161, 51))
        font = QFont()
        font.setPointSize(20)
        self.textEdit_quantity.setFont(font)
        self.textEdit_quantity.setReadOnly(True)
        self.label = QLabel(self.tab_scan)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(310, 440, 61, 21))
        font1 = QFont()
        font1.setPointSize(12)
        self.label.setFont(font1)
        self.tabWidget.addTab(self.tab_scan, "")
        self.tab_assign = QWidget()
        self.tab_assign.setObjectName(u"tab_assign")
        self.textEdit_file = QTextEdit(self.tab_assign)
        self.textEdit_file.setObjectName(u"textEdit_file")
        self.textEdit_file.setGeometry(QRect(280, 0, 301, 481))
        self.textEdit_file.setReadOnly(True)
        self.layoutWidget1 = QWidget(self.tab_assign)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(10, 320, 241, 151))
        self.verticalLayout_3 = QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_status = QLabel(self.layoutWidget1)
        self.label_status.setObjectName(u"label_status")

        self.horizontalLayout_3.addWidget(self.label_status)

        self.lineEdit_status = QLineEdit(self.layoutWidget1)
        self.lineEdit_status.setObjectName(u"lineEdit_status")
        self.lineEdit_status.setReadOnly(True)

        self.horizontalLayout_3.addWidget(self.lineEdit_status)


        self.verticalLayout_3.addLayout(self.horizontalLayout_3)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButton_reload = QPushButton(self.layoutWidget1)
        self.pushButton_reload.setObjectName(u"pushButton_reload")

        self.horizontalLayout.addWidget(self.pushButton_reload)

        self.pushButton_clear_file = QPushButton(self.layoutWidget1)
        self.pushButton_clear_file.setObjectName(u"pushButton_clear_file")

        self.horizontalLayout.addWidget(self.pushButton_clear_file)

        self.pushButton_open_archive = QPushButton(self.layoutWidget1)
        self.pushButton_open_archive.setObjectName(u"pushButton_open_archive")

        self.horizontalLayout.addWidget(self.pushButton_open_archive)


        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_barcode_count = QLabel(self.layoutWidget1)
        self.label_barcode_count.setObjectName(u"label_barcode_count")

        self.horizontalLayout_2.addWidget(self.label_barcode_count)

        self.lineEdit_barcode_count = QLineEdit(self.layoutWidget1)
        self.lineEdit_barcode_count.setObjectName(u"lineEdit_barcode_count")
        self.lineEdit_barcode_count.setReadOnly(True)

        self.horizontalLayout_2.addWidget(self.lineEdit_barcode_count)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.pushButton_start = QPushButton(self.layoutWidget1)
        self.pushButton_start.setObjectName(u"pushButton_start")
        self.pushButton_start.setEnabled(False)

        self.verticalLayout_3.addWidget(self.pushButton_start)

        self.label_time_elapsed = QLabel(self.layoutWidget1)
        self.label_time_elapsed.setObjectName(u"label_time_elapsed")
        self.label_time_elapsed.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_time_elapsed)

        self.layoutWidget2 = QWidget(self.tab_assign)
        self.layoutWidget2.setObjectName(u"layoutWidget2")
        self.layoutWidget2.setGeometry(QRect(10, 0, 269, 308))
        self.verticalLayout_4 = QVBoxLayout(self.layoutWidget2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.groupBox_2 = QGroupBox(self.layoutWidget2)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.verticalLayout = QVBoxLayout(self.groupBox_2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.radioButton_mode_batch = QRadioButton(self.groupBox_2)
        self.mode_group = QButtonGroup(Form1)
        self.mode_group.setObjectName(u"mode_group")
        self.mode_group.addButton(self.radioButton_mode_batch)
        self.radioButton_mode_batch.setObjectName(u"radioButton_mode_batch")
        self.radioButton_mode_batch.setChecked(True)

        self.verticalLayout.addWidget(self.radioButton_mode_batch)

        self.radioButton_mode_single = QRadioButton(self.groupBox_2)
        self.mode_group.addButton(self.radioButton_mode_single)
        self.radioButton_mode_single.setObjectName(u"radioButton_mode_single")
        self.radioButton_mode_single.setChecked(False)

        self.verticalLayout.addWidget(self.radioButton_mode_single)


        self.verticalLayout_4.addWidget(self.groupBox_2)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer)

        self.groupBox_loc = QGroupBox(self.layoutWidget2)
        self.groupBox_loc.setObjectName(u"groupBox_loc")
        self.verticalLayout_6 = QVBoxLayout(self.groupBox_loc)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalGroupBox = QGroupBox(self.groupBox_loc)
        self.verticalGroupBox.setObjectName(u"verticalGroupBox")
        self.verticalGroupBox.setMinimumSize(QSize(90, 0))
        self.verticalLayout_2 = QVBoxLayout(self.verticalGroupBox)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.radioButton_loc_interval = QRadioButton(self.verticalGroupBox)
        self.loc_group = QButtonGroup(Form1)
        self.loc_group.setObjectName(u"loc_group")
        self.loc_group.addButton(self.radioButton_loc_interval)
        self.radioButton_loc_interval.setObjectName(u"radioButton_loc_interval")
        self.radioButton_loc_interval.setChecked(True)

        self.verticalLayout_2.addWidget(self.radioButton_loc_interval)

        self.radioButton_loc_stanok = QRadioButton(self.verticalGroupBox)
        self.loc_group.addButton(self.radioButton_loc_stanok)
        self.radioButton_loc_stanok.setObjectName(u"radioButton_loc_stanok")

        self.verticalLayout_2.addWidget(self.radioButton_loc_stanok)

        self.radioButton_loc_sobrano = QRadioButton(self.verticalGroupBox)
        self.loc_group.addButton(self.radioButton_loc_sobrano)
        self.radioButton_loc_sobrano.setObjectName(u"radioButton_loc_sobrano")

        self.verticalLayout_2.addWidget(self.radioButton_loc_sobrano)

        self.radioButton_loc_other = QRadioButton(self.verticalGroupBox)
        self.loc_group.addButton(self.radioButton_loc_other)
        self.radioButton_loc_other.setObjectName(u"radioButton_loc_other")

        self.verticalLayout_2.addWidget(self.radioButton_loc_other)


        self.verticalLayout_6.addWidget(self.verticalGroupBox)

        self.lineEdit_custom_loc = QLineEdit(self.groupBox_loc)
        self.lineEdit_custom_loc.setObjectName(u"lineEdit_custom_loc")
        self.lineEdit_custom_loc.setEnabled(True)
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.lineEdit_custom_loc.sizePolicy().hasHeightForWidth())
        self.lineEdit_custom_loc.setSizePolicy(sizePolicy1)
        self.lineEdit_custom_loc.setClearButtonEnabled(False)

        self.verticalLayout_6.addWidget(self.lineEdit_custom_loc)

        self.pushButton_show_loc = QPushButton(self.groupBox_loc)
        self.pushButton_show_loc.setObjectName(u"pushButton_show_loc")

        self.verticalLayout_6.addWidget(self.pushButton_show_loc)


        self.verticalLayout_4.addWidget(self.groupBox_loc)

        self.tabWidget.addTab(self.tab_assign, "")
        self.pushButton_easter = QPushButton(Form1)
        self.pushButton_easter.setObjectName(u"pushButton_easter")
        self.pushButton_easter.setGeometry(QRect(880, 160, 181, 41))

        self.retranslateUi(Form1)

        self.tabWidget.setCurrentIndex(0)
        self.pushButton_reload.setDefault(False)


        QMetaObject.connectSlotsByName(Form1)
    # setupUi

    def retranslateUi(self, Form1):
        Form1.setWindowTitle(QCoreApplication.translate("Form1", u"BatchBar", None))
        self.lineEdit_scan_input.setPlaceholderText(QCoreApplication.translate("Form1", u"\u0441\u043a\u0430\u043d\u0438\u0440\u043e\u0432\u0430\u0442\u044c \u0441\u044e\u0434\u0430", None))
        self.pushButton_scan_delete.setText(QCoreApplication.translate("Form1", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
        self.pushButton_save_list.setText(QCoreApplication.translate("Form1", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
        self.label.setText(QCoreApplication.translate("Form1", u"\u041a\u043e\u043b-\u0432\u043e:", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_scan), QCoreApplication.translate("Form1", u"\u0421\u043a\u0430\u043d\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u0435", None))
        self.label_status.setText(QCoreApplication.translate("Form1", u"\u0421\u0442\u0430\u0442\u0443\u0441:", None))
        self.pushButton_reload.setText(QCoreApplication.translate("Form1", u"\u041e\u0431\u043d\u043e\u0432\u0438\u0442\u044c", None))
        self.pushButton_clear_file.setText(QCoreApplication.translate("Form1", u"\u0412 \u0430\u0440\u0445\u0438\u0432", None))
        self.pushButton_open_archive.setText(QCoreApplication.translate("Form1", u"\u0410\u0440\u0445\u0438\u0432", None))
        self.label_barcode_count.setText(QCoreApplication.translate("Form1", u"\u0428\u0442\u0440\u0438\u0445\u043a\u043e\u0434\u043e\u0432:", None))
        self.pushButton_start.setText(QCoreApplication.translate("Form1", u"\u041f\u0420\u0418\u0421\u0412\u041e\u0418\u0422\u042c", None))
        self.label_time_elapsed.setText("")
        self.groupBox_2.setTitle(QCoreApplication.translate("Form1", u"\u0420\u0435\u0436\u0438\u043c \u0440\u0430\u0431\u043e\u0442\u044b", None))
        self.radioButton_mode_batch.setText(QCoreApplication.translate("Form1", u"BATCH (\u0412\u0441\u0435 \u0448\u0442\u0440\u0438\u0445\u043a\u043e\u0434\u044b \u0432 \u043e\u0434\u043d\u0443 \u043b\u043e\u043a\u0430\u0446\u0438\u044e)", None))
        self.radioButton_mode_single.setText(QCoreApplication.translate("Form1", u"SINGLE (\u041f\u043e\u0441\u043b\u0435\u0434\u043e\u0432\u0430\u0442\u0435\u043b\u044c\u043d\u044b\u0439 \u0440\u0435\u0436\u0438\u043c)", None))
        self.groupBox_loc.setTitle(QCoreApplication.translate("Form1", u"\u0412\u044b\u0431\u043e\u0440 \u043b\u043e\u043a\u0430\u0446\u0438\u0438", None))
        self.verticalGroupBox.setTitle("")
        self.radioButton_loc_interval.setText(QCoreApplication.translate("Form1", u"INTERVAL", None))
        self.radioButton_loc_stanok.setText(QCoreApplication.translate("Form1", u"STANOK", None))
        self.radioButton_loc_sobrano.setText(QCoreApplication.translate("Form1", u"SOBRANO_V_STANOK", None))
        self.radioButton_loc_other.setText(QCoreApplication.translate("Form1", u"\u0414\u0440\u0443\u0433\u0430\u044f \u043b\u043e\u043a\u0430\u0446\u0438\u044f", None))
        self.lineEdit_custom_loc.setPlaceholderText(QCoreApplication.translate("Form1", u"\u041b\u043e\u043a\u0430\u0446\u0438\u044f", None))
        self.pushButton_show_loc.setText(QCoreApplication.translate("Form1", u"\u0412\u044b\u0432\u0435\u0441\u0442\u0438 \u0441\u043e\u0434\u0435\u0440\u0436\u0438\u043c\u043e\u0435 \u043b\u043e\u043a\u0430\u0446\u0438\u0438", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_assign), QCoreApplication.translate("Form1", u"\u041f\u0440\u0438\u0441\u0432\u043e\u0435\u043d\u0438\u0435", None))
        self.pushButton_easter.setText(QCoreApplication.translate("Form1", u"\u041e\u0419, \u0437\u0434\u0440\u0430\u0432\u0441\u0442\u0432\u0443\u0439\u0442\u0435", None))
    # retranslateUi

