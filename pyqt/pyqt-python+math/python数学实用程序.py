# 2020.2.19-2020.6.7
import numpy as np
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from matplotlib.lines import Line2D
import matplotlib as mpl
import matplotlib.pyplot as plt
import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from Ui_untitled import Ui_MainWindow

from sympy import *


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.radioButton.toggled.connect(
            lambda: self.btnstate(self.radioButton))
        self.radioButton_2.toggled.connect(
            lambda: self.btnstate(self.radioButton_2))

        self.radioButton_3.toggled.connect(
            lambda: self.btnstate_2(self.radioButton_3))
        self.radioButton_4.toggled.connect(
            lambda: self.btnstate_2(self.radioButton_4))
        self.radioButton_5.toggled.connect(
            lambda: self.btnstate_2(self.radioButton_5))
        self.radioButton_6.toggled.connect(
            lambda: self.btnstate_2(self.radioButton_6))

        self.radioButton_7.toggled.connect(
            lambda: self.btnstate_3(self.radioButton_7))
        self.radioButton_8.toggled.connect(
            lambda: self.btnstate_3(self.radioButton_8))
        self.radioButton_9.toggled.connect(
            lambda: self.btnstate_3(self.radioButton_9))
        self.radioButton_10.toggled.connect(
            lambda: self.btnstate_3(self.radioButton_10))

        self.checkBox.toggled.connect(lambda: self.checkBox_1(self.checkBox))
        self.checkBox_2.toggled.connect(
            lambda: self.checkBox_t(self.checkBox_2))

        self.pushButton_4.clicked.connect(self.initUi_3)

        self.pushButton_2.clicked.connect(self.pushButton_Clicked1)

        self.action_E.triggered.connect(self.close)
        self.action_A.triggered.connect(self.msg)
        i = 'none'
        self.i = i
# ????????????????????????????????????
        self.pushButton.clicked.connect(self.initUi_1)
        self.gridlayout = QGridLayout(self.groupBox_2)

        self.pushButton_3.clicked.connect(self.initUi_2)
        self.gridlayout2 = QGridLayout(self.groupBox_3)

        self.pushButton_4.clicked.connect(self.initUi_3)
        self.gridlayout3 = QGridLayout(self.groupBox_4)

        self.pushButton_5.clicked.connect(self.initUi_4)
        self.gridlayout4 = QGridLayout(self.groupBox_5)

        self.spinBox.valueChanged.connect(self.valuechange)
        self.d_n = 1

