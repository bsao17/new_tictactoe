# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tictactoe_ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(900, 922)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(98, 160, 234))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(98, 160, 234))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(98, 160, 234))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(98, 160, 234))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        MainWindow.setPalette(palette)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setEnabled(True)
        self.centralwidget.setMinimumSize(QtCore.QSize(900, 900))
        self.centralwidget.setMaximumSize(QtCore.QSize(0, 0))
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 0, 0, 1, 1)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_6.addItem(spacerItem2)
        self.pushButton_1 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_1.setMinimumSize(QtCore.QSize(200, 200))
        self.pushButton_1.setMaximumSize(QtCore.QSize(200, 200))
        self.pushButton_1.setText("")
        self.pushButton_1.setIconSize(QtCore.QSize(16, 16))
        self.pushButton_1.setObjectName("pushButton_1")
        self.verticalLayout_6.addWidget(self.pushButton_1)
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setMinimumSize(QtCore.QSize(200, 200))
        self.pushButton_5.setMaximumSize(QtCore.QSize(200, 200))
        self.pushButton_5.setText("")
        self.pushButton_5.setObjectName("pushButton_5")
        self.verticalLayout_6.addWidget(self.pushButton_5)
        self.pushButton_9 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_9.setMinimumSize(QtCore.QSize(200, 200))
        self.pushButton_9.setMaximumSize(QtCore.QSize(200, 200))
        self.pushButton_9.setText("")
        self.pushButton_9.setObjectName("pushButton_9")
        self.verticalLayout_6.addWidget(self.pushButton_9)
        self.pushButton_13 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_13.setMinimumSize(QtCore.QSize(200, 200))
        self.pushButton_13.setMaximumSize(QtCore.QSize(200, 200))
        self.pushButton_13.setText("")
        self.pushButton_13.setObjectName("pushButton_130")
        self.verticalLayout_6.addWidget(self.pushButton_13)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_6.addItem(spacerItem3)
        self.gridLayout.addLayout(self.verticalLayout_6, 0, 1, 1, 1)
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_10.addItem(spacerItem4)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setMinimumSize(QtCore.QSize(200, 200))
        self.pushButton_2.setMaximumSize(QtCore.QSize(200, 200))
        self.pushButton_2.setText("")
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout_10.addWidget(self.pushButton_2)
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setMinimumSize(QtCore.QSize(200, 200))
        self.pushButton_6.setMaximumSize(QtCore.QSize(200, 200))
        self.pushButton_6.setText("")
        self.pushButton_6.setObjectName("pushButton_6")
        self.verticalLayout_10.addWidget(self.pushButton_6)
        self.pushButton_10 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_10.setMinimumSize(QtCore.QSize(200, 200))
        self.pushButton_10.setMaximumSize(QtCore.QSize(200, 200))
        self.pushButton_10.setText("")
        self.pushButton_10.setObjectName("pushButton_100")
        self.verticalLayout_10.addWidget(self.pushButton_10)
        self.pushButton_14 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_14.setMinimumSize(QtCore.QSize(200, 200))
        self.pushButton_14.setMaximumSize(QtCore.QSize(200, 200))
        self.pushButton_14.setText("")
        self.pushButton_14.setObjectName("pushButton_14")
        self.verticalLayout_10.addWidget(self.pushButton_14)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_10.addItem(spacerItem5)
        self.gridLayout.addLayout(self.verticalLayout_10, 0, 2, 1, 1)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_7.addItem(spacerItem6)
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setMinimumSize(QtCore.QSize(200, 200))
        self.pushButton_3.setMaximumSize(QtCore.QSize(200, 200))
        self.pushButton_3.setText("")
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout_7.addWidget(self.pushButton_3)
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setMinimumSize(QtCore.QSize(200, 200))
        self.pushButton_7.setMaximumSize(QtCore.QSize(200, 200))
        self.pushButton_7.setText("")
        self.pushButton_7.setObjectName("pushButton_7")
        self.verticalLayout_7.addWidget(self.pushButton_7)
        self.pushButton_11 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_11.setMinimumSize(QtCore.QSize(200, 200))
        self.pushButton_11.setMaximumSize(QtCore.QSize(200, 200))
        self.pushButton_11.setText("")
        self.pushButton_11.setObjectName("pushButton_110")
        self.verticalLayout_7.addWidget(self.pushButton_11)
        self.pushButton_15 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_15.setMinimumSize(QtCore.QSize(200, 200))
        self.pushButton_15.setMaximumSize(QtCore.QSize(200, 200))
        self.pushButton_15.setText("")
        self.pushButton_15.setObjectName("pushButton_15")
        self.verticalLayout_7.addWidget(self.pushButton_15)
        spacerItem7 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_7.addItem(spacerItem7)
        self.gridLayout.addLayout(self.verticalLayout_7, 0, 3, 1, 1)
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        spacerItem8 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_8.addItem(spacerItem8)
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setMinimumSize(QtCore.QSize(0, 200))
        self.pushButton_4.setMaximumSize(QtCore.QSize(200, 200))
        self.pushButton_4.setText("")
        self.pushButton_4.setObjectName("pushButton_4")
        self.verticalLayout_8.addWidget(self.pushButton_4)
        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.setMinimumSize(QtCore.QSize(0, 200))
        self.pushButton_8.setMaximumSize(QtCore.QSize(200, 200))
        self.pushButton_8.setText("")
        self.pushButton_8.setObjectName("pushButton_8")
        self.verticalLayout_8.addWidget(self.pushButton_8)
        self.pushButton_12 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_12.setMinimumSize(QtCore.QSize(200, 200))
        self.pushButton_12.setMaximumSize(QtCore.QSize(200, 200))
        self.pushButton_12.setText("")
        self.pushButton_12.setObjectName("pushButton_120")
        self.verticalLayout_8.addWidget(self.pushButton_12)
        self.pushButton_16 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_16.setMinimumSize(QtCore.QSize(200, 200))
        self.pushButton_16.setMaximumSize(QtCore.QSize(200, 200))
        self.pushButton_16.setText("")
        self.pushButton_16.setObjectName("pushButton_16")
        self.verticalLayout_8.addWidget(self.pushButton_16)
        spacerItem9 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_8.addItem(spacerItem9)
        self.gridLayout.addLayout(self.verticalLayout_8, 0, 4, 1, 1)
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem10, 0, 5, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        spacerItem11 = QtWidgets.QSpacerItem(879, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem11)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem12 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem12)
        self.pushButton_stop = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_stop.setMinimumSize(QtCore.QSize(100, 50))
        self.pushButton_stop.setMaximumSize(QtCore.QSize(16777215, 50))
        self.pushButton_stop.setObjectName("pushButton_19")
        self.horizontalLayout_2.addWidget(self.pushButton_stop)
        spacerItem13 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem13)
        self.pushButton_start = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_start.setMinimumSize(QtCore.QSize(100, 50))
        self.pushButton_start.setMaximumSize(QtCore.QSize(16777215, 50))
        self.pushButton_start.setObjectName("pushButton_18")
        self.horizontalLayout_2.addWidget(self.pushButton_start)
        spacerItem14 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem14)
        self.pushButton_reset = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_reset.setMinimumSize(QtCore.QSize(100, 50))
        self.pushButton_reset.setMaximumSize(QtCore.QSize(16777215, 50))
        self.pushButton_reset.setObjectName("pushButton_17")
        self.horizontalLayout_2.addWidget(self.pushButton_reset)
        spacerItem15 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem15)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Tic Tac Toe "))
        self.pushButton_stop.setText(_translate("MainWindow", "STOP"))
        self.pushButton_start.setText(_translate("MainWindow", "START"))
        self.pushButton_reset.setText(_translate("MainWindow", "RESET"))
