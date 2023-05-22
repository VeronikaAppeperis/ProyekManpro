# #barchart

# import sys
# from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
# from PyQt5.QtChart import QChart, QChartView, QBarSet, QBarSeries, QBarCategoryAxis, QValueAxis
# from PyQt5.QtGui import QPainter, QColor
# from PyQt5.QtCore import Qt
# import pandas as pd

# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()

#         self.initUI()

#     def initUI(self):
#         # Read data from the Excel file using pandas
#         df = pd.read_csv("data.csv")

#         # Filter the DataFrame for status key 1
#         df_status_1 = df[df['statusKey'] == 1]
#         status_1_counts = df_status_1['category_funding'].value_counts()

#         # Filter the DataFrame for status key 2
#         df_status_2 = df[df['statusKey'] == 2]
#         status_2_counts = df_status_2['category_funding'].value_counts()

#         # Convert value_counts result for status 1 into a list of values and frequencies
#         categories_1 = status_1_counts.index.tolist()
#         frequencies_1 = status_1_counts.values.tolist()

#         # Convert value_counts result for status 2 into a list of values and frequencies
#         categories_2 = status_2_counts.index.tolist()
#         frequencies_2 = status_2_counts.values.tolist()

#         # Create a QBarSet object for status key 1 and add data from the frequencies list
#         barset_1 = QBarSet('Status 1')
#         for value in frequencies_1:
#             barset_1.append(value)

#         # Create a QBarSet object for status key 2 and add data from the frequencies list
#         barset_2 = QBarSet('Status 2')
#         for value in frequencies_2:
#             barset_2.append(value)

#         # Set different colors for each QBarSet
#         barset_1.setColor(QColor(75, 123, 163))  # Blue color for status key 1
#         barset_2.setColor(QColor(242, 142, 43))  # Red color for status key 2

#         # Create a QBarSeries object and add the QBarSet objects
#         barseries = QBarSeries()
#         barseries.append(barset_1)
#         barseries.append(barset_2)

#         # Create a QChart object and add the QBarSeries
#         chart = QChart()
#         chart.addSeries(barseries)

#         # Create a QBarCategoryAxis object and set labels on the x-axis
#         axis_x = QBarCategoryAxis()
#         for category in categories_1:
#             axis_x.append(str(category))
#         chart.addAxis(axis_x, Qt.AlignBottom)
#         barseries.attachAxis(axis_x)

#         # Create a QValueAxis object and set the range and label format on the y-axis
#         axis_y = QValueAxis()
#         axis_y.setRange(0, max(max(frequencies_1), max(frequencies_2)))  # Set the range based on the maximum value
#         axis_y.setLabelFormat("%i")  # Set the label format to integer
#         chart.addAxis(axis_y, Qt.AlignLeft)
#         barseries.attachAxis(axis_y)

#         # Create a QChartView object and set the displayed chart
#         chart_view = QChartView(chart)
#         chart_view.setRenderHint(QPainter.Antialiasing)

#         # Set up the main layout
#         layout = QVBoxLayout()
#         layout.addWidget(chart_view)

#         # Create the main widget and set the layout
#         widget = QWidget()
#         widget.setLayout(layout)

#         # Set the main widget as the central widget of the window
#         self.setCentralWidget(widget)
#         # Set the window title
#         self.setWindowTitle('Contoh PyQt dan QtCharts')

# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     window = MainWindow()
#     window.show()
#     sys.exit(app.exec_())


# # piechart
# import sys
# from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
# from PyQt5.QtChart import QChart, QChartView, QPieSeries, QPieSlice
# from PyQt5.QtGui import QPainter, QColor
# from PyQt5.QtCore import Qt
# import pandas as pd

# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()

#         self.initUI()

#     def initUI(self):
#         # Read data from the Excel file using pandas
#         df = pd.read_csv("data.csv")

#         # Filter the DataFrame for status key 1
#         df_status_1 = df[df['statusKey'] == 1]

#         # Get the top 5 categoryKey counts for status key 1
#         category_counts = df_status_1['category_list'].value_counts().head(5)

#         # Calculate the total count
#         total_count = category_counts.sum()

#         # Calculate the percentages for each slice
#         percentages = category_counts / total_count * 100

