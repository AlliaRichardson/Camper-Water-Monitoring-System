# -*- coding: utf-8 -*-
#-----------------------------imports-------------------------------------------
import SensorUsageInfo
import Database
import sys
import time
import randomNum
from subprocess import call
#-------------------------------------------------------------------------------
from PyQt5 import QtCore,  QtGui
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMainWindow, QMessageBox
from .Ui_mainWindow import Ui_MainWindow
#-------------------------------------------------------------------------------

#   Class - mainWindow
#
#   Description:
#       This class contains the methods that interacte with the user interfaces,
#       such as the buttons, progress bars, tabs, and graphs.

class MainWindow(QMainWindow, Ui_MainWindow):
    #Constructor for the MainWindow Class
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        self.setupUi(self)
        #Creates an object of threadclass
        self.threadclass = ThreadClass()
        #starts a thread
        self.threadclass.start()
        #Connects to the emitters in the thread class updates progress bars
        self.threadclass.freshWaterSig.connect(self.on_FreshWaterProgressBar_valueChanged)
        self.threadclass.greyWaterSig.connect(self.on_GreyWaterProgressBar_valueChanged)
        self.threadclass.blackWaterSig.connect(self.on_BlackWaterProgressBar_valueChanged)
        self.threadclass.batterySig.connect(self.on_BatteryProgressBar_valueChanged)
       
#-------------------------------------------------------------------------------
    #   Method - on_FreshWaterProgressBar_valueChanged
    #
    #    Description:
    #        The method sets the value of the progress bar and the color.
    #    Parameter:
    #        int value - The value the progress bar will be set too.
    #    Return:
    #        Not applicable
    @pyqtSlot(int)
    def on_FreshWaterProgressBar_valueChanged(self, value):
        #Sets the value that will will be shown in the progress bar
        self.FreshWaterProgressBar.setProperty("value", value)
        #If the value is greater than or equal to 50% the progress bar is green
        if value >= 50:
            #creates a new palette object
            palette = QtGui.QPalette(self.palette())
            #Determines the color that the palette will be, in this case green
            palette.setColor(QtGui.QPalette.Highlight, 
                QtGui.QColor(QtCore.Qt.green))
            #Sets the palette
            self.FreshWaterProgressBar.setPalette(palette)
        #If the value is greater than or equal to 20% the progress bar is green    
        elif value >= 20:
            #creates a new palette object
            palette = QtGui.QPalette(self.palette())
            #Determines the color that the palette will be, in this case orange
            palette.setColor(QtGui.QPalette.Highlight, 
                QtGui.QColor(255, 165, 0))
            #Sets the palette
            self.FreshWaterProgressBar.setPalette(palette)
        #Else the progress bar is set to red  the danger zone
        else:
            #creates a new palette object
            palette = QtGui.QPalette(self.palette())
            #Determines the color that the palette will be, in this case red
            palette.setColor(QtGui.QPalette.Highlight, 
                QtGui.QColor(QtCore.Qt.red))
            #Sets the palette
            self.FreshWaterProgressBar.setPalette(palette)    

#------------------------------------------------------------------------------- 
    #   Method - on_BlackWaterProgressBar_valueChanged
    #
    #    Description:
    #        The method sets the value of the progress bar and the color.
    #    Parameter:
    #        int value - The value the progress bar will be set too.
    #    Return:
    #        Not applicable 
    @pyqtSlot(int)
    def on_BlackWaterProgressBar_valueChanged(self, value):
        #Sets the value that will will be shown in the progress bar
        self.BlackWaterProgressBar.setProperty("value", value)
        #If the value is less than or equal to 50% the progress bar is green
        if value < 10:
            #creates a new palette object
            palette = QtGui.QPalette(self.palette())
            #Determines the color that the palette will be, in this case green
            palette.setColor(QtGui.QPalette.Highlight, 
                QtGui.QColor(QtCore.Qt.green))
            #Sets the palette
            self.BlackWaterProgressBar.setPalette(palette)
        #If the value is less than or equal to 80% the progress bar is green  
        elif value <= 50:
            #creates a new palette object
            palette = QtGui.QPalette(self.palette())
            #Determines the color that the palette will be, in this case orange
            palette.setColor(QtGui.QPalette.Highlight, 
                QtGui.QColor(255, 165, 0))
            #Sets the palette
            self.BlackWaterProgressBar.setPalette(palette)
        #Else the progress bar is set to red  the danger zone
        else:
            #creates a new palette object
            palette = QtGui.QPalette(self.palette())
            #Determines the color that the palette will be, in this case red
            palette.setColor(QtGui.QPalette.Highlight, 
                QtGui.QColor(QtCore.Qt.red))
            #Sets the palette
            self.BlackWaterProgressBar.setPalette(palette)  
 
