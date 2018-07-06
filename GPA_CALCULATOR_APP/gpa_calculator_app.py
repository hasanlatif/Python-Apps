# -*- coding: utf-8 -*-
# Created by: PyQt5
#Author :Hasan Latif
#Email :hasanlatif.pk@gmail.com
# WARNING! All changes made in this file will be lost!

from  PyQt5.QtCore import  pyqtSlot
from PyQt5.QtWidgets import QApplication, QWidget
from gpa_cal_ui import Ui_MainWindow
from gpa_cal import user_input

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication, QWidget,QMainWindow
import  concurrent.futures
from gpa_cal_ui import Ui_MainWindow

print("[Info] App is runing...")
class CalculatorForm(QMainWindow):
    def __init__(self,parent=None):
        super(CalculatorForm, self).__init__(parent)

        self.ui = Ui_MainWindow()


        self.ui.setupUi(self)


if __name__ == '__main__':
 with concurrent.futures.ProcessPoolExecutor() as executor:
        import sys
		
        app = QApplication(sys.argv)
        calculator = CalculatorForm()
        calculator.show()
        sys.exit(app.exec_())