#         # Create QPieSeries and QPieSlice for each category and percentage
#         pie_series = QPieSeries()
#         for i, (category, count) in enumerate(category_counts.items()):
#             percentage = percentages[category]
#             slice_ = QPieSlice(f"{category} ({percentage:.1f}%)", count)
#             pie_series.append(slice_)

#         # Create a QChart object and add the QPieSeries
#         chart = QChart()
#         chart.addSeries(pie_series)

#         # Create a QChartView object and set the displayed chart
#         chart_view = QChartView(chart)
#         chart_view.setRenderHint(QPainter.Antialiasing)

#         # Set up the main layout
#         layout = QVBoxLayout()
#         layout.addWidget(chart_view)

#         # Create the main widget and set the layout
#         widget = QWidget()
#         widget.setLayout(layout)

#         # Set the main widget as the central widget of the window
#         self.setCentralWidget(widget)

# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     window = MainWindow()
#     window.show()
#     sys.exit(app.exec_())


#barchart

# import sys
# from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
# from PyQt5.QtChart import QChart, QChartView, QBarSet, QBarSeries, QBarCategoryAxis, QValueAxis, QHorizontalBarSeries
# from PyQt5.QtGui import QPainter, QColor
# from PyQt5.QtCore import Qt
# import pandas as pd

# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()

#         self.initUI()

#     def initUI(self):
#         # Read data from the Excel file using pandas
#         df = pd.read_csv("data.csv")

#         # Filter the DataFrame for status key 1
#         df_status_1 = df[df['statusKey'] == 1]
#         status_1_counts = df_status_1['region'].value_counts().head(5)

#         # Filter the DataFrame for status key 2
#         df_status_2 = df[df['statusKey'] == 2]
#         status_2_counts = df_status_2['region'].value_counts().head(5)

#         # Convert value_counts result for status 1 into a list of values and frequencies
#         categories_1 = status_1_counts.index.tolist()
#         frequencies_1 = status_1_counts.values.tolist()

#         # Convert value_counts result for status 2 into a list of values and frequencies
#         categories_2 = status_2_counts.index.tolist()
#         frequencies_2 = status_2_counts.values.tolist()

#         # Create a QBarSet object for status key 1 and add data from the frequencies list
#         barset_1 = QBarSet('Status 1')
#         for value in frequencies_1:
#             barset_1.append(value)

#         # Create a QBarSet object for status key 2 and add data from the frequencies list
#         barset_2 = QBarSet('Status 2')
#         for value in frequencies_2:
#             barset_2.append(value)

#         # Set different colors for each QBarSet
#         barset_1.setColor(QColor(75, 123, 163))  # Blue color for status key 1
#         barset_2.setColor(QColor(242, 142, 43))  # Red color for status key 2

#         # Create a QBarSeries object and add the QBarSet objects
#         barseries = QHorizontalBarSeries()
#         barseries.append(barset_1)
#         barseries.append(barset_2)
        

#         # Create a QChart object and add the QBarSeries
#         chart = QChart()
#         chart.addSeries(barseries)

#         # Create a QCategoryAxis object for the y-axis (vertical axis)
#         axis_y = QBarCategoryAxis()
#         for category in categories_1:
#             axis_y.append(str(category))
#         chart.addAxis(axis_y, Qt.AlignLeft)
#         barseries.attachAxis(axis_y)

#         # Create a QValueAxis object for the x-axis (horizontal axis)
#         axis_x = QValueAxis()
#         chart.addAxis(axis_x, Qt.AlignBottom)
#         barseries.attachAxis(axis_x)

#         axis_x = QBarCategoryAxis()

#         # Create a QChartView object and set the displayed chart
#         chart_view = QChartView(chart)
#         chart_view.setRenderHint(QPainter.Antialiasing)

#         # Set up the main layout
#         layout = QVBoxLayout()
#         layout.addWidget(chart_view)

#         # Create the main widget and set the layout
#         widget = QWidget()
#         widget.setLayout(layout)

#         # Set the main widget as the central widget of the window
#         self.setCentralWidget(widget)
#         # Set the window title
#         self.setWindowTitle('Contoh PyQt dan QtCharts')

# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     window = MainWindow()
#     window.show()
#     sys.exit(app.exec_())