#------------------------------------------------------------------------------- 
    #   Method - on_GreyWaterProgressBar_valueChanged
    #
    #    Description:
    #        The method sets the value of the progress bar and the color.
    #    Parameter:
    #        int value - The value the progress bar will be set too.
    #    Return:
    #        Not applicable 
    @pyqtSlot(int)
    def on_GreyWaterProgressBar_valueChanged(self, value):
        #Sets the value that will will be shown in the progress bar
        self.GreyWaterProgressBar.setProperty("value", value)
        #If the value is less than or equal to 50% the progress bar is green
        if value < 10:
            #creates a new palette object
            palette = QtGui.QPalette(self.palette())
            #Determines the color that the palette will be, in this case green
            palette.setColor(QtGui.QPalette.Highlight, 
                QtGui.QColor(QtCore.Qt.green))
            #Sets the palette
            self.GreyWaterProgressBar.setPalette(palette)
        #If the value is less than or equal to 80% the progress bar is green  
        elif value <= 50:
            #creates a new palette object
            palette = QtGui.QPalette(self.palette())
            #Determines the color that the palette will be, in this case orange
            palette.setColor(QtGui.QPalette.Highlight, 
                QtGui.QColor(255, 165, 0))
            #Sets the palette
            self.GreyWaterProgressBar.setPalette(palette)
        #Else the progress bar is set to red  the danger zone
        else:
            #creates a new palette object
            palette = QtGui.QPalette(self.palette())
            #Determines the color that the palette will be, in this case red
            palette.setColor(QtGui.QPalette.Highlight, 
                QtGui.QColor(QtCore.Qt.red))
            #Sets the palette
            self.GreyWaterProgressBar.setPalette(palette)  
    
#-------------------------------------------------------------------------------
    #   Method - on_BatteryProgressBar_valueChanged
    #
    #    Description:
    #        The method sets the value of the progress bar and the color.
    #    Parameter:
    #        int value - The value the progress bar will be set too.
    #    Return:
    #        Not applicable  
    @pyqtSlot(int)
    def on_BatteryProgressBar_valueChanged(self, value):
        #Sets the value that will will be shown in the progress bar
        self.BatteryProgressBar.setProperty("value", value)
        #If the value is greater than or equal to 50% the progress bar is green
        if value >= 80:
            #creates a new palette object
            palette = QtGui.QPalette(self.palette())
            #Determines the color that the palette will be, in this case green
            palette.setColor(QtGui.QPalette.Highlight, 
                QtGui.QColor(QtCore.Qt.green))
            #Sets the palette
            self.BatteryProgressBar.setPalette(palette)
        #If the value is greater than or equal to 20% the progress bar is green    
        elif value >= 60:
            #creates a new palette object
            palette = QtGui.QPalette(self.palette())
            #Determines the color that the palette will be, in this case orange
            palette.setColor(QtGui.QPalette.Highlight, 
                QtGui.QColor(255, 165, 0))
            #Sets the palette
            self.BatteryProgressBar.setPalette(palette)
        #Else the progress bar is set to red  the danger zone
        else:
            #creates a new palette object
            palette = QtGui.QPalette(self.palette())
            #Determines the color that the palette will be, in this case red
            palette.setColor(QtGui.QPalette.Highlight, 
                QtGui.QColor(QtCore.Qt.red))
            #Sets the palette
            self.BatteryProgressBar.setPalette(palette)        

#-------------------------------------------------------------------------------
    #   Method - update_graph
    #
    #    Description:
    #       The method plots the fresh water, grey water, black water and 
    #       battery usage over time. It plots a total of 100 records.
    #    Parameter:
    #       Not Applicable
    #    Return:
    #        Not applicable  
    def update_graph(self):
        usageIdArr, dateTimeArr, freshWaterArr, greyWaterArr, blackWaterArr,  \
            batteryArr = Database.sensorData()
        #Clears the graphs
        self.SensorGraph.canvas.axes.clear()        
        #Sets y-axix limits 0 to 100%
        self.SensorGraph.canvas.axes.set_ylim(0, 100)
        #Plots the graphs
        self.SensorGraph.canvas.axes.plot(dateTimeArr,freshWaterArr)  
        self.SensorGraph.canvas.axes.plot(dateTimeArr, greyWaterArr) 
        self.SensorGraph.canvas.axes.plot(dateTimeArr,  blackWaterArr) 
        self.SensorGraph.canvas.axes.plot(dateTimeArr, batteryArr)  
        #creates the legend
        self.SensorGraph.canvas.axes.legend(('FreshWater', 'GreyWater',  
            'BlackWater',  'Battery'), loc='center left', 
            bbox_to_anchor=(1, 0.5))
        #Angles the x-axis
        self.SensorGraph.canvas.axes.xaxis.set_tick_params(rotation=45)
        #Titles of the graphs
        self.SensorGraph.canvas.axes.set_title('Sensors')
        self.SensorGraph.canvas.axes.set_xlabel('Date and Time')
        self.SensorGraph.canvas.axes.set_ylabel('Percentage')
        #Auto adjusts figure
        self.SensorGraph.canvas.axes.figure.tight_layout()
        #Draws the graphs
        self.SensorGraph.canvas.draw()