# ??????????????????????????????????????????(?????????)
    def initUi_1(self):
        global sol1, sol2, yr_a, yr_b, yr_c, yr_d, yr_b_z, yr_c_z
        yr_a = self.lineEdit_4.displayText()
        yr_b = self.lineEdit_5.displayText()
        yr_c = self.lineEdit_6.displayText()
        if yr_a == '' or yr_b == '' or yr_c == '' or yr_a == '0':
            error = QMessageBox.critical(self, '??????', '????????????,\n??????????????????',
                                         QMessageBox.Yes)
            print(error)

        else:
            delta = float(yr_b) ** 2 - 4 * float(yr_a) * float(yr_c)
            if float(yr_b) >= 0:
                yr_b_z = '+' + str(yr_b)
            else:
                yr_b_z = str(yr_b)

            if float(yr_c) >= 0:
                yr_c_z = '+' + str(yr_c)
            else:
                yr_c_z = str(yr_c)
            self.textBrowser_4.clear()
            self.textBrowser_4.append(
                'y=' + str(yr_a) + 'x^2' + yr_b_z + 'x' + yr_c_z)
            yr_d = float(yr_b) / -(2 * float(yr_a))
            self.textBrowser_4.append('????????????' + str(yr_d))
            self.textBrowser_4.append('delta=' + str(delta))
            if delta > 0:
                self.mpl_f = Figure_Canvas(self, width=5, height=5, dpi=100)
        # ???MyFigure???????????????????????????
                self.gridlayout.addWidget(self.mpl_f, 0, 1)
                sol1 = (-float(yr_b) - float(delta) ** 0.5) / (2 * float(yr_a))
                sol2 = (-float(yr_b) + float(delta) ** 0.5) / (2 * float(yr_a))
                self.mpl_f.fig_1()
                self.textBrowser_4.append(
                    '????????????\n' + 'x1=' + str(sol1.real) + ',\n' + 'x2=' + str(sol2.real))
            elif delta == 0:
                self.mpl_f = Figure_Canvas(self, width=5, height=5, dpi=100)
                self.mpl_f.fig_2()
        # ???MyFigure???????????????????????????
                self.gridlayout.addWidget(self.mpl_f, 0, 1)
                sol1 = (-float(yr_b) - float(delta) ** 0.5) / (2 * float(yr_a))
                self.textBrowser_4.append('????????????\n' + 'x1=x2=' + str(sol1.real))
            else:
                self.mpl_f = Figure_Canvas(self, width=5, height=5, dpi=100)
                self.mpl_f.fig_2()
        # ???MyFigure???????????????????????????
                self.gridlayout.addWidget(self.mpl_f, 0, 1)
                sol1 = (-float(yr_b) - float(delta) ** 0.5) / (2 * float(yr_a))
                sol2 = (-float(yr_b) + float(delta) ** 0.5) / (2 * float(yr_a))
                self.textBrowser_4.append(
                    '????????????\n' + 'x1=' + str(sol1) + ',\n' + 'x2=' + str(sol2))

    def msg(self):
        reply = QMessageBox.about(self, '??????', '''                     Python+??????-GUI 1.0.0-beta
    matplotlib?????????????????????????????????PyQt5???????????????
                              ?????????????????????
                  ???????????????GNU???????????????????????????3???
                      Email:w1443469207@163.com
                          ???????????? (C) faawdd 2020''')
        print(reply)

    def btnstate_2(self, btn):
        if btn.text() == '1.>0' and btn.isChecked() == True:
            i = 'c_1'
            self.i = i
        if btn.text() == '2.<0' and btn.isChecked() == True:
            i = 'c_2'
            self.i = i
        if btn.text() == '3.>=0' and btn.isChecked() == True:
            i = 'c_3'
            self.i = i
        if btn.text() == '4.<=0' and btn.isChecked() == True:
            i = 'c_4'
            self.i = i

    def btnstate_3(self, btn):
        if btn.text() == '1.x' and btn.isChecked() == True:
            i = 'p_1'
            self.i = i
        if btn.text() == '2.y' and btn.isChecked() == True:
            i = 'p_2'
            self.i = i
        if btn.text() == '3.-x' and btn.isChecked() == True:
            i = 'p_3'
            self.i = i
        if btn.text() == '4.-y' and btn.isChecked() == True:
            i = 'p_4'
            self.i = i

