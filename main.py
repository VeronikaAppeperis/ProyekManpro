import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
from PyQt5.QtChart import QChart, QChartView, QAreaSeries, QPieSeries, QLineSeries, QBarSeries, QBarSet, QBarCategoryAxis

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Simple PyQt5 Charts Example")
        self.setGeometry(100, 100, 800, 600)

        layout = QVBoxLayout()
        central_widget = QWidget(self)
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        # Area Chart
        area_chart = QChart()
        area_series = QAreaSeries()
        area_series.append(0, 0)
        area_series.append(1, 3)
        area_series.append(2, 2)
        area_series.append(3, 4)
        area_series.append(4, 1)
        area_series.append(5, 5)
        area_series.append(6, 3)
        area_chart.addSeries(area_series)
        area_chart.createDefaultAxes()
        area_chart.setTitle("Area Chart")

        area_chart_view = QChartView(area_chart)
        layout.addWidget(area_chart_view)

        # Pie Chart
        pie_chart = QChart()
        pie_series = QPieSeries()
        pie_series.append("Apples", 30)
        pie_series.append("Bananas", 50)
        pie_series.append("Oranges", 20)
        pie_chart.addSeries(pie_series)
        pie_chart.setTitle("Pie Chart")

        pie_chart_view = QChartView(pie_chart)
        layout.addWidget(pie_chart_view)

        # Line Chart
        line_chart = QChart()
        line_series = QLineSeries()
        line_series.append(0, 6)
        line_series.append(2, 4)
        line_series.append(3, 8)
        line_series.append(7, 4)
        line_series.append(10, 5)
        line_chart.addSeries(line_series)
        line_chart.createDefaultAxes()
        line_chart.setTitle("Line Chart")

        line_chart_view = QChartView(line_chart)
        layout.addWidget(line_chart_view)

        # Bar Chart
        bar_chart = QChart()
        bar_series = QBarSeries()
        bar_set = QBarSet("Series 1")
        bar_set << 1 << 2 << 3 << 4 << 5
        bar_series.append(bar_set)
        bar_chart.addSeries(bar_series)
        bar_chart.createDefaultAxes()
        bar_chart.setTitle("Bar Chart")

        bar_chart_view = QChartView(bar_chart)
        layout.addWidget(bar_chart_view)


def main():
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
