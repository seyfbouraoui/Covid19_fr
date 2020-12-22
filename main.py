__author__ = 'Escargot'
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Coronavirus.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QDesktopWidget
import numpy
import pyttsx3
from datetime import datetime

class Ui_MainWindow(object):

    def Seyfallah(self):
        # print("Mamicha")
        # print(self.age.currentText())
        # print(self.val11)
        self.Stress = 0.80
        # Temps = 14./24
        vag = int(self.age.currentText())
        #self.vvage = vag
        if vag < 31:
            vag = (vag * numpy.sin(numpy.pi / 3)) / 30  # pi/3 = 60 degree
        else:
            if vag < 45:
                vag = (vag * numpy.sin(numpy.pi / 2)) / (vag + 0.02)  # pi/2 = 90 degree
            else:
                vag = (44 * numpy.sin(numpy.pi / 4)) / vag  # pi/3 = 60 degree
        # vag = (1-vag) * 0.1
        # vag = vag * 0.1
        print(vag)
        self.vvage = vag
        self.calcul = 0
        if self.checkBox.isChecked():
            self.calcul = self.calcul + self.val11 * .33
        else:
            if self.checkBox_2.isChecked():
                self.calcul = self.calcul + self.val12 * .33
            else:
                if self.checkBox_3.isChecked():
                    self.calcul = self.calcul + self.val13 * .33
                else:
                    if self.checkBox_4.isChecked():
                        self.calcul = self.calcul + self.val14 * .33
                    else:
                        if self.checkBox_5.isChecked():
                            self.calcul = self.calcul + self.val15 * .33
            ######
        if self.checkBox_9.isChecked():
            self.calcul = self.calcul + self.val21 * 0.05
        else:
            if self.checkBox_8.isChecked():
                self.calcul = self.calcul + self.val22 * 0.05
            else:
                if self.checkBox_6.isChecked():
                    self.calcul = self.calcul + self.val23 * 0.05
                else:
                    if self.checkBox_10.isChecked():
                        self.calcul = self.calcul + self.val24 * 0.05
                    else:
                        if self.checkBox_7.isChecked():
                            self.calcul = self.calcul + self.val25 * 0.05

        ######
        if self.checkBox_14.isChecked():
            self.calcul = self.calcul + self.val31 * 0.15
        else:
            if self.checkBox_13.isChecked():
                self.calcul = self.calcul + self.val32 * 0.15
            else:
                if self.checkBox_11.isChecked():
                    self.calcul = self.calcul + self.val33 * 0.15
                else:
                    if self.checkBox_15.isChecked():
                        self.calcul = self.calcul + self.val34 * 0.15
                    else:
                        if self.checkBox_12.isChecked():
                            self.calcul = self.calcul + self.val35 * 0.15
        ######
        if self.checkBox_19.isChecked():
            self.calcul = self.calcul + self.val41 * 0.09
        else:
            if self.checkBox_18.isChecked():
                self.calcul = self.calcul + self.val42 * 0.09
            else:
                if self.checkBox_16.isChecked():
                    self.calcul = self.calcul + self.val43 * 0.09
                else:
                    if self.checkBox_20.isChecked():
                        self.calcul = self.calcul + self.val44 * 0.09
                    else:
                        if self.checkBox_17.isChecked():
                            self.calcul = self.calcul + self.val45 * 0.09

        ######
        if self.checkBox_24.isChecked():
            self.calcul = self.calcul + self.val51 * 0.2
        else:
            if self.checkBox_23.isChecked():
                self.calcul = self.calcul + self.val52 * 0.2
            else:
                if self.checkBox_21.isChecked():
                    self.calcul = self.calcul + self.val53 * 0.2
                else:
                    if self.checkBox_25.isChecked():
                        self.calcul = self.calcul + self.val54 * 0.2
                    else:
                        if self.checkBox_22.isChecked():
                            self.calcul = self.calcul + self.val55 * 0.2

        ######
        if self.checkBox_29.isChecked():
            self.calcul = self.calcul + self.val61 * 0.23
        else:
            if self.checkBox_28.isChecked():
                self.calcul = self.calcul + self.val62 * 0.23
            else:
                if self.checkBox_26.isChecked():
                    self.calcul = self.calcul + self.val63 * 0.23
                else:
                    if self.checkBox_30.isChecked():
                        self.calcul = self.calcul + self.val64 * 0.23
                    else:
                        if self.checkBox_27.isChecked():
                            self.calcul = self.calcul + self.val65 * 0.23

        ######
        if self.checkBox_34.isChecked():
            self.calcul = self.calcul + self.val71 * 0.47
        else:
            if self.checkBox_33.isChecked():
                self.calcul = self.calcul + self.val72 * 0.47
            else:
                if self.checkBox_31.isChecked():
                    self.calcul = self.calcul + self.val73 * 0.47
                else:
                    if self.checkBox_35.isChecked():
                        self.calcul = self.calcul + self.val74 * 0.47
                    else:
                        if self.checkBox_32.isChecked():
                            self.calcul = self.calcul + self.val75 * 0.47

        ######
        if self.checkBox_39.isChecked():
            self.calcul = self.calcul + self.val81 * 0.13
        else:
            if self.checkBox_38.isChecked():
                self.calcul = self.calcul + self.val82 * 0.13
            else:
                if self.checkBox_36.isChecked():
                    self.calcul = self.calcul + self.val83 * 0.13
                else:
                    if self.checkBox_40.isChecked():
                        self.calcul = self.calcul + self.val84 * 0.13
                    else:
                        if self.checkBox_37.isChecked():
                            self.calcul = self.calcul + self.val85 * 0.13

        ######
        if self.checkBox_44.isChecked():
            self.calcul = self.calcul + self.val91 * 0.19
        else:
            if self.checkBox_43.isChecked():
                self.calcul = self.calcul + self.val92 * 0.19
            else:
                if self.checkBox_41.isChecked():
                    self.calcul = self.calcul + self.val93 * 0.19
                else:
                    if self.checkBox_45.isChecked():
                        self.calcul = self.calcul + self.val94 * 0.19
                    else:
                        if self.checkBox_42.isChecked():
                            self.calcul = self.calcul + self.val95 * 0.19

        ######
        if self.checkBox_49.isChecked():
            self.calcul = self.calcul + self.val101 * 0.39
        else:
            if self.checkBox_48.isChecked():
                self.calcul = self.calcul + self.val102 * 0.39
            else:
                if self.checkBox_46.isChecked():
                    self.calcul = self.calcul + self.val103 * 0.39
                else:
                    if self.checkBox_50.isChecked():
                        self.calcul = self.calcul + self.val104 * 0.39
                    else:
                        if self.checkBox_47.isChecked():
                            self.calcul = self.calcul + self.val105 * 0.39

        self.calcul = (((self.calcul * 100) / 230)) * 100 + (self.Stress * vag)
        self.lettre = ""
        if self.calcul < 20:
            print("Vous êtes en bonne santé")
            self.lettre ="Vous êtes en bonne santé"
        else:
            if ((self.calcul < 33) and (self.vvage < 40)):
                print("Vous avez un rhume, rassurez-vous et ne vous inquiétez pas.")
                self.lettre = "Vous avez un rhume, rassurez-vous et ne vous inquiétez pas."
            else:
                if ((self.calcul < 33) and (self.vvage > 40)):
                    print("Vous avez un rhume. faites du sport et lavez votre main")
                    self.lettre = "Vous avez un rhume. faites du sport et lavez votre main"
                else:
                    # if ((self.calcul > 33) and (self.vvage < 40)) :
                    #    print("Vous avez un rhume, Attention a votre sante.")
                    # else:
                    # if ((self.calcul > 33) and (self.vvag > 40)) :
                    #    print("Vous avez un rhume,Vous devriez suivre les conseilles du ministere de la sante.")
                    # else:
                    if ((self.calcul < 55) and (self.vvage < 40)):
                        print("Vous devriez suivre les conseilles du ministere de la santé...lavez-vous les mains...")
                        self.lettre = "Vous devriez suivre les conseilles du ministere de la santé...lavez-vous les mains..."
                    else:
                        if ((self.calcul < 55) and (self.vvage > 40)):
                            print("Vous devriez suivre les conseilles du ministere de la santé....vous n'êtes pas en  très bonne santé ")
                            self.lettre = "Vous devriez suivre les conseilles du ministere de la santé....vous n'êtes pas en  très bonne santé "
                        else:
                            if ((self.calcul < 66) and (self.vvage < 40)):
                                print("Vous devriez suivre les conseilles du ministere de la santé....vous n'êtes pas en  très bonne santé")
                                self.lettre = "Vous devriez suivre les conseilles du ministere de la sante....vous n'êtes pas en  très bonne santé"
                            else:
                                print("Evacuation immidiate")
                                self.lettre = "Evacuation immidiate"
        print("%.6f" % self.calcul)


    def c11(self, state):
        if (QtCore.Qt.Checked == state):
            # self.label_2.setText("Selected.")
            self.val11 = float(0. / 5)
        else:
            # self.label_2.setText("Not Selected.")
            self.val11 = 0
        # print(self.val1)

    def c12(self, state):
        if (QtCore.Qt.Checked == state):
            # self.label_2.setText("Selected.")
            self.val12 = float(2. / 5)

        else:
            # self.label_2.setText("Not Selected.")
            self.val12 = 0

    def c13(self, state):
        if (QtCore.Qt.Checked == state):
            # self.label_2.setText("Selected.")
            self.val13 = float(3. / 5)
        else:
            # self.label_2.setText("Not Selected.")
            self.val13 = 0

    def c14(self, state):
        if (QtCore.Qt.Checked == state):
            # self.label_2.setText("Selected.")
            self.val14 = float(4. / 5)
        else:
            # self.label_2.setText("Not Selected.")
            self.val14 = 0

    def c15(self, state):
        if (QtCore.Qt.Checked == state):
            # self.label_2.setText("Selected.")
            self.val15 = float(5. / 5)
        else:
            # self.label_2.setText("Not Selected.")
            self.val15 = 0

    ##############################################################
    def c21(self, state):
        if (QtCore.Qt.Checked == state):
            # self.label_2.setText("Selected.")
            self.val21 = float(5. / 5)
        else:
            # self.label_2.setText("Not Selected.")
            self.val21 = 0
        # print(self.val1)

    def c22(self, state):
        if (QtCore.Qt.Checked == state):
            # self.label_2.setText("Selected.")
            self.val22 = float(4. / 5)
        else:
            # self.label_2.setText("Not Selected.")
            self.val22 = 0

    def c23(self, state):
        if (QtCore.Qt.Checked == state):
            # self.label_2.setText("Selected.")
            self.val23 = float(3. / 5)
        else:
            # self.label_2.setText("Not Selected.")
            self.val23 = 0

    def c24(self, state):
        if (QtCore.Qt.Checked == state):
            # self.label_2.setText("Selected.")
            self.val24 = float(2. / 5)
        else:
            # self.label_2.setText("Not Selected.")
            self.val24 = 0

    def c25(self, state):
        if (QtCore.Qt.Checked == state):
            # self.label_2.setText("Selected.")
            self.val25 = float(1. / 5)
        else:
            # self.label_2.setText("Not Selected.")
            self.val25 = 0

    ##############################################################
    def c31(self, state):
        if (QtCore.Qt.Checked == state):
            # self.label_2.setText("Selected.")
            self.val31 = float(5. / 5)
        else:
            # self.label_2.setText("Not Selected.")
            self.val31 = 0
        # print(self.val1)

    def c32(self, state):
        if (QtCore.Qt.Checked == state):
            # self.label_2.setText("Selected.")
            self.val32 = float(4. / 5)
        else:
            # self.label_2.setText("Not Selected.")
            self.val32 = 0

    def c33(self, state):
        if (QtCore.Qt.Checked == state):
            # self.label_2.setText("Selected.")
            self.val33 = float(3. / 5)
        else:
            # self.label_2.setText("Not Selected.")
            self.val33 = 0

    def c34(self, state):
        if (QtCore.Qt.Checked == state):
            # self.label_2.setText("Selected.")
            self.val34 = float(2. / 5)
        else:
            # self.label_2.setText("Not Selected.")
            self.val34 = 0

    def c35(self, state):
        if (QtCore.Qt.Checked == state):
            # self.label_2.setText("Selected.")
            self.val35 = float(1. / 5)
        else:
            # self.label_2.setText("Not Selected.")
            self.val35 = 0

    ##############################################################
    def c41(self, state):
        if (QtCore.Qt.Checked == state):
            # self.label_2.setText("Selected.")
            self.val41 = float(0. / 5)
        else:
            # self.label_2.setText("Not Selected.")
            self.val41 = 0
        # print(self.val1)

    def c42(self, state):
        if (QtCore.Qt.Checked == state):
            # self.label_2.setText("Selected.")
            self.val42 = float(2. / 5)
        else:
            # self.label_2.setText("Not Selected.")
            self.val42 = 0

    def c43(self, state):
        if (QtCore.Qt.Checked == state):
            # self.label_2.setText("Selected.")
            self.val43 = float(3. / 5)
        else:
            # self.label_2.setText("Not Selected.")
            self.val43 = 0

    def c44(self, state):
        if (QtCore.Qt.Checked == state):
            # self.label_2.setText("Selected.")
            self.val44 = float(4. / 5)
        else:
            # self.label_2.setText("Not Selected.")
            self.val44 = 0

    def c45(self, state):
        if (QtCore.Qt.Checked == state):
            # self.label_2.setText("Selected.")
            self.val45 = float(5. / 5)
        else:
            # self.label_2.setText("Not Selected.")
            self.val45 = 0

    ##############################################################
    def c51(self, state):
        if (QtCore.Qt.Checked == state):
            # self.label_2.setText("Selected.")
            self.val51 = float(0. / 5)
        else:
            # self.label_2.setText("Not Selected.")
            self.val51 = 0
        # print(self.val1)

    def c52(self, state):
        if (QtCore.Qt.Checked == state):
            # self.label_2.setText("Selected.")
            self.val52 = float(2. / 5)
        else:
            # self.label_2.setText("Not Selected.")
            self.val52 = 0

    def c53(self, state):
        if (QtCore.Qt.Checked == state):
            # self.label_2.setText("Selected.")
            self.val53 = float(3. / 5)
        else:
            # self.label_2.setText("Not Selected.")
            self.val53 = 0

    def c54(self, state):
        if (QtCore.Qt.Checked == state):
            # self.label_2.setText("Selected.")
            self.val54 = float(4. / 5)
        else:
            # self.label_2.setText("Not Selected.")
            self.val54 = 0

    def c55(self, state):
        if (QtCore.Qt.Checked == state):
            # self.label_2.setText("Selected.")
            self.val55 = float(5. / 5)
        else:
            # self.label_2.setText("Not Selected.")
            self.val55 = 0

    ##############################################################
    def c61(self, state):
        if (QtCore.Qt.Checked == state):
            # self.label_2.setText("Selected.")
            self.val61 = float(0. / 5)
        else:
            # self.label_2.setText("Not Selected.")
            self.val61 = 0
        # print(self.val1)

    def c62(self, state):
        if (QtCore.Qt.Checked == state):
            # self.label_2.setText("Selected.")
            self.val62 = float(2. / 5)
        else:
            # self.label_2.setText("Not Selected.")
            self.val62 = 0

    def c63(self, state):
        if (QtCore.Qt.Checked == state):
            # self.label_2.setText("Selected.")
            self.val63 = float(3. / 5)
        else:
            # self.label_2.setText("Not Selected.")
            self.val63 = 0

    def c64(self, state):
        if (QtCore.Qt.Checked == state):
            # self.label_2.setText("Selected.")
            self.val64 = float(4. / 5)
        else:
            # self.label_2.setText("Not Selected.")
            self.val64 = 0

    def c65(self, state):
        if (QtCore.Qt.Checked == state):
            # self.label_2.setText("Selected.")
            self.val65 = float(5. / 5)
        else:
            # self.label_2.setText("Not Selected.")
            self.val65 = 0

    ##############################################################
    def c71(self, state):
        if (QtCore.Qt.Checked == state):
            # self.label_2.setText("Selected.")
            self.val71 = float(0. / 5)
        else:
            # self.label_2.setText("Not Selected.")
            self.val71 = 0
        # print(self.val1)

    def c72(self, state):
        if (QtCore.Qt.Checked == state):
            # self.label_2.setText("Selected.")
            self.val72 = float(2. / 5)
        else:
            # self.label_2.setText("Not Selected.")
            self.val72 = 0

    def c73(self, state):
        if (QtCore.Qt.Checked == state):
            # self.label_2.setText("Selected.")
            self.val73 = float(3. / 5)
        else:
            # self.label_2.setText("Not Selected.")
            self.val73 = 0

    def c74(self, state):
        if (QtCore.Qt.Checked == state):
            # self.label_2.setText("Selected.")
            self.val74 = float(4. / 5)
        else:
            # self.label_2.setText("Not Selected.")
            self.val74 = 0

    def c75(self, state):
        if (QtCore.Qt.Checked == state):
            # self.label_2.setText("Selected.")
            self.val75 = float(5. / 5)
        else:
            # self.label_2.setText("Not Selected.")
            self.val75 = 0

    ##############################################################
    def c81(self, state):
        if (QtCore.Qt.Checked == state):
            # self.label_2.setText("Selected.")
            self.val81 = float(0. / 5)
        else:
            # self.label_2.setText("Not Selected.")
            self.val81 = 0
        # print(self.val1)

    def c82(self, state):
        if (QtCore.Qt.Checked == state):
            # self.label_2.setText("Selected.")
            self.val82 = float(2. / 5)
        else:
            # self.label_2.setText("Not Selected.")
            self.val82 = 0

    def c83(self, state):
        if (QtCore.Qt.Checked == state):
            # self.label_2.setText("Selected.")
            self.val83 = float(3. / 5)
        else:
            # self.label_2.setText("Not Selected.")
            self.val83 = 0

    def c84(self, state):
        if (QtCore.Qt.Checked == state):
            # self.label_2.setText("Selected.")
            self.val84 = float(4. / 5)
        else:
            # self.label_2.setText("Not Selected.")
            self.val84 = 0

    def c85(self, state):
        if (QtCore.Qt.Checked == state):
            # self.label_2.setText("Selected.")
            self.val85 = float(5. / 5)
        else:
            # self.label_2.setText("Not Selected.")
            self.val85 = 0

    ##############################################################
    def c91(self, state):
        if (QtCore.Qt.Checked == state):
            # self.label_2.setText("Selected.")
            self.val91 = float(0. / 5)
        else:
            # self.label_2.setText("Not Selected.")
            self.val91 = 0
        # print(self.val1)

    def c92(self, state):
        if (QtCore.Qt.Checked == state):
            # self.label_2.setText("Selected.")
            self.val92 = float(2. / 5)
        else:
            # self.label_2.setText("Not Selected.")
            self.val92 = 0

    def c93(self, state):
        if (QtCore.Qt.Checked == state):
            # self.label_2.setText("Selected.")
            self.val93 = float(3. / 5)
        else:
            # self.label_2.setText("Not Selected.")
            self.val93 = 0

    def c94(self, state):
        if (QtCore.Qt.Checked == state):
            # self.label_2.setText("Selected.")
            self.val94 = float(4. / 5)
        else:
            # self.label_2.setText("Not Selected.")
            self.val94 = 0

    def c95(self, state):
        if (QtCore.Qt.Checked == state):
            # self.label_2.setText("Selected.")
            self.val95 = float(5. / 5)
        else:
            # self.label_2.setText("Not Selected.")
            self.val95 = 0

    ##############################################################
    def c101(self, state):
        if (QtCore.Qt.Checked == state):
            # self.label_2.setText("Selected.")
            self.val101 = float(0. / 5)
        else:
            # self.label_2.setText("Not Selected.")
            self.val101 = 0
        # print(self.val1)

    def c102(self, state):
        if (QtCore.Qt.Checked == state):
            # self.label_2.setText("Selected.")
            self.val102 = float(2. / 5)
        else:
            # self.label_2.setText("Not Selected.")
            self.val102 = 0

    def c103(self, state):
        if (QtCore.Qt.Checked == state):
            # self.label_2.setText("Selected.")
            self.val103 = float(3. / 5)
        else:
            # self.label_2.setText("Not Selected.")
            self.val103 = 0

    def c104(self, state):
        if (QtCore.Qt.Checked == state):
            # self.label_2.setText("Selected.")
            self.val104 = float(4. / 5)
        else:
            # self.label_2.setText("Not Selected.")
            self.val104 = 0

    def c105(self, state):
        if (QtCore.Qt.Checked == state):
            # self.label_2.setText("Selected.")
            self.val105 = float(5. / 5)
        else:
            # self.label_2.setText("Not Selected.")
            self.val105 = 0

    ##############################################################

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        font = QtGui.QFont()
        font.setItalic(True)
        MainWindow.setFont(font)
        MainWindow.setAutoFillBackground(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        #MainWindow.setCentralWidget(self.centralwidget)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 10, 737, 73))
        font = QtGui.QFont()
        font.setPointSize(48)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(0, 90, 281, 21))
        font = QtGui.QFont()
        font.setPointSize(13)
        # calcul
        self.calcul = 0
        self.initself()
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(320, 90, 53, 25))
        self.comboBox.setObjectName("comboBox")
        self.age = self.comboBox
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(0, 120, 291, 21))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(0, 140, 281, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(0, 200, 321, 21))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(0, 240, 301, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(0, 290, 231, 21))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(0, 330, 271, 21))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(0, 370, 371, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(0, 400, 301, 21))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(0, 440, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(0, 470, 251, 17))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(290, 500, 131, 41))
        self.pushButton.clicked.connect(self.Seyfallah)
        #j ai ajouter ici
        self.pushButton.clicked.connect(self.parler_covid)
        self.pushButton.clicked.connect(self.info_covid)

        font = QtGui.QFont()
        font.setPointSize(20)
        font.setItalic(True)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.dateEdit = QtWidgets.QDateEdit(self.centralwidget)
        self.dateEdit.setGeometry(QtCore.QRect(450, 90, 111, 26))
        self.dateEdit.setObjectName("dateEdit")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(0, 110, 691, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(0, 140, 321, 16))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(-10, 170, 321, 16))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.line_4 = QtWidgets.QFrame(self.centralwidget)
        self.line_4.setGeometry(QtCore.QRect(0, 220, 321, 16))
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.line_5 = QtWidgets.QFrame(self.centralwidget)
        self.line_5.setGeometry(QtCore.QRect(0, 270, 321, 16))
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.line_6 = QtWidgets.QFrame(self.centralwidget)
        self.line_6.setGeometry(QtCore.QRect(0, 320, 321, 16))
        self.line_6.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.line_7 = QtWidgets.QFrame(self.centralwidget)
        self.line_7.setGeometry(QtCore.QRect(0, 360, 321, 16))
        self.line_7.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.line_8 = QtWidgets.QFrame(self.centralwidget)
        self.line_8.setGeometry(QtCore.QRect(0, 390, 321, 16))
        self.line_8.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_8.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_8.setObjectName("line_8")
        self.line_9 = QtWidgets.QFrame(self.centralwidget)
        self.line_9.setGeometry(QtCore.QRect(-10, 420, 321, 16))
        self.line_9.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_9.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_9.setObjectName("line_9")
        self.line_10 = QtWidgets.QFrame(self.centralwidget)
        self.line_10.setGeometry(QtCore.QRect(0, 460, 321, 16))
        self.line_10.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_10.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_10.setObjectName("line_10")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(320, 120, 377, 25))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.checkBox = QtWidgets.QCheckBox(self.layoutWidget)
        self.checkBox.setObjectName("checkBox")
        # if self.checkBox.isChecked():
        # self.val1 = 1
        # else:
        # self.val1 = 3
        # self.checkBox.toggled.connect(self.Seyfallah)#mamicha

        self.buttonGroup = QtWidgets.QButtonGroup(MainWindow)
        self.buttonGroup.setObjectName("buttonGroup")
        self.buttonGroup.addButton(self.checkBox)
        self.horizontalLayout.addWidget(self.checkBox)
        self.checkBox_2 = QtWidgets.QCheckBox(self.layoutWidget)
        self.checkBox_2.setObjectName("checkBox_2")
        self.buttonGroup.addButton(self.checkBox_2)
        self.horizontalLayout.addWidget(self.checkBox_2)
        self.checkBox_3 = QtWidgets.QCheckBox(self.layoutWidget)
        self.checkBox_3.setObjectName("checkBox_3")
        self.buttonGroup.addButton(self.checkBox_3)
        self.horizontalLayout.addWidget(self.checkBox_3)
        self.checkBox_4 = QtWidgets.QCheckBox(self.layoutWidget)
        self.checkBox_4.setObjectName("checkBox_4")
        self.buttonGroup.addButton(self.checkBox_4)
        self.horizontalLayout.addWidget(self.checkBox_4)
        self.checkBox_5 = QtWidgets.QCheckBox(self.layoutWidget)
        self.checkBox_5.setObjectName("checkBox_5")
        self.buttonGroup.addButton(self.checkBox_5)
        self.horizontalLayout.addWidget(self.checkBox_5)
        self.layoutWidget1 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget1.setGeometry(QtCore.QRect(320, 150, 377, 25))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.checkBox_9 = QtWidgets.QCheckBox(self.layoutWidget1)
        self.checkBox_9.setObjectName("checkBox_9")
        self.buttonGroup_2 = QtWidgets.QButtonGroup(MainWindow)
        self.buttonGroup_2.setObjectName("buttonGroup_2")
        self.buttonGroup_2.addButton(self.checkBox_9)
        self.horizontalLayout_2.addWidget(self.checkBox_9)
        self.checkBox_8 = QtWidgets.QCheckBox(self.layoutWidget1)
        self.checkBox_8.setObjectName("checkBox_8")
        self.buttonGroup_2.addButton(self.checkBox_8)
        self.horizontalLayout_2.addWidget(self.checkBox_8)
        self.checkBox_6 = QtWidgets.QCheckBox(self.layoutWidget1)
        self.checkBox_6.setObjectName("checkBox_6")
        self.buttonGroup_2.addButton(self.checkBox_6)
        self.horizontalLayout_2.addWidget(self.checkBox_6)
        self.checkBox_10 = QtWidgets.QCheckBox(self.layoutWidget1)
        self.checkBox_10.setObjectName("checkBox_10")
        self.buttonGroup_2.addButton(self.checkBox_10)
        self.horizontalLayout_2.addWidget(self.checkBox_10)
        self.checkBox_7 = QtWidgets.QCheckBox(self.layoutWidget1)
        self.checkBox_7.setObjectName("checkBox_7")
        self.buttonGroup_2.addButton(self.checkBox_7)
        self.horizontalLayout_2.addWidget(self.checkBox_7)
        self.layoutWidget2 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget2.setGeometry(QtCore.QRect(320, 200, 377, 25))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.checkBox_14 = QtWidgets.QCheckBox(self.layoutWidget2)
        self.checkBox_14.setObjectName("checkBox_14")
        self.buttonGroup_3 = QtWidgets.QButtonGroup(MainWindow)
        self.buttonGroup_3.setObjectName("buttonGroup_3")
        self.buttonGroup_3.addButton(self.checkBox_14)
        self.horizontalLayout_3.addWidget(self.checkBox_14)
        self.checkBox_13 = QtWidgets.QCheckBox(self.layoutWidget2)
        self.checkBox_13.setObjectName("checkBox_13")
        self.buttonGroup_3.addButton(self.checkBox_13)
        self.horizontalLayout_3.addWidget(self.checkBox_13)
        self.checkBox_11 = QtWidgets.QCheckBox(self.layoutWidget2)
        self.checkBox_11.setObjectName("checkBox_11")
        self.buttonGroup_3.addButton(self.checkBox_11)
        self.horizontalLayout_3.addWidget(self.checkBox_11)
        self.checkBox_15 = QtWidgets.QCheckBox(self.layoutWidget2)
        self.checkBox_15.setObjectName("checkBox_15")
        self.buttonGroup_3.addButton(self.checkBox_15)
        self.horizontalLayout_3.addWidget(self.checkBox_15)
        self.checkBox_12 = QtWidgets.QCheckBox(self.layoutWidget2)
        self.checkBox_12.setObjectName("checkBox_12")
        self.buttonGroup_3.addButton(self.checkBox_12)
        self.horizontalLayout_3.addWidget(self.checkBox_12)
        self.layoutWidget3 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget3.setGeometry(QtCore.QRect(320, 240, 377, 25))
        self.layoutWidget3.setObjectName("layoutWidget3")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.layoutWidget3)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.checkBox_19 = QtWidgets.QCheckBox(self.layoutWidget3)
        self.checkBox_19.setObjectName("checkBox_19")
        self.buttonGroup_4 = QtWidgets.QButtonGroup(MainWindow)
        self.buttonGroup_4.setObjectName("buttonGroup_4")
        self.buttonGroup_4.addButton(self.checkBox_19)
        self.horizontalLayout_4.addWidget(self.checkBox_19)
        self.checkBox_18 = QtWidgets.QCheckBox(self.layoutWidget3)
        self.checkBox_18.setObjectName("checkBox_18")
        self.buttonGroup_4.addButton(self.checkBox_18)
        self.horizontalLayout_4.addWidget(self.checkBox_18)
        self.checkBox_16 = QtWidgets.QCheckBox(self.layoutWidget3)
        self.checkBox_16.setObjectName("checkBox_16")
        self.buttonGroup_4.addButton(self.checkBox_16)
        self.horizontalLayout_4.addWidget(self.checkBox_16)
        self.checkBox_20 = QtWidgets.QCheckBox(self.layoutWidget3)
        self.checkBox_20.setObjectName("checkBox_20")
        self.buttonGroup_4.addButton(self.checkBox_20)
        self.horizontalLayout_4.addWidget(self.checkBox_20)
        self.checkBox_17 = QtWidgets.QCheckBox(self.layoutWidget3)
        self.checkBox_17.setObjectName("checkBox_17")
        self.buttonGroup_4.addButton(self.checkBox_17)
        self.horizontalLayout_4.addWidget(self.checkBox_17)
        self.layoutWidget4 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget4.setGeometry(QtCore.QRect(320, 290, 377, 25))
        self.layoutWidget4.setObjectName("layoutWidget4")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.layoutWidget4)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.checkBox_24 = QtWidgets.QCheckBox(self.layoutWidget4)
        self.checkBox_24.setObjectName("checkBox_24")
        self.buttonGroup_5 = QtWidgets.QButtonGroup(MainWindow)
        self.buttonGroup_5.setObjectName("buttonGroup_5")
        self.buttonGroup_5.addButton(self.checkBox_24)
        self.horizontalLayout_5.addWidget(self.checkBox_24)
        self.checkBox_23 = QtWidgets.QCheckBox(self.layoutWidget4)
        self.checkBox_23.setObjectName("checkBox_23")
        self.buttonGroup_5.addButton(self.checkBox_23)
        self.horizontalLayout_5.addWidget(self.checkBox_23)
        self.checkBox_21 = QtWidgets.QCheckBox(self.layoutWidget4)
        self.checkBox_21.setObjectName("checkBox_21")
        self.buttonGroup_5.addButton(self.checkBox_21)
        self.horizontalLayout_5.addWidget(self.checkBox_21)
        self.checkBox_25 = QtWidgets.QCheckBox(self.layoutWidget4)
        self.checkBox_25.setObjectName("checkBox_25")
        self.buttonGroup_5.addButton(self.checkBox_25)
        self.horizontalLayout_5.addWidget(self.checkBox_25)
        self.checkBox_22 = QtWidgets.QCheckBox(self.layoutWidget4)
        self.checkBox_22.setObjectName("checkBox_22")
        self.buttonGroup_5.addButton(self.checkBox_22)
        self.horizontalLayout_5.addWidget(self.checkBox_22)
        self.layoutWidget5 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget5.setGeometry(QtCore.QRect(320, 330, 377, 25))
        self.layoutWidget5.setObjectName("layoutWidget5")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.layoutWidget5)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.checkBox_29 = QtWidgets.QCheckBox(self.layoutWidget5)
        self.checkBox_29.setObjectName("checkBox_29")
        self.buttonGroup_6 = QtWidgets.QButtonGroup(MainWindow)
        self.buttonGroup_6.setObjectName("buttonGroup_6")
        self.buttonGroup_6.addButton(self.checkBox_29)
        self.horizontalLayout_6.addWidget(self.checkBox_29)
        self.checkBox_28 = QtWidgets.QCheckBox(self.layoutWidget5)
        self.checkBox_28.setObjectName("checkBox_28")
        self.buttonGroup_6.addButton(self.checkBox_28)
        self.horizontalLayout_6.addWidget(self.checkBox_28)
        self.checkBox_26 = QtWidgets.QCheckBox(self.layoutWidget5)
        self.checkBox_26.setObjectName("checkBox_26")
        self.buttonGroup_6.addButton(self.checkBox_26)
        self.horizontalLayout_6.addWidget(self.checkBox_26)
        self.checkBox_30 = QtWidgets.QCheckBox(self.layoutWidget5)
        self.checkBox_30.setObjectName("checkBox_30")
        self.buttonGroup_6.addButton(self.checkBox_30)
        self.horizontalLayout_6.addWidget(self.checkBox_30)
        self.checkBox_27 = QtWidgets.QCheckBox(self.layoutWidget5)
        self.checkBox_27.setObjectName("checkBox_27")
        self.buttonGroup_6.addButton(self.checkBox_27)
        self.horizontalLayout_6.addWidget(self.checkBox_27)
        self.layoutWidget6 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget6.setGeometry(QtCore.QRect(320, 370, 377, 25))
        self.layoutWidget6.setObjectName("layoutWidget6")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.layoutWidget6)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.checkBox_34 = QtWidgets.QCheckBox(self.layoutWidget6)
        self.checkBox_34.setObjectName("checkBox_34")
        self.buttonGroup_7 = QtWidgets.QButtonGroup(MainWindow)
        self.buttonGroup_7.setObjectName("buttonGroup_7")
        self.buttonGroup_7.addButton(self.checkBox_34)
        self.horizontalLayout_7.addWidget(self.checkBox_34)
        self.checkBox_33 = QtWidgets.QCheckBox(self.layoutWidget6)
        self.checkBox_33.setObjectName("checkBox_33")
        self.buttonGroup_7.addButton(self.checkBox_33)
        self.horizontalLayout_7.addWidget(self.checkBox_33)
        self.checkBox_31 = QtWidgets.QCheckBox(self.layoutWidget6)
        self.checkBox_31.setObjectName("checkBox_31")
        self.buttonGroup_7.addButton(self.checkBox_31)
        self.horizontalLayout_7.addWidget(self.checkBox_31)
        self.checkBox_35 = QtWidgets.QCheckBox(self.layoutWidget6)
        self.checkBox_35.setObjectName("checkBox_35")
        self.buttonGroup_7.addButton(self.checkBox_35)
        self.horizontalLayout_7.addWidget(self.checkBox_35)
        self.checkBox_32 = QtWidgets.QCheckBox(self.layoutWidget6)
        self.checkBox_32.setObjectName("checkBox_32")
        self.buttonGroup_7.addButton(self.checkBox_32)
        self.horizontalLayout_7.addWidget(self.checkBox_32)
        self.layoutWidget7 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget7.setGeometry(QtCore.QRect(320, 400, 377, 25))
        self.layoutWidget7.setObjectName("layoutWidget7")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.layoutWidget7)
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.checkBox_39 = QtWidgets.QCheckBox(self.layoutWidget7)
        self.checkBox_39.setObjectName("checkBox_39")
        self.buttonGroup_8 = QtWidgets.QButtonGroup(MainWindow)
        self.buttonGroup_8.setObjectName("buttonGroup_8")
        self.buttonGroup_8.addButton(self.checkBox_39)
        self.horizontalLayout_8.addWidget(self.checkBox_39)
        self.checkBox_38 = QtWidgets.QCheckBox(self.layoutWidget7)
        self.checkBox_38.setObjectName("checkBox_38")
        self.buttonGroup_8.addButton(self.checkBox_38)
        self.horizontalLayout_8.addWidget(self.checkBox_38)
        self.checkBox_36 = QtWidgets.QCheckBox(self.layoutWidget7)
        self.checkBox_36.setObjectName("checkBox_36")
        self.buttonGroup_8.addButton(self.checkBox_36)
        self.horizontalLayout_8.addWidget(self.checkBox_36)
        self.checkBox_40 = QtWidgets.QCheckBox(self.layoutWidget7)
        self.checkBox_40.setObjectName("checkBox_40")
        self.buttonGroup_8.addButton(self.checkBox_40)
        self.horizontalLayout_8.addWidget(self.checkBox_40)
        self.checkBox_37 = QtWidgets.QCheckBox(self.layoutWidget7)
        self.checkBox_37.setObjectName("checkBox_37")
        self.buttonGroup_8.addButton(self.checkBox_37)
        self.horizontalLayout_8.addWidget(self.checkBox_37)
        self.layoutWidget8 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget8.setGeometry(QtCore.QRect(320, 440, 377, 25))
        self.layoutWidget8.setObjectName("layoutWidget8")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.layoutWidget8)
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.checkBox_44 = QtWidgets.QCheckBox(self.layoutWidget8)
        self.checkBox_44.setObjectName("checkBox_44")
        self.buttonGroup_9 = QtWidgets.QButtonGroup(MainWindow)
        self.buttonGroup_9.setObjectName("buttonGroup_9")
        self.buttonGroup_9.addButton(self.checkBox_44)
        self.horizontalLayout_9.addWidget(self.checkBox_44)
        self.checkBox_43 = QtWidgets.QCheckBox(self.layoutWidget8)
        self.checkBox_43.setObjectName("checkBox_43")
        self.buttonGroup_9.addButton(self.checkBox_43)
        self.horizontalLayout_9.addWidget(self.checkBox_43)
        self.checkBox_41 = QtWidgets.QCheckBox(self.layoutWidget8)
        self.checkBox_41.setObjectName("checkBox_41")
        self.buttonGroup_9.addButton(self.checkBox_41)
        self.horizontalLayout_9.addWidget(self.checkBox_41)
        self.checkBox_45 = QtWidgets.QCheckBox(self.layoutWidget8)
        self.checkBox_45.setObjectName("checkBox_45")
        self.buttonGroup_9.addButton(self.checkBox_45)
        self.horizontalLayout_9.addWidget(self.checkBox_45)
        self.checkBox_42 = QtWidgets.QCheckBox(self.layoutWidget8)
        self.checkBox_42.setObjectName("checkBox_42")
        self.buttonGroup_9.addButton(self.checkBox_42)
        self.horizontalLayout_9.addWidget(self.checkBox_42)
        self.layoutWidget9 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget9.setGeometry(QtCore.QRect(320, 470, 377, 25))
        self.layoutWidget9.setObjectName("layoutWidget9")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.layoutWidget9)
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.checkBox_49 = QtWidgets.QCheckBox(self.layoutWidget9)
        self.checkBox_49.setObjectName("checkBox_49")
        self.buttonGroup_10 = QtWidgets.QButtonGroup(MainWindow)
        self.buttonGroup_10.setObjectName("buttonGroup_10")
        self.buttonGroup_10.addButton(self.checkBox_49)
        self.horizontalLayout_10.addWidget(self.checkBox_49)
        self.checkBox_48 = QtWidgets.QCheckBox(self.layoutWidget9)
        self.checkBox_48.setObjectName("checkBox_48")
        self.buttonGroup_10.addButton(self.checkBox_48)
        self.horizontalLayout_10.addWidget(self.checkBox_48)
        self.checkBox_46 = QtWidgets.QCheckBox(self.layoutWidget9)
        self.checkBox_46.setObjectName("checkBox_46")
        self.buttonGroup_10.addButton(self.checkBox_46)
        self.horizontalLayout_10.addWidget(self.checkBox_46)
        self.checkBox_50 = QtWidgets.QCheckBox(self.layoutWidget9)
        self.checkBox_50.setObjectName("checkBox_50")
        self.buttonGroup_10.addButton(self.checkBox_50)
        self.horizontalLayout_10.addWidget(self.checkBox_50)
        self.checkBox_47 = QtWidgets.QCheckBox(self.layoutWidget9)
        self.checkBox_47.setObjectName("checkBox_47")
        self.buttonGroup_10.addButton(self.checkBox_47)
        self.horizontalLayout_10.addWidget(self.checkBox_47)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        self.menuFichier = QtWidgets.QMenu(self.menubar)
        self.menuFichier.setObjectName("menuFichier")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        #self.actionOuvrir = QtWidgets.QAction(MainWindow)
        #self.actionOuvrir.setObjectName("actionOuvrir")
        self.actionSauvgarder = QtWidgets.QAction(MainWindow)
        self.actionSauvgarder.setObjectName("actionSauvgarder")
        self.actionSauvgarder.triggered.connect(self.sauveGarder)
        self.actionQuitter = QtWidgets.QAction(MainWindow)
        self.actionQuitter.setObjectName("actionQuitter")
        self.actionQuitter.triggered.connect(self.closeEvent)
        self.actionA_propos = QtWidgets.QAction(MainWindow)
        self.actionA_propos.setObjectName("actionA_propos")
        self.actionA_propos.triggered.connect(self.Help)
        #self.menuFichier.addAction(self.actionOuvrir)
        self.menuFichier.addAction(self.actionSauvgarder)
        self.menuFichier.addAction(self.actionQuitter)
        self.menuHelp.addAction(self.actionA_propos)
        self.menubar.addAction(self.menuFichier.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.checkBox.stateChanged.connect(self.c11)  # mamicha
        self.checkBox_2.stateChanged.connect(self.c12)  # mamicha
        self.checkBox_3.stateChanged.connect(self.c13)  # mamicha
        self.checkBox_4.stateChanged.connect(self.c14)  # mamicha
        self.checkBox_5.stateChanged.connect(self.c15)  # mamicha

        self.checkBox_9.stateChanged.connect(self.c21)  # mamicha
        self.checkBox_8.stateChanged.connect(self.c22)  # mamicha
        self.checkBox_6.stateChanged.connect(self.c23)  # mamicha
        self.checkBox_10.stateChanged.connect(self.c24)  # mamicha
        self.checkBox_7.stateChanged.connect(self.c25)  # mamicha

        self.checkBox_14.stateChanged.connect(self.c31)  # mamicha
        self.checkBox_13.stateChanged.connect(self.c32)  # mamicha
        self.checkBox_11.stateChanged.connect(self.c33)  # mamicha
        self.checkBox_15.stateChanged.connect(self.c34)  # mamicha
        self.checkBox_12.stateChanged.connect(self.c35)  # mamicha

        self.checkBox_19.stateChanged.connect(self.c41)  # mamicha
        self.checkBox_18.stateChanged.connect(self.c42)  # mamicha
        self.checkBox_16.stateChanged.connect(self.c43)  # mamicha
        self.checkBox_20.stateChanged.connect(self.c44)  # mamicha
        self.checkBox_17.stateChanged.connect(self.c45)  # mamicha

        self.checkBox_24.stateChanged.connect(self.c51)  # mamicha
        self.checkBox_23.stateChanged.connect(self.c52)  # mamicha
        self.checkBox_21.stateChanged.connect(self.c53)  # mamicha
        self.checkBox_25.stateChanged.connect(self.c54)  # mamicha
        self.checkBox_22.stateChanged.connect(self.c55)  # mamicha

        self.checkBox_29.stateChanged.connect(self.c61)  # mamicha
        self.checkBox_28.stateChanged.connect(self.c62)  # mamicha
        self.checkBox_26.stateChanged.connect(self.c63)  # mamicha
        self.checkBox_30.stateChanged.connect(self.c64)  # mamicha
        self.checkBox_27.stateChanged.connect(self.c65)  # mamicha

        self.checkBox_34.stateChanged.connect(self.c71)  # mamicha
        self.checkBox_33.stateChanged.connect(self.c72)  # mamicha
        self.checkBox_31.stateChanged.connect(self.c73)  # mamicha
        self.checkBox_35.stateChanged.connect(self.c74)  # mamicha
        self.checkBox_32.stateChanged.connect(self.c75)  # mamicha

        self.checkBox_39.stateChanged.connect(self.c81)  # mamicha
        self.checkBox_38.stateChanged.connect(self.c82)  # mamicha
        self.checkBox_36.stateChanged.connect(self.c83)  # mamicha
        self.checkBox_40.stateChanged.connect(self.c84)  # mamicha
        self.checkBox_37.stateChanged.connect(self.c85)  # mamicha

        self.checkBox_44.stateChanged.connect(self.c91)  # mamicha
        self.checkBox_43.stateChanged.connect(self.c92)  # mamicha
        self.checkBox_41.stateChanged.connect(self.c93)  # mamicha
        self.checkBox_45.stateChanged.connect(self.c94)  # mamicha
        self.checkBox_42.stateChanged.connect(self.c95)  # mamicha

        self.checkBox_49.stateChanged.connect(self.c101)  # mamicha
        self.checkBox_48.stateChanged.connect(self.c102)  # mamicha
        self.checkBox_46.stateChanged.connect(self.c103)  # mamicha
        self.checkBox_50.stateChanged.connect(self.c104)  # mamicha
        self.checkBox_47.stateChanged.connect(self.c105)  # mamicha

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "sars-cov-2-covid-19-test-rapide"))
        self.label.setText(_translate("MainWindow", "checkpoint COVID-19"))
        self.label_2.setText(_translate("MainWindow", " Veuillez indiquez Votre age : "))
        self.comboBox.setItemText(0, _translate("MainWindow", "1"))
        self.comboBox.setItemText(1, _translate("MainWindow", "2"))
        self.comboBox.setItemText(2, _translate("MainWindow", "3"))
        self.comboBox.setItemText(3, _translate("MainWindow", "4"))
        self.comboBox.setItemText(4, _translate("MainWindow", "5"))
        self.comboBox.setItemText(5, _translate("MainWindow", "6"))
        self.comboBox.setItemText(6, _translate("MainWindow", "7"))
        self.comboBox.setItemText(7, _translate("MainWindow", "8"))
        self.comboBox.setItemText(8, _translate("MainWindow", "9"))
        self.comboBox.setItemText(9, _translate("MainWindow", "10"))
        self.comboBox.setItemText(10, _translate("MainWindow", "11"))
        self.comboBox.setItemText(11, _translate("MainWindow", "12"))
        self.comboBox.setItemText(12, _translate("MainWindow", "13"))
        self.comboBox.setItemText(13, _translate("MainWindow", "14"))
        self.comboBox.setItemText(14, _translate("MainWindow", "15"))
        self.comboBox.setItemText(15, _translate("MainWindow", "16"))
        self.comboBox.setItemText(16, _translate("MainWindow", "17"))
        self.comboBox.setItemText(17, _translate("MainWindow", "18"))
        self.comboBox.setItemText(18, _translate("MainWindow", "19"))
        self.comboBox.setItemText(19, _translate("MainWindow", "20"))
        self.comboBox.setItemText(20, _translate("MainWindow", "21"))
        self.comboBox.setItemText(21, _translate("MainWindow", "22"))
        self.comboBox.setItemText(22, _translate("MainWindow", "23"))
        self.comboBox.setItemText(23, _translate("MainWindow", "24"))
        self.comboBox.setItemText(24, _translate("MainWindow", "25"))
        self.comboBox.setItemText(25, _translate("MainWindow", "26"))
        self.comboBox.setItemText(26, _translate("MainWindow", "27"))
        self.comboBox.setItemText(27, _translate("MainWindow", "28"))
        self.comboBox.setItemText(28, _translate("MainWindow", "29"))
        self.comboBox.setItemText(29, _translate("MainWindow", "30"))
        self.comboBox.setItemText(30, _translate("MainWindow", "31"))
        self.comboBox.setItemText(31, _translate("MainWindow", "32"))
        self.comboBox.setItemText(32, _translate("MainWindow", "33"))
        self.comboBox.setItemText(33, _translate("MainWindow", "34"))
        self.comboBox.setItemText(34, _translate("MainWindow", "35"))
        self.comboBox.setItemText(35, _translate("MainWindow", "36"))
        self.comboBox.setItemText(36, _translate("MainWindow", "37"))
        self.comboBox.setItemText(37, _translate("MainWindow", "38"))
        self.comboBox.setItemText(38, _translate("MainWindow", "39"))
        self.comboBox.setItemText(39, _translate("MainWindow", "40"))
        self.comboBox.setItemText(40, _translate("MainWindow", "41"))
        self.comboBox.setItemText(41, _translate("MainWindow", "42"))
        self.comboBox.setItemText(42, _translate("MainWindow", "43"))
        self.comboBox.setItemText(43, _translate("MainWindow", "44"))
        self.comboBox.setItemText(44, _translate("MainWindow", "45"))
        self.comboBox.setItemText(45, _translate("MainWindow", "46"))
        self.comboBox.setItemText(46, _translate("MainWindow", "47"))
        self.comboBox.setItemText(47, _translate("MainWindow", "48"))
        self.comboBox.setItemText(48, _translate("MainWindow", "49"))
        self.comboBox.setItemText(49, _translate("MainWindow", "50"))
        self.comboBox.setItemText(50, _translate("MainWindow", "51"))
        self.comboBox.setItemText(51, _translate("MainWindow", "52"))
        self.comboBox.setItemText(52, _translate("MainWindow", "53"))
        self.comboBox.setItemText(53, _translate("MainWindow", "54"))
        self.comboBox.setItemText(54, _translate("MainWindow", "55"))
        self.comboBox.setItemText(55, _translate("MainWindow", "56"))
        self.comboBox.setItemText(56, _translate("MainWindow", "57"))
        self.comboBox.setItemText(57, _translate("MainWindow", "58"))
        self.comboBox.setItemText(58, _translate("MainWindow", "59"))
        self.comboBox.setItemText(59, _translate("MainWindow", "60"))
        self.comboBox.setItemText(60, _translate("MainWindow", "61"))
        self.comboBox.setItemText(61, _translate("MainWindow", "62"))
        self.comboBox.setItemText(62, _translate("MainWindow", "63"))
        self.comboBox.setItemText(63, _translate("MainWindow", "64"))
        self.comboBox.setItemText(64, _translate("MainWindow", "65"))
        self.comboBox.setItemText(65, _translate("MainWindow", "66"))
        self.comboBox.setItemText(66, _translate("MainWindow", "67"))
        self.comboBox.setItemText(67, _translate("MainWindow", "68"))
        self.comboBox.setItemText(68, _translate("MainWindow", "69"))
        self.comboBox.setItemText(69, _translate("MainWindow", "70"))
        self.comboBox.setItemText(70, _translate("MainWindow", "71"))
        self.comboBox.setItemText(71, _translate("MainWindow", "72"))
        self.comboBox.setItemText(72, _translate("MainWindow", "73"))
        self.comboBox.setItemText(73, _translate("MainWindow", "74"))
        self.comboBox.setItemText(74, _translate("MainWindow", "75"))
        self.comboBox.setItemText(75, _translate("MainWindow", "76"))
        self.comboBox.setItemText(76, _translate("MainWindow", "77"))
        self.comboBox.setItemText(77, _translate("MainWindow", "78"))
        self.comboBox.setItemText(78, _translate("MainWindow", "79"))
        self.comboBox.setItemText(79, _translate("MainWindow", "80"))
        self.comboBox.setItemText(80, _translate("MainWindow", "81"))
        self.comboBox.setItemText(81, _translate("MainWindow", "82"))
        self.comboBox.setItemText(82, _translate("MainWindow", "83"))
        self.comboBox.setItemText(83, _translate("MainWindow", "84"))
        self.comboBox.setItemText(84, _translate("MainWindow", "85"))
        self.comboBox.setItemText(85, _translate("MainWindow", "86"))
        self.comboBox.setItemText(86, _translate("MainWindow", "87"))
        self.comboBox.setItemText(87, _translate("MainWindow", "88"))
        self.comboBox.setItemText(88, _translate("MainWindow", "89"))
        self.comboBox.setItemText(89, _translate("MainWindow", "90"))
        self.comboBox.setItemText(90, _translate("MainWindow", "91"))
        self.comboBox.setItemText(91, _translate("MainWindow", "92"))
        self.comboBox.setItemText(92, _translate("MainWindow", "93"))
        self.comboBox.setItemText(93, _translate("MainWindow", "94"))
        self.comboBox.setItemText(94, _translate("MainWindow", "95"))
        self.comboBox.setItemText(95, _translate("MainWindow", "96"))
        self.comboBox.setItemText(96, _translate("MainWindow", "97"))
        self.comboBox.setItemText(97, _translate("MainWindow", "98"))
        self.comboBox.setItemText(98, _translate("MainWindow", "99"))
        self.comboBox.setItemText(99, _translate("MainWindow", "100"))
        self.label_3.setText(_translate("MainWindow", " Sortez-vous dehors (par jour) "))
        self.label_4.setText(_translate("MainWindow", " Lavez-vous les mains (par jour) "))
        self.label_5.setText(_translate("MainWindow", " Exercez-vous une activité physique "))
        self.label_6.setText(_translate("MainWindow", " Avez-vous de la fièvre "))
        self.label_7.setText(_translate("MainWindow", " Souffre-vous d'une toux "))
        self.label_8.setText(_translate("MainWindow", " Souffrez-vous d'un éternuement "))
        self.label_9.setText(_translate("MainWindow", " Souffrez-vous de la difficulté respiratoire "))
        self.label_10.setText(_translate("MainWindow", " Souffrez-vous d’un nez qui coule "))
        self.label_11.setText(_translate("MainWindow", " Avez-vous mal à la gorge "))
        self.label_12.setText(_translate("MainWindow", " Souffrez-vous du diarrhée "))
        self.pushButton.setText(_translate("MainWindow", "&Tester"))
        self.checkBox.setText(_translate("MainWindow", "Non"))
        self.checkBox_2.setText(_translate("MainWindow", "Rarement"))
        self.checkBox_3.setText(_translate("MainWindow", "Parfois"))
        self.checkBox_4.setText(_translate("MainWindow", "Souvent"))
        self.checkBox_5.setText(_translate("MainWindow", "Oui"))
        self.checkBox_9.setText(_translate("MainWindow", "Non"))
        self.checkBox_8.setText(_translate("MainWindow", "Rarement"))
        self.checkBox_6.setText(_translate("MainWindow", "Parfois"))
        self.checkBox_10.setText(_translate("MainWindow", "Souvent"))
        self.checkBox_7.setText(_translate("MainWindow", "Oui"))
        self.checkBox_14.setText(_translate("MainWindow", "Non"))
        self.checkBox_13.setText(_translate("MainWindow", "Rarement"))
        self.checkBox_11.setText(_translate("MainWindow", "Parfois"))
        self.checkBox_15.setText(_translate("MainWindow", "Souvent"))
        self.checkBox_12.setText(_translate("MainWindow", "Oui"))
        self.checkBox_19.setText(_translate("MainWindow", "Non"))
        self.checkBox_18.setText(_translate("MainWindow", "Rarement"))
        self.checkBox_16.setText(_translate("MainWindow", "Parfois"))
        self.checkBox_20.setText(_translate("MainWindow", "Souvent"))
        self.checkBox_17.setText(_translate("MainWindow", "Oui"))
        self.checkBox_24.setText(_translate("MainWindow", "Non"))
        self.checkBox_23.setText(_translate("MainWindow", "Rarement"))
        self.checkBox_21.setText(_translate("MainWindow", "Parfois"))
        self.checkBox_25.setText(_translate("MainWindow", "Souvent"))
        self.checkBox_22.setText(_translate("MainWindow", "Oui"))
        self.checkBox_29.setText(_translate("MainWindow", "Non"))
        self.checkBox_28.setText(_translate("MainWindow", "Rarement"))
        self.checkBox_26.setText(_translate("MainWindow", "Parfois"))
        self.checkBox_30.setText(_translate("MainWindow", "Souvent"))
        self.checkBox_27.setText(_translate("MainWindow", "Oui"))
        self.checkBox_34.setText(_translate("MainWindow", "Non"))
        self.checkBox_33.setText(_translate("MainWindow", "Rarement"))
        self.checkBox_31.setText(_translate("MainWindow", "Parfois"))
        self.checkBox_35.setText(_translate("MainWindow", "Souvent"))
        self.checkBox_32.setText(_translate("MainWindow", "Oui"))
        self.checkBox_39.setText(_translate("MainWindow", "Non"))
        self.checkBox_38.setText(_translate("MainWindow", "Rarement"))
        self.checkBox_36.setText(_translate("MainWindow", "Parfois"))
        self.checkBox_40.setText(_translate("MainWindow", "Souvent"))
        self.checkBox_37.setText(_translate("MainWindow", "Oui"))
        self.checkBox_44.setText(_translate("MainWindow", "Non"))
        self.checkBox_43.setText(_translate("MainWindow", "Rarement"))
        self.checkBox_41.setText(_translate("MainWindow", "Parfois"))
        self.checkBox_45.setText(_translate("MainWindow", "Souvent"))
        self.checkBox_42.setText(_translate("MainWindow", "Oui"))
        self.checkBox_49.setText(_translate("MainWindow", "Non"))
        self.checkBox_48.setText(_translate("MainWindow", "Rarement"))
        self.checkBox_46.setText(_translate("MainWindow", "Parfois"))
        self.checkBox_50.setText(_translate("MainWindow", "Souvent"))
        self.checkBox_47.setText(_translate("MainWindow", "Oui"))
        self.menuFichier.setTitle(_translate("MainWindow", "Fichier"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        #self.actionOuvrir.setText(_translate("MainWindow", "&Ouvrir"))
        self.actionSauvgarder.setText(_translate("MainWindow", "&Sauvgarder"))
        self.actionQuitter.setText(_translate("MainWindow", "&Quitter"))
        self.actionA_propos.setText(_translate("MainWindow", "A propos"))

    def closeEvent(self):
        msg = QtWidgets.QMessageBox()
        msg.setGeometry(200, 200, 100, 200)
        msg.setWindowModality(QtCore.Qt.NonModal)
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("SARS-COV-2  1.0")
        msg.setText('Voullez-vous quitter')
        #msg.setStandardButtons(QMessageBox.Yes | QMessageBox.Cancel)
        msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        msg.setEscapeButton(QMessageBox.Close)
        msg.show()
        reply = msg.exec_()
        if reply == QMessageBox.Yes:
            sys.exit(0)
        else:
            msg.Abort

    def info_covid(self):
        msg = QtWidgets.QMessageBox()
        msg.setGeometry(200, 200, 100, 200)
        msg.setWindowModality(QtCore.Qt.NonModal)
        msg.setWindowTitle("SARS-COV-2  1.0")
        ba3 = self.calcul/(3 * 100)
        msg.setText(self.lettre + " : R0: " + str("%.3f" % ba3) + " | Stresse : " + str("%.3f" % self.vvage))
        msg.show()
        msg.exec_()
    def parler_covid(self):
        engine = pyttsx3.init()
        engine.setProperty('rate', 120)
        engine.setProperty('volume', 0.8)
        voice = engine.getProperty('voices')[26]
        engine.setProperty('voice', 'french')
        engine.setProperty('voice', voice.id)
        engine.say(self.lettre)
        engine.runAndWait()

    def Help(self):
        msg = QtWidgets.QMessageBox()
        msg.setGeometry(200, 200, 100, 200)
        msg.setWindowModality(QtCore.Qt.NonModal)
        msg.setWindowTitle("SARS-COV-2  1.0")
        msg.setText('Bouraoui seyfallah (c)')
        msg.show()
        msg.exec_()
    def sauveGarder(self):
        now = datetime.now()
        # dd/mm/YY H:M:S
        dtstring = "Covid_19_"
        dt_string = now.strftime("%d_%m_%Y_%H_%M_%S")
        dtstring =dtstring + dt_string+".txt"
        text_file = open(dtstring, "w")
        text_file.writelines("Test Covid-19 : "+ dt_string)
        text_file.write("\n")
        text_file.writelines("Age :"  + self.comboBox.currentText())
        text_file.write("\n")
        text_file.writelines(str(self.val11) + ":" + str(self.val12) + ":" + str(self.val13) + ":" + str(self.val14) + ":" + str(self.val15))
        text_file.write("\n")
        text_file.writelines(str(self.val21) + ":" + str(self.val22) + ":" + str(self.val23) + ":" + str(self.val24) + ":" + str(self.val25))
        text_file.write("\n")
        text_file.writelines(str(self.val31) + ":" + str(self.val32) + ":" + str(self.val33) + ":" + str(self.val34) + ":" + str(self.val35))
        text_file.write("\n")
        text_file.writelines(str(self.val41) + ":" + str(self.val42) + ":" + str(self.val43) + ":" + str(self.val44) + ":" + str(self.val45))
        text_file.write("\n")
        text_file.writelines(str(self.val51) + ":" + str(self.val52) + ":" + str(self.val53) + ":" + str(self.val54) + ":" + str(self.val55))
        text_file.write("\n")
        text_file.writelines(str(self.val61) + ":" + str(self.val62) + ":" + str(self.val63) + ":" + str(self.val64) + ":" + str(self.val65))
        text_file.write("\n")
        text_file.writelines(str(self.val71) + ":" + str(self.val72) + ":" + str(self.val73) + ":" + str(self.val74) + ":" + str(self.val75))
        text_file.write("\n")
        text_file.writelines(str(self.val81) + ":" + str(self.val82) + ":" + str(self.val83) + ":" + str(self.val84) + ":" + str(self.val85))
        text_file.write("\n")
        text_file.writelines(str(self.val91) + ":" + str(self.val92) + ":" + str(self.val93) + ":" + str(self.val94) + ":" + str(self.val95))
        text_file.write("\n")
        text_file.writelines(str(self.val101) + ":" + str(self.val102) + ":" + str(self.val103) + ":" + str(self.val104) + ":" + str(self.val105))
        text_file.write("\n")
        text_file.writelines("-------------------------------o------------------------------------")
        text_file.close()

    def initself(self):
        self.val11 = 0
        self.val12 = 0
        self.val13 = 0
        self.val14 = 0
        self.val15 = 0
        self.val21 = 0
        self.val22 = 0
        self.val23 = 0
        self.val24 = 0
        self.val25 = 0
        self.val31 = 0
        self.val32 = 0
        self.val33 = 0
        self.val34 = 0
        self.val35 = 0
        self.val41 = 0
        self.val42 = 0
        self.val43 = 0
        self.val44 = 0
        self.val45 = 0
        self.val51 = 0
        self.val52 = 0
        self.val53 = 0
        self.val54 = 0
        self.val55 = 0
        self.val61 = 0
        self.val62 = 0
        self.val63 = 0
        self.val64 = 0
        self.val65 = 0
        self.val71 = 0
        self.val72 = 0
        self.val73 = 0
        self.val74 = 0
        self.val75 = 0
        self.val81 = 0
        self.val82 = 0
        self.val83 = 0
        self.val84 = 0
        self.val85 = 0
        self.val91 = 0
        self.val92 = 0
        self.val93 = 0
        self.val94 = 0
        self.val95 = 0
        self.val101 = 0
        self.val102 = 0
        self.val103 = 0
        self.val104 = 0
        self.val105 = 0


    def center(self):
        # geometry of the main window
        qr = self.frameGeometry()

        # center point of screen
        cp = QDesktopWidget().availableGeometry().center()

        # move rectangle's center point to screen's center point
        qr.moveCenter(cp)

        # top left of rectangle becomes top left of window centering it
        self.move(qr.topLeft())

if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