# ????????????????????????
    def initUi_2(self):
        global sol1, sol2, yr_a, yr_b, yr_c, yr_d, yr_b_z, yr_c_z
        yr_a = self.lineEdit_7.displayText()
        yr_b = self.lineEdit_8.displayText()
        yr_c = self.lineEdit_9.displayText()
        if yr_a == '' or yr_b == '' or yr_c == '' or yr_a == '0':
            error = QMessageBox.critical(self, '??????', '????????????,\n??????????????????',
                                         QMessageBox.Yes)
            print(error)

        else:
            delta = float(yr_b) ** 2 - 4 * float(yr_a) * float(yr_c)
            if float(yr_b) >= 0:
                yr_b_z = '+' + str(yr_b)
            else:
                yr_b_z = str(yr_b)

            if float(yr_c) >= 0:
                yr_c_z = '+' + str(yr_c)
            else:
                yr_c_z = str(yr_c)
            self.textBrowser_5.clear()
            yr_d = float(yr_b) / -(2 * float(yr_a))
            if self.i == 'c_1':
                if float(yr_a) > 0:
                    self.textBrowser_5.append(
                        str(yr_a) + 'x^2' + yr_b_z + 'x' + yr_c_z + '>0')
                    self.textBrowser_5.append('????????????' + str(yr_d))
                    self.textBrowser_5.append('delta=' + str(delta))
                    if delta > 0:
                        self.mpl_f = Figure_Canvas(
                            self, width=5, height=5, dpi=100)
        # ???MyFigure???????????????????????????
                        self.gridlayout2.addWidget(self.mpl_f, 0, 1)
                        sol1 = (-float(yr_b) - float(delta)
                                ** 0.5) / (2 * float(yr_a))
                        sol2 = (-float(yr_b) + float(delta)
                                ** 0.5) / (2 * float(yr_a))
                        self.mpl_f.fig_1()
                        self.textBrowser_5.append(
                            '?????????\n' + 'x1???x2\n' + '{x|x<' + str(sol1.real) + ',' + 'x>' + str(sol2.real) + '}')
                    elif delta == 0:
                        self.mpl_f = Figure_Canvas(
                            self, width=5, height=5, dpi=100)
        # ???MyFigure???????????????????????????
                        self.gridlayout2.addWidget(self.mpl_f, 0, 1)
                        sol1 = (-float(yr_b) - float(delta)
                                ** 0.5) / (2 * float(yr_a))
                        self.mpl_f.fig_2()
                        self.textBrowser_5.append(
                            '?????????\n' + 'x1=x2\n' + '{x|x???' + str(sol1.real) + '}')
                    else:
                        self.mpl_f = Figure_Canvas(
                            self, width=5, height=5, dpi=100)
        # ???MyFigure???????????????????????????
                        self.gridlayout2.addWidget(self.mpl_f, 0, 1)
                        sol1 = (-float(yr_b) - float(delta)
                                ** 0.5) / (2 * float(yr_a))
                        self.mpl_f.fig_2()
                        self.textBrowser_5.append('?????????\n' + '{x|x???R(????????????)}')
                else:
                    self.textBrowser_5.append(
                        str(yr_a) + 'x^2' + yr_b_z + 'x' + yr_c_z + '>0')
                    self.textBrowser_5.append('????????????' + str(yr_d))
                    self.textBrowser_5.append('delta=' + str(delta))
                    if delta > 0:
                        self.mpl_f = Figure_Canvas(
                            self, width=5, height=5, dpi=100)
        # ???MyFigure???????????????????????????
                        self.gridlayout2.addWidget(self.mpl_f, 0, 1)
                        sol1 = (-float(yr_b) - float(delta)
                                ** 0.5) / (2 * float(yr_a))
                        sol2 = (-float(yr_b) + float(delta)
                                ** 0.5) / (2 * float(yr_a))
                        self.mpl_f.fig_1()
                        self.textBrowser_5.append(
                            '?????????\n' + 'x1???x2\n' + '{x|' + str(sol2.real) + '<x<' + str(sol1.real) + '}')
                    elif delta == 0:
                        self.mpl_f = Figure_Canvas(
                            self, width=5, height=5, dpi=100)
        # ???MyFigure???????????????????????????
                        self.gridlayout2.addWidget(self.mpl_f, 0, 1)
                        sol1 = (-float(yr_b) - float(delta)
                                ** 0.5) / (2 * float(yr_a))
                        self.mpl_f.fig_2()
                        self.textBrowser_5.append(
                            '?????????\n' + 'x1=x2\n' + '???(??????)')
                    else:
                        self.mpl_f = Figure_Canvas(
                            self, width=5, height=5, dpi=100)
        # ???MyFigure???????????????????????????
                        self.gridlayout2.addWidget(self.mpl_f, 0, 1)
                        sol1 = (-float(yr_b) - float(delta)
                                ** 0.5) / (2 * float(yr_a))
                        self.mpl_f.fig_2()
                        self.textBrowser_5.append('?????????\n' + '???(??????)')
            elif self.i == 'c_2':
                if float(yr_a) > 0:
                    self.textBrowser_5.append(
                        str(yr_a) + 'x^2' + yr_b_z + 'x' + yr_c_z + '<0')
                    self.textBrowser_5.append('????????????' + str(yr_d))
                    self.textBrowser_5.append('delta=' + str(delta))
                    if delta > 0:
                        self.mpl_f = Figure_Canvas(
                            self, width=5, height=5, dpi=100)
        # ???MyFigure???????????????????????????
                        self.gridlayout2.addWidget(self.mpl_f, 0, 1)
                        sol1 = (-float(yr_b) - float(delta)
                                ** 0.5) / (2 * float(yr_a))
                        sol2 = (-float(yr_b) + float(delta)
                                ** 0.5) / (2 * float(yr_a))
                        self.mpl_f.fig_1()
                        self.textBrowser_5.append(
                            '?????????\n' + 'x1???x2\n' + '{x|' + str(sol1.real) + '<x<' + str(sol2.real) + '}')
                    elif delta == 0:
                        self.mpl_f = Figure_Canvas(
                            self, width=5, height=5, dpi=100)
        # ???MyFigure???????????????????????????
                        self.gridlayout2.addWidget(self.mpl_f, 0, 1)
                        sol1 = (-float(yr_b) - float(delta)
                                ** 0.5) / (2 * float(yr_a))
                        self.mpl_f.fig_2()
                        self.textBrowser_5.append(
                            '?????????\n' + 'x1=x2\n' + '???(??????)')
                    else:
                        self.mpl_f = Figure_Canvas(
                            self, width=5, height=5, dpi=100)
        # ???MyFigure???????????????????????????
                        self.gridlayout2.addWidget(self.mpl_f, 0, 1)
                        sol1 = (-float(yr_b) - float(delta)
                                ** 0.5) / (2 * float(yr_a))
                        self.mpl_f.fig_2()
                        self.textBrowser_5.append(
                            '?????????\n' + 'x1=x2\n' + '???(??????)')
                else:
                    self.textBrowser_5.append(
                        str(yr_a) + 'x^2' + yr_b_z + 'x' + yr_c_z + '<0')
                    self.textBrowser_5.append('????????????' + str(yr_d))
                    self.textBrowser_5.append('delta=' + str(delta))
                    if delta > 0:
                        self.mpl_f = Figure_Canvas(
                            self, width=5, height=5, dpi=100)
        # ???MyFigure???????????????????????????
                        self.gridlayout2.addWidget(self.mpl_f, 0, 1)
                        sol1 = (-float(yr_b) - float(delta)
                                ** 0.5) / (2 * float(yr_a))
                        sol2 = (-float(yr_b) + float(delta)
                                ** 0.5) / (2 * float(yr_a))
                        self.mpl_f.fig_1()
                        self.textBrowser_5.append(
                            '?????????\n' + 'x1???x2\n' + '{x|x<' + str(sol1.real) + ',' + 'x>' + str(sol2.real) + '}')
                    elif delta == 0:
                        self.mpl_f = Figure_Canvas(
                            self, width=5, height=5, dpi=100)
        # ???MyFigure???????????????????????????
                        self.gridlayout2.addWidget(self.mpl_f, 0, 1)
                        sol1 = (-float(yr_b) - float(delta)
                                ** 0.5) / (2 * float(yr_a))
                        self.mpl_f.fig_2()
                        self.textBrowser_5.append(
                            '?????????\n' + 'x1=x2\n' + '{x|x???' + str(sol1.real) + '}')
                    else:
                        self.mpl_f = Figure_Canvas(
                            self, width=5, height=5, dpi=100)
        # ???MyFigure???????????????????????????
                        self.gridlayout2.addWidget(self.mpl_f, 0, 1)
                        sol1 = (-float(yr_b) - float(delta)
                                ** 0.5) / (2 * float(yr_a))
                        self.mpl_f.fig_2()
                        self.textBrowser_5.append('?????????\n' + '{x|x???R(????????????)}')
            elif self.i == 'c_3':
                if float(yr_a) > 0:
                    self.textBrowser_5.append(
                        str(yr_a) + 'x^2' + yr_b_z + 'x' + yr_c_z + '???0')
                    self.textBrowser_5.append('????????????' + str(yr_d))
                    self.textBrowser_5.append('delta=' + str(delta))
                    if delta > 0:
                        self.mpl_f = Figure_Canvas(
                            self, width=5, height=5, dpi=100)
        # ???MyFigure???????????????????????????
                        self.gridlayout2.addWidget(self.mpl_f, 0, 1)
                        sol1 = (-float(yr_b) - float(delta)
                                ** 0.5) / (2 * float(yr_a))
                        sol2 = (-float(yr_b) + float(delta)
                                ** 0.5) / (2 * float(yr_a))
                        self.mpl_f.fig_1()
                        self.textBrowser_5.append(
                            '?????????\n' + 'x1???x2\n' + '{x|x???' + str(sol1.real) + ',' + 'x???' + str(sol2.real) + '}')
                    elif delta == 0:
                        self.mpl_f = Figure_Canvas(
                            self, width=5, height=5, dpi=100)
        # ???MyFigure???????????????????????????
                        self.gridlayout2.addWidget(self.mpl_f, 0, 1)
                        sol1 = (-float(yr_b) - float(delta)
                                ** 0.5) / (2 * float(yr_a))
                        self.mpl_f.fig_2()
                        self.textBrowser_5.append('?????????\n' + '{x|x???R(????????????)}')
                    else:
                        self.mpl_f = Figure_Canvas(
                            self, width=5, height=5, dpi=100)
        # ???MyFigure???????????????????????????
                        self.gridlayout2.addWidget(self.mpl_f, 0, 1)
                        sol1 = (-float(yr_b) - float(delta)
                                ** 0.5) / (2 * float(yr_a))
                        self.mpl_f.fig_2()
                        self.textBrowser_5.append('?????????\n' + '{x|x???R(????????????)}')
                else:
                    self.textBrowser_5.append(
                        str(yr_a) + 'x^2' + yr_b_z + 'x' + yr_c_z + '???0')
                    self.textBrowser_5.append('????????????' + str(yr_d))
                    self.textBrowser_5.append('delta=' + str(delta))
                    if delta > 0:
                        self.mpl_f = Figure_Canvas(
                            self, width=5, height=5, dpi=100)
        # ???MyFigure???????????????????????????
                        self.gridlayout2.addWidget(self.mpl_f, 0, 1)
                        sol1 = (-float(yr_b) - float(delta)
                                ** 0.5) / (2 * float(yr_a))
                        sol2 = (-float(yr_b) + float(delta)
                                ** 0.5) / (2 * float(yr_a))
                        self.mpl_f.fig_1()
                        self.textBrowser_5.append(
                            '?????????\n' + 'x1???x2\n' + '{x|' + str(sol2.real) + '???x???' + str(sol1.real) + '}')
                    elif delta == 0:
                        self.mpl_f = Figure_Canvas(
                            self, width=5, height=5, dpi=100)
        # ???MyFigure???????????????????????????
                        self.gridlayout2.addWidget(self.mpl_f, 0, 1)
                        sol1 = (-float(yr_b) - float(delta)
                                ** 0.5) / (2 * float(yr_a))
                        self.mpl_f.fig_2()
                        self.textBrowser_5.append(
                            '?????????\n' + 'x1=x2\n' + '{x|x=' + str(sol1.real) + '}')
                    else:
                        self.mpl_f = Figure_Canvas(
                            self, width=5, height=5, dpi=100)
        # ???MyFigure???????????????????????????
                        self.gridlayout2.addWidget(self.mpl_f, 0, 1)
                        sol1 = (-float(yr_b) - float(delta)
                                ** 0.5) / (2 * float(yr_a))
                        self.mpl_f.fig_2()
                        self.textBrowser_5.append('?????????\n' + '???(??????)')
            elif self.i == 'c_4':
                if float(yr_a) > 0:
                    self.textBrowser_5.append(
                        str(yr_a) + 'x^2' + yr_b_z + 'x' + yr_c_z + '???0')
                    self.textBrowser_5.append('????????????' + str(yr_d))
                    self.textBrowser_5.append('delta=' + str(delta))
                    if delta > 0:
                        self.mpl_f = Figure_Canvas(
                            self, width=5, height=5, dpi=100)
        # ???MyFigure???????????????????????????
                        self.gridlayout2.addWidget(self.mpl_f, 0, 1)
                        sol1 = (-float(yr_b) - float(delta)
                                ** 0.5) / (2 * float(yr_a))
                        sol2 = (-float(yr_b) + float(delta)
                                ** 0.5) / (2 * float(yr_a))
                        self.mpl_f.fig_1()
                        self.textBrowser_5.append(
                            '?????????\n' + 'x1???x2\n' + '{x|' + str(sol1.real) + '???x???' + str(sol2.real) + '}')
                    elif delta == 0:
                        self.mpl_f = Figure_Canvas(
                            self, width=5, height=5, dpi=100)
        # ???MyFigure???????????????????????????
                        self.gridlayout2.addWidget(self.mpl_f, 0, 1)
                        sol1 = (-float(yr_b) - float(delta)
                                ** 0.5) / (2 * float(yr_a))
                        self.mpl_f.fig_2()
                        self.textBrowser_5.append(
                            '?????????\n' + 'x1=x2\n' + '{x|x=' + str(sol1.real) + '}')
                    else:
                        self.mpl_f = Figure_Canvas(
                            self, width=5, height=5, dpi=100)
        # ???MyFigure???????????????????????????
                        self.gridlayout2.addWidget(self.mpl_f, 0, 1)
                        sol1 = (-float(yr_b) - float(delta)
                                ** 0.5) / (2 * float(yr_a))
                        self.mpl_f.fig_2()
                        self.textBrowser_5.append(
                            '?????????\n' + 'x1=x2\n' + '???(??????)')
                else:
                    self.textBrowser_5.append(
                        str(yr_a) + 'x^2' + yr_b_z + 'x' + yr_c_z + '???0')
                    self.textBrowser_5.append('????????????' + str(yr_d))
                    self.textBrowser_5.append('delta=' + str(delta))
                    if delta > 0:
                        self.mpl_f = Figure_Canvas(
                            self, width=5, height=5, dpi=100)
        # ???MyFigure???????????????????????????
                        self.gridlayout2.addWidget(self.mpl_f, 0, 1)
                        sol1 = (-float(yr_b) - float(delta)
                                ** 0.5) / (2 * float(yr_a))
                        sol2 = (-float(yr_b) + float(delta)
                                ** 0.5) / (2 * float(yr_a))
                        self.mpl_f.fig_1()
                        self.textBrowser_5.append(
                            '?????????\n' + 'x1???x2\n' + '{x|x???' + str(sol1.real) + ',' + 'x???' + str(sol2.real) + '}')
                    elif delta == 0:
                        self.mpl_f = Figure_Canvas(
                            self, width=5, height=5, dpi=100)
        # ???MyFigure???????????????????????????
                        self.gridlayout2.addWidget(self.mpl_f, 0, 1)
                        sol1 = (-float(yr_b) - float(delta)
                                ** 0.5) / (2 * float(yr_a))
                        self.mpl_f.fig_2()
                        self.textBrowser_5.append('?????????\n' + '{x|x???R(????????????)}')
                    else:
                        self.mpl_f = Figure_Canvas(
                            self, width=5, height=5, dpi=100)
        # ???MyFigure???????????????????????????
                        self.gridlayout2.addWidget(self.mpl_f, 0, 1)
                        sol1 = (-float(yr_b) - float(delta)
                                ** 0.5) / (2 * float(yr_a))
                        self.mpl_f.fig_2()
                        self.textBrowser_5.append('?????????\n' + '{x|x???R(????????????)}')
            else:
                error = QMessageBox.critical(self, '??????', '?????????',
                                             QMessageBox.Yes)
                print(error)
