# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 
#'/home/eeddey/Desktop/Capstone/UI/mainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 480)
        MainWindow.setMaximumSize(QtCore.QSize(800, 480))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/icons/FaucetMenuIcon.png"), 
		QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("")
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setEnabled(True)
        self.centralWidget.setMinimumSize(QtCore.QSize(0, 0))
        self.centralWidget.setMaximumSize(QtCore.QSize(800, 480))
        self.centralWidget.setObjectName("centralWidget")
        self.TabWidget = QtWidgets.QTabWidget(self.centralWidget)
        self.TabWidget.setGeometry(QtCore.QRect(0, 0, 800, 480))
        self.TabWidget.setMinimumSize(QtCore.QSize(0, 0))
        self.TabWidget.setMaximumSize(QtCore.QSize(800, 480))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.TabWidget.setFont(font)
        self.TabWidget.setStatusTip("")
        self.TabWidget.setWhatsThis("")
        self.TabWidget.setAccessibleName("")
        self.TabWidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.TabWidget.setTabPosition(QtWidgets.QTabWidget.North)
        self.TabWidget.setUsesScrollButtons(True)
        self.TabWidget.setDocumentMode(False)
        self.TabWidget.setTabsClosable(False)
        self.TabWidget.setMovable(False)
        self.TabWidget.setTabBarAutoHide(False)
        self.TabWidget.setObjectName("TabWidget")
        self.Sensors = QtWidgets.QWidget()
        self.Sensors.setObjectName("Sensors")
        self.GreyWaterLabel = QtWidgets.QLabel(self.Sensors)
        self.GreyWaterLabel.setGeometry(QtCore.QRect(440, 40, 292, 37))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setKerning(True)
        self.GreyWaterLabel.setFont(font)
        self.GreyWaterLabel.setObjectName("GreyWaterLabel")
        self.BlackWaterLabel = QtWidgets.QLabel(self.Sensors)
        self.BlackWaterLabel.setGeometry(QtCore.QRect(440, 228, 293, 36))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setKerning(True)
        self.BlackWaterLabel.setFont(font)
        self.BlackWaterLabel.setObjectName("BlackWaterLabel")
        self.BatteryLabel = QtWidgets.QLabel(self.Sensors)
        self.BatteryLabel.setGeometry(QtCore.QRect(60, 228, 292, 36))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setKerning(True)
        self.BatteryLabel.setFont(font)
        self.BatteryLabel.setObjectName("BatteryLabel")
        self.FreshWaterLabel = QtWidgets.QLabel(self.Sensors)
        self.FreshWaterLabel.setGeometry(QtCore.QRect(60, 37, 293, 37))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setKerning(True)
        self.FreshWaterLabel.setFont(font)
        self.FreshWaterLabel.setObjectName("FreshWaterLabel")
        self.FreshWaterProgressBar = QtWidgets.QProgressBar(self.Sensors)
        self.FreshWaterProgressBar.setGeometry(QtCore.QRect(60, 80, 300, 80))
        self.FreshWaterProgressBar.setMinimumSize(QtCore.QSize(270, 70))
        self.FreshWaterProgressBar.setProperty("value", 24)
        self.FreshWaterProgressBar.setObjectName("FreshWaterProgressBar")
        self.BatteryProgressBar = QtWidgets.QProgressBar(self.Sensors)
        self.BatteryProgressBar.setGeometry(QtCore.QRect(60, 270, 300, 80))
        self.BatteryProgressBar.setMinimumSize(QtCore.QSize(270, 70))
        self.BatteryProgressBar.setProperty("value", 24)
        self.BatteryProgressBar.setObjectName("BatteryProgressBar")
        self.BlackWaterProgressBar = QtWidgets.QProgressBar(self.Sensors)
        self.BlackWaterProgressBar.setGeometry(QtCore.QRect(440, 270, 300, 80))
        self.BlackWaterProgressBar.setMinimumSize(QtCore.QSize(270, 70))
        self.BlackWaterProgressBar.setProperty("value", 24)
        self.BlackWaterProgressBar.setObjectName("BlackWaterProgressBar")
        self.GreyWaterProgressBar = QtWidgets.QProgressBar(self.Sensors)
        self.GreyWaterProgressBar.setGeometry(QtCore.QRect(440, 83, 300, 80))
        self.GreyWaterProgressBar.setMinimumSize(QtCore.QSize(270, 70))
        self.GreyWaterProgressBar.setProperty("value", 24)
        self.GreyWaterProgressBar.setObjectName("GreyWaterProgressBar")
        self.SensorInfoBackground = QtWidgets.QLabel(self.Sensors)
        self.SensorInfoBackground.setGeometry(QtCore.QRect(0, -35, 800, 480))
        self.SensorInfoBackground.setMaximumSize(QtCore.QSize(800, 480))
        self.SensorInfoBackground.setObjectName("SensorInfoBackground")
        self.SensorInfoBackground.raise_()
        self.GreyWaterLabel.raise_()
        self.BlackWaterLabel.raise_()
        self.BatteryLabel.raise_()
        self.FreshWaterLabel.raise_()
        self.FreshWaterProgressBar.raise_()
        self.BatteryProgressBar.raise_()
        self.BlackWaterProgressBar.raise_()
        self.GreyWaterProgressBar.raise_()
        self.TabWidget.addTab(self.Sensors, "")
        self.Usage = QtWidgets.QWidget()
        self.Usage.setObjectName("Usage")
        self.CheckGraphs = QtWidgets.QPushButton(self.Usage)
        self.CheckGraphs.setGeometry(QtCore.QRect(650, 140, 130, 130))
        self.CheckGraphs.setMaximumSize(QtCore.QSize(130, 130))
        self.CheckGraphs.setAutoFillBackground(False)
        self.CheckGraphs.setStyleSheet(
			"background-image: url(:/images/icons/RefreshBttnImg.jpg);")
        self.CheckGraphs.setText("")
        self.CheckGraphs.setObjectName("CheckGraphs")
        self.SensorGraph = MplWidget(self.Usage)
        self.SensorGraph.setGeometry(QtCore.QRect(0, 0, 629, 429))
        self.SensorGraph.setObjectName("SensorGraph")
        self.UsageBackground = QtWidgets.QLabel(self.Usage)
        self.UsageBackground.setGeometry(QtCore.QRect(0, -40, 800, 480))
        self.UsageBackground.setMaximumSize(QtCore.QSize(800, 480))
        self.UsageBackground.setObjectName("UsageBackground")
        self.UsageBackground.raise_()
        self.CheckGraphs.raise_()
        self.SensorGraph.raise_()
        self.TabWidget.addTab(self.Usage, "")
        self.Power = QtWidgets.QWidget()
        self.Power.setObjectName("Power")
        self.powerApp = QtWidgets.QPushButton(self.Power)
        self.powerApp.setGeometry(QtCore.QRect(120, 100, 200, 200))
        self.powerApp.setMinimumSize(QtCore.QSize(200, 200))
        self.powerApp.setMaximumSize(QtCore.QSize(200, 200))
        self.powerApp.setAutoFillBackground(False)
        self.powerApp.setStyleSheet(
			"background-image: url(:/images/icons/AppPwrBttnImg.jpg);")
        self.powerApp.setText("")
        self.powerApp.setObjectName("powerApp")
        self.powerRasberry = QtWidgets.QPushButton(self.Power)
        self.powerRasberry.setGeometry(QtCore.QRect(480, 100, 200, 200))
        self.powerRasberry.setMinimumSize(QtCore.QSize(200, 200))
        self.powerRasberry.setMaximumSize(QtCore.QSize(200, 200))
        self.powerRasberry.setAcceptDrops(False)
        self.powerRasberry.setStyleSheet(
			"background-image: url(:/images/icons/RaspPiPwrBttnImg.jpg);")
        self.powerRasberry.setText("")
        self.powerRasberry.setObjectName("powerRasberry")
        self.SensorInfoBackground_2 = QtWidgets.QLabel(self.Power)
        self.SensorInfoBackground_2.setGeometry(QtCore.QRect(0, -30, 800, 480))
        self.SensorInfoBackground_2.setMaximumSize(QtCore.QSize(800, 480))
        self.SensorInfoBackground_2.setObjectName(
			"SensorInfoBackground_2")
        self.SensorInfoBackground_2.raise_()
        self.powerApp.raise_()
        self.powerRasberry.raise_()
        self.TabWidget.addTab(self.Power, "")
        self.label = QtWidgets.QLabel(self.centralWidget)
        self.label.setGeometry(QtCore.QRect(0, 6, 900, 480))
        self.label.setMaximumSize(QtCore.QSize(900, 480))
        self.label.setObjectName("label")
        self.MainBackground = QtWidgets.QLabel(self.centralWidget)
        self.MainBackground.setGeometry(QtCore.QRect(0, 0, 800, 480))
        self.MainBackground.setMaximumSize(QtCore.QSize(800, 480))
        self.MainBackground.setObjectName("MainBackground")
        self.MainBackground.raise_()
        self.label.raise_()
        self.TabWidget.raise_()
        MainWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(MainWindow)
        self.TabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.powerApp, self.powerRasberry)
        MainWindow.setTabOrder(self.powerRasberry, self.CheckGraphs)

        flags = QtCore.Qt.WindowFlags(QtCore.Qt.FramelessWindowHint | 
			QtCore.Qt.WindowStaysOnTopHint)
        self.setWindowFlags(flags)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate(
			"MainWindow", "Camper Sensor System"))
        self.GreyWaterLabel.setText(_translate(
			"MainWindow", "<html><head/><body><p>"+
			"<span style=\" color:#000000;\">Grey Water</span></p></body>" +
			"</html>"))
        self.BlackWaterLabel.setText(_translate("MainWindow", "<html><head/>" +
			"<body><p><span style=\" color:#000000;\">Black Water</span></p>" +
			"</body></html>"))
        self.BatteryLabel.setText(_translate("MainWindow", "<html><head/>" + 
			"<body><p><span style=\" color:#000000;\">Battery</span></p>" +
			"</body></html>"))
        self.FreshWaterLabel.setText(_translate("MainWindow", "<html><head/>" +
			"<body><p><span style=\" color:#000000;\">Fresh Water</span></p>" +
			"</body></html>"))
        self.FreshWaterProgressBar.setToolTip(_translate("MainWindow", 
			"<html><head/><body><p>Adjust to the content of the fresh water " +
			"tank</p></body></html>"))
        self.SensorInfoBackground.setText(_translate("MainWindow", "<html>" +
			"<head/><body><p><img src=\":/images/icons/background1.jpg\"/></p>"+
			"</body></html>"))
        self.TabWidget.setTabText(self.TabWidget.indexOf(self.Sensors), 
			_translate("MainWindow", "Sensors"))
        self.TabWidget.setTabToolTip(self.TabWidget.indexOf(self.Sensors), 
			_translate("MainWindow", "Click to see status of sensors"))
        self.CheckGraphs.setStatusTip(_translate("MainWindow", 
			"Click to reset the graph."))
        self.CheckGraphs.setWhatsThis(_translate("MainWindow", 
			"Refreshes the graph when clicked."))
        self.UsageBackground.setText(_translate("MainWindow", 
			"<html><head/><body><p>" +
			"<img src=\":/images/icons/background1.jpg\"/></p></body></html>"))
        self.TabWidget.setTabText(self.TabWidget.indexOf(self.Usage), 
			_translate("MainWindow", "Usage"))
        self.TabWidget.setTabToolTip(self.TabWidget.indexOf(self.Usage), 
			_translate("MainWindow", 
			"Click to see a graph of the sensor usage."))
        self.powerApp.setStatusTip(_translate("MainWindow", 
			"Click to turn off the Application"))
        self.powerApp.setWhatsThis(_translate("MainWindow", 
			"Turns off the application"))
        self.powerRasberry.setStatusTip(_translate("MainWindow", 
			"Click to turn off the Raspberry Pi"))
        self.powerRasberry.setWhatsThis(_translate("MainWindow", 
			"Turns off the Raspberry Pi"))
        self.SensorInfoBackground_2.setText(_translate("MainWindow", 
			"<html><head/><body><p>" +
			"<img src=\":/images/icons/background1.jpg\"/></p></body></html>"))
        self.TabWidget.setTabText(self.TabWidget.indexOf(self.Power), 
			_translate("MainWindow", "Power"))
        self.TabWidget.setTabToolTip(self.TabWidget.indexOf(self.Power), 
			_translate("MainWindow", "Click to access power buttons."))
        self.label.setText(_translate("MainWindow", "TextLabel"))
        self.MainBackground.setText(_translate("MainWindow", "<html><head/>" +
			"<body><p><img src=\":/images/icons/background1.jpg\"/></p>" +
			"</body></html>"))


from mplwidget import MplWidget
import image_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
