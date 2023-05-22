import os
import sys
from output2 import Ui_MainWindow
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import *
from PyQt5.QtChart import *
from PyQt5.QtWidgets import *

class MainWindow:
    def __init__(self):
        self.main_win=QMainWindow()
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self.main_win)

        self.ui.stackedWidget.setCurrentWidget(self.ui.bc)
        self.ui.pbc_button.clicked.connect(self.show_pbc)
        self.ui.pc_button.clicked.connect(self.show_pc)
        self.ui.nd_button.clicked.connect(self.show_nd)
        self.ui.lc_button.clicked.connect(self.show_lc)
        self.ui.bc_button.clicked.connect(self.show_bc)
        
    def show(self):
        self.main_win.show()

    def show_pbc(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.pbc)
    def show_pc(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.pc)
    def show_lc(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.lc)
    def show_bc(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.bc)
    def show_nd(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.nd)

if __name__=='__main__':
    app=QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec_())

# app = QApplication(sys.argv)
# window = QMainWindow()
# ui = Ui_MainWindow()
# ui.setupUi(window)


# window.show()
# sys.exit(app.exec_())