# ??????????????????

    def initUi_3(self):
        self.textBrowser_6.clear()
        global p, t
        p = self.lineEdit_10.displayText()
        if p == '':
            error = QMessageBox.critical(self, '??????', 'p????????????',
                                         QMessageBox.Yes)
            print(error)
        else:
            if self.i == 'p_1':
                p = float(p)
                if p > 0:
                    t = - (p / 2)
                    self.textBrowser_6.append('y^2=' + str(2 * p) + 'x')
                    self.textBrowser_6.append('?????????x=' + str(t))
                    self.textBrowser_6.append('?????????' + '(' + str(-t) + ',0)')
                    self.mpl_f = Figure_Canvas(
                        self, width=5, height=5, dpi=100)
                    self.gridlayout3.addWidget(self.mpl_f, 0, 1)
                    self.mpl_f.fig_3()
                else:
                    error = QMessageBox.critical(self, '??????', 'p>0',
                                                 QMessageBox.Yes)
                    print(error)
            elif self.i == 'p_2':
                p = float(p)
                if p > 0:
                    t = - (p / 2)
                    self.textBrowser_6.append('x^2=' + str(2 * p) + 'x')
                    self.textBrowser_6.append('?????????y=' + str(t))
                    self.textBrowser_6.append('?????????' + '(0,' + str(-t) + ')')
                    self.mpl_f = Figure_Canvas(
                        self, width=5, height=5, dpi=100)
                    self.gridlayout3.addWidget(self.mpl_f, 0, 1)
                    self.mpl_f.fig_5()
                else:
                    error = QMessageBox.critical(self, '??????', 'p>0',
                                                 QMessageBox.Yes)
                    print(error)
            elif self.i == 'p_3':
                p = float(p)
                if p > 0:
                    t = p / 2
                    self.textBrowser_6.append('y^2=-' + str(2 * p) + 'x')
                    self.textBrowser_6.append('?????????x=' + str(t))
                    self.textBrowser_6.append('?????????' + '(' + str(-t) + ',0)')
                    self.mpl_f = Figure_Canvas(
                        self, width=5, height=5, dpi=100)
                    self.gridlayout3.addWidget(self.mpl_f, 0, 1)
                    self.mpl_f.fig_4()
                else:
                    error = QMessageBox.critical(self, '??????', 'p>0',
                                                 QMessageBox.Yes)
                    print(error)
            elif self.i == 'p_4':
                p = float(p)
                if p > 0:
                    t = p / 2
                    self.textBrowser_6.append('x^2=-' + str(2 * p) + 'x')
                    self.textBrowser_6.append('?????????y=' + str(t))
                    self.textBrowser_6.append('?????????' + '(0,' + str(-t) + ')')
                    self.mpl_f = Figure_Canvas(
                        self, width=5, height=5, dpi=100)
                    self.gridlayout3.addWidget(self.mpl_f, 0, 1)
                    self.mpl_f.fig_6()
                else:
                    error = QMessageBox.critical(self, '??????', 'p>0',
                                                 QMessageBox.Yes)
                    print(error)
            else:
                error = QMessageBox.critical(self, '??????', '?????????',
                                             QMessageBox.Yes)
                print(error)

    def valuechange(self):
        d_n = int(self.spinBox.value())
        self.d_n = d_n

    def checkBox_1(self):
        if self.checkBox.isChecked() == True:
            apart(d_z)
            self.textBrowser_7.append('f(x)=' + str(d_y) + '???' + str(
                self.d_n) + '?????????\n' + 'f\'(x)=' + str(d_z) + '\n' + '?????????' + str(d_j))
        else:
            self.textBrowser_7.append('f(x)=' + str(d_y) + '???' + str(
                self.d_n) + '?????????\n' + 'f\'(x)=' + str(d_z) + '\n' + '?????????' + str(d_j))

    def checkBox_t(self):
        if self.checkBox_2.isChecked() == True:
            self.mpl_f.fig_7()
        else:
            pass
        
    def initUi_4(self):
        self.textBrowser_7.clear()
        global d_y, d_x, d_z, d_j
        d_y = self.lineEdit_11.displayText()
        if d_y == '':
            error = QMessageBox.critical(self, '??????', '????????????',
                                         QMessageBox.Yes)
            print(error)
        else:
            d_x = symbols('x')
            d_z = diff(d_y, d_x, self.d_n)
            d_j = solve(d_z)
            self.checkBox_1()
            self.mpl_f = Figure_Canvas(
                self, width=5, height=5, dpi=100)
            self.gridlayout4.addWidget(self.mpl_f, 0, 1)
            self.checkBox_t()

