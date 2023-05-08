#install pyqt
# %pip install PyQt5


import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QTableWidget, QTableWidgetItem, QHeaderView,  QLabel, QLineEdit, QVBoxLayout, QSpinBox
from PyQt5.uic import loadUi


app = QApplication(sys.argv)

# import aplikasi pyqt

window = QWidget()
window.setWindowTitle('PyQt Application')


# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         loadUi('mainwindow.ui', self)
#         self.show()


# window = MainWindow()

window = QMainWindow()


table = QTableWidget(window)
table.setColumnCount(3)
table.setRowCount(2)
table.setItem(0, 0, QTableWidgetItem('Nama'))
table.setItem(0, 1, QTableWidgetItem('Revenue'))

header = table.horizontalHeader()
header.setSectionResizeMode(QHeaderView.Stretch)

window.setCentralWidget(table)


#untuk membuat inputan

layout = QVBoxLayout()

label1 = QLabel('Name:', window)
input1 = QLineEdit(window)
label2 = QLabel('Age:', window)
input2 = QSpinBox(window)

layout.addWidget(label1)
layout.addWidget(input1)
layout.addWidget(label2)
layout.addWidget(input2)

window.setLayout(layout)
window.show()
app.exec_()
