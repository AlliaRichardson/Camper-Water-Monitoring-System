# -*- coding: utf-8 -*-

import WaterUsageInfo
#import BatteryInfo
import Database
import sys
import time
import randomNum
import datetime
from subprocess import call

from PyQt5 import QtCore,  QtGui
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMainWindow, QMessageBox
from matplotlib.backends.backend_qt5agg import (NavigationToolbar2QT as NavigationToolbar)
import numpy as np
import random
from .Ui_mainWindow import Ui_MainWindow

class MainWindow(QMainWindow, Ui_MainWindow):
    #Constructor for the MainWindow Class
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        self.setupUi(self)
        #Creates an object of threadclass
        self.threadclass = ThreadClass()
        #starts a thread
        self.threadclass.start()
        #Connects to the emitters in the thread class so it can set the sensor's progressbar value
        self.threadclass.freshWaterSig.connect(self.on_FreshWaterProgressBar_valueChanged)
        self.threadclass.greyWaterSig.connect(self.on_GreyWaterProgressBar_valueChanged)
        self.threadclass.blackWaterSig.connect(self.on_BlackWaterProgressBar_valueChanged)
        self.threadclass.batterySig.connect(self.on_BatteryProgressBar_valueChanged)
       
    
    @pyqtSlot(int)
    def on_FreshWaterProgressBar_valueChanged(self, value):
        #Sets the value that will will be shown in the progress bar
        self.FreshWaterProgressBar.setProperty("value", value)
        #If the value is greater than or equal to 50% the progress bar is green
        if value >= 50:
            #creates a new palette object
            palette = QtGui.QPalette(self.palette())
            #Determines the color that the palette will be, in this case green
            palette.setColor(QtGui.QPalette.Highlight, QtGui.QColor(QtCore.Qt.green))
            #Sets the palette
            self.FreshWaterProgressBar.setPalette(palette)
        #If the value is greater than or equal to 20% the progress bar is green    
        elif value >= 20:
            #creates a new palette object
            palette = QtGui.QPalette(self.palette())
            #Determines the color that the palette will be, in this case orange
            palette.setColor(QtGui.QPalette.Highlight, QtGui.QColor(255, 165, 0))
            #Sets the palette
            self.FreshWaterProgressBar.setPalette(palette)
        #Else the progress bar is set to red  the danger zone
        else:
            #creates a new palette object
            palette = QtGui.QPalette(self.palette())
            #Determines the color that the palette will be, in this case red
            palette.setColor(QtGui.QPalette.Highlight, QtGui.QColor(QtCore.Qt.red))
            #Sets the palette
            self.FreshWaterProgressBar.setPalette(palette)    
    
    @pyqtSlot(int)
    def on_BlackWaterProgressBar_valueChanged(self, value):
        #Sets the value that will will be shown in the progress bar
        self.BlackWaterProgressBar.setProperty("value", value)
        #If the value is less than or equal to 50% the progress bar is green
        if value < 10:
            #creates a new palette object
            palette = QtGui.QPalette(self.palette())
            #Determines the color that the palette will be, in this case green
            palette.setColor(QtGui.QPalette.Highlight, QtGui.QColor(QtCore.Qt.green))
            #Sets the palette
            self.BlackWaterProgressBar.setPalette(palette)
        #If the value is less than or equal to 80% the progress bar is green  
        elif value <= 50:
            #creates a new palette object
            palette = QtGui.QPalette(self.palette())
            #Determines the color that the palette will be, in this case orange
            palette.setColor(QtGui.QPalette.Highlight, QtGui.QColor(255, 165, 0))
            #Sets the palette
            self.BlackWaterProgressBar.setPalette(palette)
        #Else the progress bar is set to red  the danger zone
        else:
            #creates a new palette object
            palette = QtGui.QPalette(self.palette())
            #Determines the color that the palette will be, in this case red
            palette.setColor(QtGui.QPalette.Highlight, QtGui.QColor(QtCore.Qt.red))
            #Sets the palette
            self.BlackWaterProgressBar.setPalette(palette)  
    
    @pyqtSlot(int)
    def on_GreyWaterProgressBar_valueChanged(self, value):
        #Sets the value that will will be shown in the progress bar
        self.GreyWaterProgressBar.setProperty("value", value)
        #If the value is less than or equal to 50% the progress bar is green
        if value < 10:
            #creates a new palette object
            palette = QtGui.QPalette(self.palette())
            #Determines the color that the palette will be, in this case green
            palette.setColor(QtGui.QPalette.Highlight, QtGui.QColor(QtCore.Qt.green))
            #Sets the palette
            self.GreyWaterProgressBar.setPalette(palette)
        #If the value is less than or equal to 80% the progress bar is green  
        elif value <= 50:
            #creates a new palette object
            palette = QtGui.QPalette(self.palette())
            #Determines the color that the palette will be, in this case orange
            palette.setColor(QtGui.QPalette.Highlight, QtGui.QColor(255, 165, 0))
            #Sets the palette
            self.GreyWaterProgressBar.setPalette(palette)
        #Else the progress bar is set to red  the danger zone
        else:
            #creates a new palette object
            palette = QtGui.QPalette(self.palette())
            #Determines the color that the palette will be, in this case red
            palette.setColor(QtGui.QPalette.Highlight, QtGui.QColor(QtCore.Qt.red))
            #Sets the palette
            self.GreyWaterProgressBar.setPalette(palette)  
    
    @pyqtSlot(int)
    def on_BatteryProgressBar_valueChanged(self, value):
        #Sets the value that will will be shown in the progress bar
        self.BatteryProgressBar.setProperty("value", value)
        #If the value is greater than or equal to 50% the progress bar is green
        if value >= 50:
            #creates a new palette object
            palette = QtGui.QPalette(self.palette())
            #Determines the color that the palette will be, in this case green
            palette.setColor(QtGui.QPalette.Highlight, QtGui.QColor(QtCore.Qt.green))
            #Sets the palette
            self.BatteryProgressBar.setPalette(palette)
        #If the value is greater than or equal to 20% the progress bar is green    
        elif value >= 20:
            #creates a new palette object
            palette = QtGui.QPalette(self.palette())
            #Determines the color that the palette will be, in this case orange
            palette.setColor(QtGui.QPalette.Highlight, QtGui.QColor(255, 165, 0))
            #Sets the palette
            self.BatteryProgressBar.setPalette(palette)
        #Else the progress bar is set to red  the danger zone
        else:
            #creates a new palette object
            palette = QtGui.QPalette(self.palette())
            #Determines the color that the palette will be, in this case red
            palette.setColor(QtGui.QPalette.Highlight, QtGui.QColor(QtCore.Qt.red))
            #Sets the palette
            self.BatteryProgressBar.setPalette(palette)        

    def update_graph(self):
        usageIdArr,  dateTimeArr, freshWaterArr,  greyWaterArr,  blackWaterArr,  batteryArr = Database.sensorData()
        #Clears the graphs
        self.SensorGraph.canvas.axes.clear()        
        #freshWaterArr, greyWaterArr, blackWaterArr, batteryArr, time = sensorData()
        self.SensorGraph.canvas.axes.set_ylim(0, 100)
        #Plots the graphs
        self.SensorGraph.canvas.axes.plot(dateTimeArr,freshWaterArr)      #(time, freshWaterArr)  #FreshWater
        self.SensorGraph.canvas.axes.plot(dateTimeArr, greyWaterArr)          #(time, greyWaterArr)    #greyWater
        self.SensorGraph.canvas.axes.plot(dateTimeArr,  blackWaterArr)        #(time, blackWaterArr)     #blackWater
        self.SensorGraph.canvas.axes.plot(dateTimeArr, batteryArr)    #(time, batteryArr)    #battery
        #creates the legend
        self.SensorGraph.canvas.axes.legend(('FreshWater', 'GreyWater',  'BlackWater',  'Battery'), loc='right')
        #Angles the x-axis
        self.SensorGraph.canvas.axes.xaxis.set_tick_params(rotation=45)
        #Titles of the graphs
        self.SensorGraph.canvas.axes.set_title('Sensors')
        self.SensorGraph.canvas.axes.set_xlabel('Date')
        self.SensorGraph.canvas.axes.set_ylabel('Percentage')
        #Draws the graphs
        self.SensorGraph.canvas.draw()
        
    @pyqtSlot()
    def on_CheckGraphs_clicked(self):
       self.update_graph()
    
    @pyqtSlot()
    def on_powerApp_clicked(self):
        choice = QMessageBox.question(self,  'Close',  "Do you want to exit the application?",  QMessageBox.No | QMessageBox.Yes)
        if choice == QMessageBox.Yes:
            sys.exit()
        else:
            pass

    @pyqtSlot()
    def on_powerApp_pressed(self):
        choice = QMessageBox.question(self,  'Close',  "Do you want to exit the application?",  QMessageBox.No | QMessageBox.Yes)
        if choice == QMessageBox.Yes:
            sys.exit()
        else:
            pass
            
    @pyqtSlot()
    def on_powerRasberry_clicked(self):
        choice = QMessageBox.question(self,  'Close',  "Do you want to turn off the Raspberry Pi?",  QMessageBox.No | QMessageBox.Yes)
        if choice == QMessageBox.Yes:
            call("sudo shutdown -h now", shell=True)
        else:
            pass

    
    @pyqtSlot()
    def on_powerRasberry_pressed(self):
        choice = QMessageBox.question(self,  'Close',  "Do you want to turn off the Raspberry Pi?",  QMessageBox.No | QMessageBox.Yes)
        if choice == QMessageBox.Yes:
            call("sudo shutdown -h now", shell=True)
        else:
            pass

        