# ???????????????
    def btnstate(self, btn):
        if btn.text() == '????????????(&C)':
            if btn.isChecked() == True:
                i = 'dc'
                self.i = i
        if btn.text() == '????????????(&B)':
            if btn.isChecked() == True:
                i = 'db'
                self.i = i

    def pushButton_Clicked1(self):
        self.textBrowser.clear()
        if self.i == 'dc':
            A = self.lineEdit.displayText()
            d = self.lineEdit_2.displayText()
            n = 1
            weishu = self.lineEdit_3.displayText()
            if weishu == '' or d == '' or A == '':
                error = QMessageBox.critical(self, '??????', 'a1 ??? d ??? ?????? ?????????',
                                             QMessageBox.Yes)
                print(error)
            else:
                A = float(A)
                d = float(d)
                weishu = int(weishu)
                if weishu < 2:
                    error = QMessageBox.critical(self, '??????', '????????????',
                                                 QMessageBox.Yes)
                    print(error)
                else:
                    if weishu > 5000:
                        error = QMessageBox.warning(self, '??????', '??????????????????5000??????????????????????????????',
                                                    QMessageBox.Yes)
                        print(error)
                    self.textBrowser.append('?????????')
                    self.textBrowser.append('A1:' + str(A))
                    S = weishu * A + (weishu*(weishu - 1)) / 2 * d
                    self.textBrowser_2.setPlainText(str(S))
                    while True:
                        n = n + 1
                        A = A + d
                        self.textBrowser.append('A' + str(n) + ':' + str(A))
                        if n == weishu:
                            break
                    self.textBrowser.moveCursor(
                        self.textBrowser.textCursor().End)
        elif self.i == 'db':
            A = self.lineEdit.displayText()
            Q = self.lineEdit_2.displayText()
            n = 1
            weishu = self.lineEdit_3.displayText()
            if weishu == '' or Q == '' or A == '':
                error = QMessageBox.critical(self, '??????', 'a1 ??? Q ??? ?????? ?????????',
                                             QMessageBox.Yes)
                print(error)
            else:
                A = float(A)
                Q = float(Q)
                weishu = int(weishu)
                if weishu < 2 or Q == 0 or A == 0:
                    error = QMessageBox.critical(self, '??????', 'a1 ??? Q ??????0',
                                                 QMessageBox.Yes)
                    print(error)
                else:
                    if weishu > 5000:
                        error = QMessageBox.warning(self, '??????', '??????????????????5000??????????????????????????????',
                                                    QMessageBox.Yes)
                        print(error)
                    self.textBrowser.append('?????????')
                    self.textBrowser.append('A1:' + str(A))
                    if Q == 1:
                        S = weishu * A
                    else:
                        S = (A * (1 - Q ** weishu)) / (1 - Q)
                    self.textBrowser_2.setPlainText(str(S))
                    while True:
                        n = n + 1
                        A = A * Q
                        self.textBrowser.append('A' + str(n) + ':' + str(A))
                        if n == weishu:
                            break
        else:
            error = QMessageBox.critical(self, '??????', '?????????',
                                         QMessageBox.Yes)
            print(error)


