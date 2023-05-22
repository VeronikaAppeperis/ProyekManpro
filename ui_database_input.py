import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QTableWidget, QTableWidgetItem, QHeaderView, QLabel, QLineEdit, QVBoxLayout
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
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

        # Membuat button Enter
        button = QPushButton('Enter', self)
        button.clicked.connect(self.on_enter_clicked)

        layout.addWidget(button)

        self.show()

    def on_enter_clicked(self):
        row_count = self.table.rowCount()
        self.table.insertRow(row_count)
        for column in range(self.table.columnCount()):
            item = QTableWidgetItem()
            item.setTextAlignment(Qt.AlignCenter)
            item.setText(self.layout().itemAt(column * 2 + 1).widget().text())
            self.table.setItem(row_count, column, item)

        # Menghapus teks input setelah tombol Enter ditekan
        for i in range(self.layout().count()):
            if isinstance(self.layout().itemAt(i).widget(), QLineEdit):
                self.layout().itemAt(i).widget().clear()

app = QApplication(sys.argv)
window = MainWindow()
sys.exit(app.exec_())