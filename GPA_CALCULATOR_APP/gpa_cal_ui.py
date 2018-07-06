# -*- coding: utf-8 -*-
# Created by: PyQt5
#Author :Hasan Latif
#Email :hasanlatif.pk@gmail.com
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox,QMainWindow
from PyQt5.QtCore import pyqtSlot
print("[Info] Loading UI modules...")
from  gpa_cal import user_input,assign_gpa_points,gpa_calculation
print("[Info] Loading GPA calculation modules....")


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(700, 590)
        MainWindow.setFixedSize(700,590)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(120, 20, 261, 25))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(130, 90, 141, 25))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(260, 90, 121, 25))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(30, 150, 89, 25))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(30, 190, 89, 25))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(30, 230, 89, 25))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(30, 270, 89, 25))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(30, 310, 89, 25))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(30, 350, 89, 25))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(30, 390, 89, 25))
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(30, 430, 89, 25))
        self.label_11.setObjectName("label_11")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(160, 150, 71, 31))
        self.lineEdit.setObjectName("lineEdit")


        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(160, 190, 71, 31))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(160, 230, 71, 31))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(160, 270, 71, 31))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_5.setGeometry(QtCore.QRect(160, 310, 71, 31))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_6.setGeometry(QtCore.QRect(160, 350, 71, 31))
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.lineEdit_7 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_7.setGeometry(QtCore.QRect(160, 390, 71, 31))
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.lineEdit_8 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_8.setGeometry(QtCore.QRect(160, 430, 71, 31))
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.lineEdit_9 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_9.setGeometry(QtCore.QRect(280, 150, 71, 31))
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.lineEdit_10 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_10.setGeometry(QtCore.QRect(280, 190, 71, 31))
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.lineEdit_11 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_11.setGeometry(QtCore.QRect(280, 230, 71, 31))
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.lineEdit_12 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_12.setGeometry(QtCore.QRect(280, 270, 71, 31))
        self.lineEdit_12.setObjectName("lineEdit_12")
        self.lineEdit_13 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_13.setGeometry(QtCore.QRect(280, 310, 71, 31))
        self.lineEdit_13.setObjectName("lineEdit_13")
        self.lineEdit_14 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_14.setGeometry(QtCore.QRect(280, 350, 71, 31))
        self.lineEdit_14.setObjectName("lineEdit_14")
        self.lineEdit_15 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_15.setGeometry(QtCore.QRect(280, 390, 71, 31))
        self.lineEdit_15.setObjectName("lineEdit_15")
        self.lineEdit_16 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_16.setGeometry(QtCore.QRect(280, 430, 71, 31))
        self.lineEdit_16.setObjectName("lineEdit_16")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(390, 180, 89, 25))
        self.label_12.setObjectName("label_12")
        self.lineEdit_17 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_17.setGeometry(QtCore.QRect(450, 180, 131, 31))
        self.lineEdit_17.setObjectName("lineEdit_17")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(200, 480, 101, 46))
        self.pushButton.setObjectName("pushButton")

        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(400, 270, 141, 31))
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(400, 310, 241, 25))
        self.label_14.setObjectName("label_14")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(500, 340, 131, 46))
        self.pushButton_2.setObjectName("pushButton_2")


        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 38))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")

        MainWindow.setStatusBar(self.statusbar)


        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "CIIT GPA Calculator"))
        self.label.setText(_translate("MainWindow", "COMSATS GPA Caclculator"))
        self.label_2.setText(_translate("MainWindow", "Marks Obt."))
        self.label_3.setText(_translate("MainWindow", "Credit hrs"))
        self.label_4.setText(_translate("MainWindow", "Subject 1"))
        self.label_5.setText(_translate("MainWindow", "Subject 2"))
        self.label_6.setText(_translate("MainWindow", "Subject 3"))
        self.label_7.setText(_translate("MainWindow", "Subject 4"))
        self.label_8.setText(_translate("MainWindow", "Subject 5"))
        self.label_9.setText(_translate("MainWindow", "Subject 6"))
        self.label_10.setText(_translate("MainWindow", "Subject 7"))
        self.label_11.setText(_translate("MainWindow", "Subject 8"))
        self.label_12.setText(_translate("MainWindow", "GPA="))
        self.pushButton.setText(_translate("MainWindow", "Calculate"))
        self.label_13.setText(_translate("MainWindow", "Developed by:"))
        self.label_14.setText(_translate("MainWindow", "hasanlatif.pk@gmail.com"))
        self.pushButton_2.setText(_translate("MainWindow", "More..>>"))
        self.pushButton_2.clicked.connect(self.clickedButton1)
        self.pushButton.clicked.connect(self.clickedButton)

    def clickedButton(self):
         num_credit_hour_array =[]
         subject_num_array=[]
         subject_gpa_array=[]
         subjectNum=int(self.lineEdit.text())
         subjectNum2 = float(self.lineEdit_2.text())
         subjectNum3 = float(self.lineEdit_3.text())
         subjectNum4 =float( self.lineEdit_4.text())
         subjectNum5 = float(self.lineEdit_5.text())
         subjectNum6 = float(self.lineEdit_6.text())
         subjectNum7 = float(self.lineEdit_7.text())
         subjectNum8 = float(self.lineEdit_8.text())
         subjectCredit9 =float(self.lineEdit_9.text())
         subjectCredit10 = float(self.lineEdit_10.text())
         subjectCredit11 = float(self.lineEdit_11.text())
         subjectCredit12 =float(self.lineEdit_12.text())
         subjectCredit13 = float(self.lineEdit_13.text())
         subjectCredit14 =float( self.lineEdit_14.text())
         subjectCredit15 = float(self.lineEdit_15.text())
         subjectCredit16 = float(self.lineEdit_16.text())
         user_input(subjectNum, subjectNum2, subjectNum3, subjectNum4, subjectNum5, subjectNum6,
                    subjectNum7, subjectNum8, subjectCredit9, subjectCredit10, subjectCredit11, subjectCredit12,
                    subjectCredit13, subjectCredit14, subjectCredit15, subjectCredit16, subject_num_array,
                    num_credit_hour_array)

         assign_gpa_points(subject_num_array, subject_gpa_array)
         a=gpa_calculation(subject_gpa_array, num_credit_hour_array)

         a=str(round(a,2))+str("   /4.0")
         self.lineEdit_17.setText(a)
    def clickedButton1(self):
        import os

        os.system("notepad file.txt")