class ThreadClass(QtCore.QThread):
    # Create the signals for sensors
    freshWaterSig = QtCore.pyqtSignal(int)
    greyWaterSig = QtCore.pyqtSignal(int)
    blackWaterSig = QtCore.pyqtSignal(int)
    batterySig = QtCore.pyqtSignal(int)

    #Constructor for the ThreadClass
    def __init__(self, parent=None):
        super(ThreadClass, self).__init__(parent)

    def run(self):
        counterDatabaseInput = 0
        while True:
            #gets Values for sensors
            freshWaterVal =  WaterUsageInfo.getWaterUsage(3.5, 1.9, 0)
            greyWaterVal = WaterUsageInfo.getWaterUsage(3.8, 2.2, 1)
            blackWaterVal = WaterUsageInfo.getWaterUsage(3.7, 1.9, 2)
            batteryVal =  randomNum.getRandNum() #BatteryInfo.getBattery()
            #freshWaterVal,  greyWaterVal,  blackWaterVal,  batteryVal = Database.lastInput(freshWaterVal,  greyWaterVal,  blackWaterVal,  batteryVal)
            # Emits the signal 
            self.freshWaterSig.emit(freshWaterVal)
            self.greyWaterSig.emit(greyWaterVal)
            self.blackWaterSig.emit(blackWaterVal)
            self.batterySig.emit(batteryVal)
            #Inputs the values into the data base.
            print(counterDatabaseInput)
            if (counterDatabaseInput % 1) == 0: #records ever 10 run cycles
                Database.input(freshWaterVal,  greyWaterVal,  blackWaterVal,  batteryVal)
            #increments counter
            counterDatabaseInput = counterDatabaseInput + 1
            #sleeps for 2 seconds
            time.sleep (1)
                
 
    #Flushes the toilet
    def flush(self):
        pass    
