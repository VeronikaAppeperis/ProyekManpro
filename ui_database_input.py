import sys
import sqlite3
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QTableWidget, QTableWidgetItem, QHeaderView, QLabel, QLineEdit, QVBoxLayout, QSpinBox

app = QApplication(sys.argv)

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

        button = QPushButton('Submit', self)
        layout.addWidget(button)

        widget = QWidget()
        widget.setLayout(layout)

        self.setCentralWidget(widget)

        button.clicked.connect(lambda: self.submitData(input1.text(), input2.text(), input3.text(), input4.text(), input5.text(), input6.text(), input7.text()))

        self.show()

    def submitData(self, name, category, funding, country, state, region, city):
        # buat koneksi ke database
        conn = sqlite3.connect('startup.db')
        cursor = conn.cursor()

        # buat tabel jika belum ada
        cursor.execute('''CREATE TABLE IF NOT EXISTS startup
                        (name TEXT, category TEXT, funding INT, country TEXT, state TEXT, region TEXT, city TEXT)''')

        # masukkan data ke dalam tabel
        cursor.execute("INSERT INTO startup VALUES (?, ?, ?, ?, ?, ?, ?)", (name, category, int(funding), country, state, region, city))
        conn.commit()

        # tampilkan data di tabel
        rowCount = self.table.rowCount()
        self.table.insertRow(rowCount)
        self.table.setItem(rowCount, 0, QTableWidgetItem(name))
        self.table.setItem(rowCount, 1, QTableWidgetItem(category))
        self.table.setItem(rowCount, 2, QTableWidgetItem(str(funding)))
        self.table.setItem(rowCount, 3, QTableWidgetItem(country))
        self.table.setItem(rowCount, 4, QTableWidgetItem(state))
        self.table.setItem(rowCount, 5, QTableWidgetItem(region))
        self.table.setItem(rowCount, 6, QTableWidgetItem(city))

        # Menutup koneksi ke database
        cursor.close()
        conn.close()


if __name__ == '__main__':
    window = MainWindow()
    sys.exit(app.exec_())
