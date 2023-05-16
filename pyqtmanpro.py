import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QTableWidget, QTableWidgetItem, QHeaderView, QLabel, QLineEdit, QVBoxLayout, QSpinBox
from PyQt5.uic import loadUi

app = QApplication(sys.argv)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # loadUi('mainwindow.ui', self)
        self.setWindowTitle('Startup Success or Fail')

        self.table = QTableWidget(self)
        self.table.setColumnCount(7)
        self.table.setRowCount(1)
        self.table.setItem(0, 0, QTableWidgetItem('Nama'))
        self.table.setItem(0, 1, QTableWidgetItem('Category'))
        self.table.setItem(0, 2, QTableWidgetItem('Funding'))
        self.table.setItem(0, 3, QTableWidgetItem('Country'))
        self.table.setItem(0, 4, QTableWidgetItem('State'))
        self.table.setItem(0, 5, QTableWidgetItem('Region'))
        self.table.setItem(0, 6, QTableWidgetItem('City'))

        header = self.table.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.Stretch)

        self.setCentralWidget(self.table)

        layout = QVBoxLayout()

        label1 = QLabel('Name:', self)
        input1 = QLineEdit(self)
        label2 = QLabel('Category:', self)
        input2 = QLineEdit(self)
        label3 = QLabel('Funding:', self)
        input3 = QLineEdit(self)
        label4 = QLabel('Country:', self)
        input4 = QLineEdit(self)
        label5 = QLabel('State:', self)
        input5 = QLineEdit(self)
        label6 = QLabel('Region:', self)
        input6 = QLineEdit(self)
        label7 = QLabel('City:', self)
        input7 = QLineEdit(self)

        layout.addWidget(label1)
        layout.addWidget(input1)
        layout.addWidget(label2)
        layout.addWidget(input2)
        layout.addWidget(label3)
        layout.addWidget(input3)
        layout.addWidget(label4)
        layout.addWidget(input4)
        layout.addWidget(label5)
        layout.addWidget(input5)
        layout.addWidget(label6)
        layout.addWidget(input6)
        layout.addWidget(label7)
        layout.addWidget(input7)

        widget = QWidget()
        widget.setLayout(layout)

        self.setCentralWidget(widget)

        self.show()

window = MainWindow()
sys.exit(app.exec_())