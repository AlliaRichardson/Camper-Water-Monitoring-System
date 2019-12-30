'''
 Name:       Allia Richardson
 Project:    Capstone
 Term:       Spring 2019
   Description
        The program that allows all the components of the CamperWaterSystem to
		run together.
'''
import sys
from PyQt5.QtWidgets import QApplication
from UI.mainWindow import MainWindow

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui = MainWindow()
    ui.show()
    sys.exit(app.exec_())
