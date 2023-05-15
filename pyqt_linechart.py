import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtChart import QChart, QChartView, QLineSeries

def main():
    app = QApplication(sys.argv)

    window = QMainWindow()
    window.setWindowTitle("Simple PyQt5 Chart Example")
    window.setGeometry(100, 100, 800, 600)

    chart = QChart()
    series = QLineSeries()
    series.append(0, 6)
    series.append(2, 4)
    series.append(3, 8)
    series.append(7, 4)
    series.append(10, 5)
    chart.addSeries(series)
    chart.createDefaultAxes()

    chart_view = QChartView(chart, window)
    chart_view.setGeometry(10, 10, 780, 580)

    window.show()

    sys.exit(app.exec_())

if __name__ == '__main__':
    main()