#-------------------------------------------------------------------------------
    #   Method - on_CheckGraphs_clicked
    #
    #    Description:
    #       When the refresh button is clicked in the graph tab it  calls 
    #       the update_graph method
    #    Parameter:
    #       Not Applicable
    #    Return:
    #        Not applicable          
    @pyqtSlot()
    def on_CheckGraphs_clicked(self):
       self.update_graph()

#-------------------------------------------------------------------------------
    #   Method - on_powerApp_clicked
    #
    #    Description:
    #       Turns off the the application when the button is clicked. Pops-up
    #       a message asking if they are sure if yes exits program.
    #    Parameter:
    #       Not Applicable
    #    Return:
    #        Not applicable         
    @pyqtSlot()
    def on_powerApp_clicked(self):
        choice = QMessageBox.question(self,  'Close',  
            "Do you want to exit the application?",  
            QMessageBox.No | QMessageBox.Yes)
        if choice == QMessageBox.Yes:
            sys.exit()
        else:
            pass

#-------------------------------------------------------------------------------
    #   Method - on_powerRasberry_clicked
    #
    #    Description:
    #       Turns off the raspberry pi when the button is clicked. Pops-up
    #       a message asking if they are sure if yes exits program.
    #    Parameter:
    #       Not Applicable
    #    Return:
    #        Not applicable                    
    @pyqtSlot()
    def on_powerRasberry_clicked(self):
        choice = QMessageBox.question(self,  'Close',  
            "Do you want to turn off the Raspberry Pi?",  
            QMessageBox.No | QMessageBox.Yes)
        if choice == QMessageBox.Yes:
            call("sudo shutdown -h now", shell=True)
        else:
            pass

#-------------------------------------------------------------------------------
#   Class - ThreadClass
#
#   Description:
#       Has four signal variables for fresh water, grey water, black water, 
#       and battery.  It then emits the signals to the mainWindow class.
class ThreadClass(QtCore.QThread):
    # Create the signals for sensors
    freshWaterSig = QtCore.pyqtSignal(int)
    greyWaterSig = QtCore.pyqtSignal(int)
    blackWaterSig = QtCore.pyqtSignal(int)
    batterySig = QtCore.pyqtSignal(int)

    #Constructor for the ThreadClass
    def __init__(self, parent=None):
        super(ThreadClass, self).__init__(parent)

#-------------------------------------------------------------------------------
    #   Method - run
    #
    #    Description:
    #       Gets the four values that will be emit to the mainWindow class.
    #       Every 10 cycles it records the values into the database. 
    #       It emits every value back to the mainWindowClass.
    #    Parameter:
    #       Not Applicable
    #    Return:
    #        Not applicable     
    def run(self):
        #counter for the run method
        counterDatabaseInput = 0
        
        #while true, obtain the values, store the values, and emit the values
        while True:
            #gets Values for sensors
            freshWaterVal =  SensorUsageInfo.getWaterUsage(-3.55, 1.9, 0)
            greyWaterVal = SensorUsageInfo.getWaterUsage(-3.74, 2.2, 1)
            blackWaterVal = SensorUsageInfo.getWaterUsage(-3.43, 1.9, 2)
            batteryVal = SensorUsageInfo.getWaterUsage(0, 5, 7)
#            freshWaterVal,  greyWaterVal,  blackWaterVal,  batteryVal = \
#                Database.lastInput(freshWaterVal,  greyWaterVal,  blackWaterVal,  
#                batteryVal)
            # Emits the signal 
            self.freshWaterSig.emit(freshWaterVal)
            self.greyWaterSig.emit(greyWaterVal)
            self.blackWaterSig.emit(blackWaterVal)
            self.batterySig.emit(batteryVal)
            #Inputs the values into the data base.
            if (counterDatabaseInput % 1) == 0: #records ever 10 run cycles
                Database.input(freshWaterVal,  greyWaterVal,  blackWaterVal,  
                batteryVal)
            #increments counter
            counterDatabaseInput = counterDatabaseInput + 1
            #sleeps for 2 seconds
            time.sleep (1)
                
#------------------------------------------------------------------------------- 
    #Flushes everything but the kitchen sink
    def flush(self):
        pass    
