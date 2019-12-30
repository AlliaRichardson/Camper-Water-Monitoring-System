# -*- coding: utf-8 -*-

import FreshWaterInfo
import GreyWaterInfo
import BlackWaterInfo
#import BatteryInfo
import Database
import time
import randomNum
from PyQt5 import QtCore,  QtGui
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMainWindow
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
        #Connects to an emitter in the thread class so it can set the fresh water progress bar's value
        self.threadclass.freshWaterSig.connect(self.on_FreshWaterProgressBar_valueChanged)
        #Connects to an emitter in the thread class so it can set the grey water  progress bar's value
        self.threadclass.greyWaterSig.connect(self.on_GreyWaterProgressBar_valueChanged)
       #Connects to an emitter in the thread class so it can set the black water  progress bar's value
        self.threadclass.blackWaterSig.connect(self.on_BlackWaterProgressBar_valueChanged)
       #Connects to an emitter in the thread class so it can set the battery  progress bar's value
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

class ThreadClass(QtCore.QThread):
    # Create the signal for the fresh water thread
    freshWaterSig = QtCore.pyqtSignal(int)
    # Create the signal for the grey water thread
    greyWaterSig = QtCore.pyqtSignal(int)
    # Create the signal for the black water thread
    blackWaterSig = QtCore.pyqtSignal(int)
    #Create the signal for the battery thread
    batterySig = QtCore.pyqtSignal(int)

    #Constructor for the ThreadClass
    def __init__(self, parent=None):
        super(ThreadClass, self).__init__(parent)

    def run(self):
        counterDatabaseInput = 0
        while True:
            #gets the CPU value from the file sysinfo.py
            freshWaterVal = FreshWaterInfo.getFreshWater()
            #gets a random number from randomNum.py
            greyWaterVal = GreyWaterInfo.getGreyWater()
            #gets the CPU value from the file sysinfo.py
            blackWaterVal = BlackWaterInfo.getBlackWater()
            #gets a random number from randomNum.py
            batteryVal =  randomNum.getRandNum() #BatteryInfo.getBattery()
            # Emits the signal of the fresh wter value
            self.freshWaterSig.emit(freshWaterVal)
            # Emits the signal of the grey water value
            self.greyWaterSig.emit(greyWaterVal)
            # Emits the signal of the black water value
            self.blackWaterSig.emit(blackWaterVal)
            # Emits the signal of the battery value
            self.batterySig.emit(batteryVal)
            
            counterDatabaseInput = counterDatabaseInput + 1
            print(counterDatabaseInput)
            if (counterDatabaseInput % 10) == 0:
                Database.input(freshWaterVal,  greyWaterVal,  blackWaterVal,  batteryVal)
            time.sleep (2)
                
 
    #Flushes the toilet
    def flush(self):
        pass    