# ?????????
class Figure_Canvas(FigureCanvas):
    def __init__(self, parent=None, width=5, height=5, dpi=100):
        self.fig = Figure(figsize=(width, height), dpi=100)
        self.axes = self.fig.add_subplot(111)
        FigureCanvas.__init__(self, self.fig)
        self.setParent(parent)

    def fig_1(self):
        self.axes.clear()
        self.fig.suptitle('y=' + str(yr_a) + 'x^2' + yr_b_z + 'x' + yr_c_z)
        self.axes.axvline(x=0, color='r')
        self.axes.axhline(y=0, color='r')
        self.axes.axvline(x=float(yr_d), ls='--', color='y')
        if float(yr_a) > 0:
            x = np.arange(sol1-0.5, sol2+0.5, 0.00001)
        else:
            x = np.arange(sol2-0.5, sol1+0.5, 0.00001)
        y = float(yr_a) * x ** 2 + float(yr_b) * x + float(yr_c)
        self.axes.plot(x, y)
        self.axes.grid(True)

    def fig_2(self):
        self.axes.clear()
        self.fig.suptitle('y=' + str(yr_a) + 'x^2' + yr_b_z + 'x' + yr_c_z)
        self.axes.axvline(x=0, color='r')
        self.axes.axhline(y=0, color='r')
        self.axes.axvline(x=float(yr_d), ls='--', color='y')
        x = np.arange(0-10, 0+10, 0.00001)
        y = float(yr_a) * x ** 2 + float(yr_b) * x + float(yr_c)
        self.axes.plot(x, y)
        self.axes.grid(True)

    def fig_3(self):
        self.axes.clear()
        self.fig.suptitle('y^2=2' + str(p) + 'x')
        self.axes.axvline(x=0, color='r')
        self.axes.axhline(y=0, color='r')
        self.axes.axvline(x=t, linestyle='--')
        y = np.arange(-2*p, 2*p, 0.00001)
        x = y ** 2 / (2 * p)
        self.axes.plot(x, y)
        self.axes.grid(True)

    def fig_4(self):
        self.axes.clear()
        self.fig.suptitle('y^2=-2' + str(p) + 'x')
        self.axes.axvline(x=0, color='r')
        self.axes.axhline(y=0, color='r')
        self.axes.axvline(x=t, linestyle='--')
        y = np.arange(-2*p, 2*p, 0.00001)
        x = -y ** 2 / (2 * p)
        self.axes.plot(x, y)
        self.axes.grid(True)

    def fig_5(self):
        self.axes.clear()
        self.fig.suptitle('x^2=2' + str(p) + 'x')
        self.axes.axvline(x=0, color='r')
        self.axes.axhline(y=0, color='r')
        self.axes.axhline(y=t, linestyle='--')
        x = np.arange(-2*p, 2*p, 0.00001)
        y = x ** 2 / (2 * p)
        self.axes.plot(x, y)
        self.axes.grid(True)

    def fig_6(self):
        self.axes.clear()
        self.fig.suptitle('x^2=-2' + str(p) + 'x')
        self.axes.axvline(x=0, color='r')
        self.axes.axhline(y=0, color='r')
        self.axes.axhline(y=t, linestyle='--')
        x = np.arange(-2*p, 2*p, 0.00001)
        y = -x ** 2 / (2 * p)
        self.axes.plot(x, y)
        self.axes.grid(True)

    def fig_7(self):
        self.axes.clear()
        self.fig.suptitle('f(x)=' + str(d_y))
        self.axes.axvline(x=0, color='r')
        self.axes.axhline(y=0, color='r')
        x = np.arange(-20, 20, 0.00001)
        y = eval(str(d_y))
        self.axes.plot(x, y)
        self.axes.grid(True)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = MainWindow()
    ui.show()
    sys.exit(app.exec_())
