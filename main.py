import numpy as np
import matplotlib.pyplot as plt

from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QPushButton,
    QVBoxLayout,
    QLineEdit
)


filename = "Ice Cream.csv"

def load_sales(filename):

    temperatures = []
    revenues = []

    with open(filename, "r") as file:

        next(file)

        for line in file:

            if line.strip() != "":

                temperature, revenue = line.strip().split(",")

                temperatures.append(float(temperature))
                revenues.append(float(revenue))

    return temperatures, revenues


def calculate_trendline(temperatures, revenues):

    coefficients = np.polyfit(temperatures, revenues, 1)

    line_function = np.poly1d(coefficients)

    return coefficients, line_function

class FileWindow(QWidget):

    def __init__(self, main_window):
        super().__init__()

        self.main_window = main_window

        self.setWindowTitle("Choose CSV File")
        self.resize(450, 180)

        layout = QVBoxLayout()

        self.label = QLabel("Enter CSV file name or path:")
        layout.addWidget(self.label)

        self.file_input = QLineEdit()
        self.file_input.setText("Ice Cream.csv")
        layout.addWidget(self.file_input)

        self.load_button = QPushButton("Load CSV")
        layout.addWidget(self.load_button)

        self.message = QLabel("")
        layout.addWidget(self.message)

        self.load_button.clicked.connect(self.load_file)

        self.setLayout(layout)

    def load_file(self):

        filename = self.file_input.text()

        if filename == "":
            self.message.setText("Please enter a file name")
            return

        try:
            temperatures, revenues = load_sales(filename)

            coefficients, line_function = calculate_trendline(
                temperatures, revenues
            )

        except Exception as error:
            self.message.setText("Error: " + str(error))
            return

        self.main_window.temperatures = temperatures
        self.main_window.revenues = revenues
        self.main_window.coefficients = coefficients
        self.main_window.line_function = line_function

        self.main_window.status_label.setText(
            "Loaded: " + filename
        )

        self.close()

class IceCreamWindow(QWidget):

    def __init__(self):
        super().__init__()

        self.temperatures, self.revenues = load_sales("Ice Cream.csv")

        self.coefficients, self.line_function = calculate_trendline(
            self.temperatures,
            self.revenues
        )

        self.setWindowTitle("Ice Cream Sales")
        self.resize(600, 250)

        layout = QVBoxLayout()

        self.title = QLabel("Ice Cream Sales Analysis")
        layout.addWidget(self.title)

        self.graph_button = QPushButton("Show Graph")
        layout.addWidget(self.graph_button)

        self.graph_button.clicked.connect(self.draw_graph)

        self.file_window = FileWindow(self)

        self.open_button = QPushButton("Choose CSV File")
        layout.addWidget(self.open_button)

        self.open_button.clicked.connect(self.file_window.show)

        self.status_label = QLabel("Loaded: Ice Cream.csv")
        layout.addWidget(self.status_label)

        self.setLayout(layout)

    def draw_graph(self):

        fig, ax = plt.subplots(1, 1)

        ax.scatter(
            self.temperatures,
            self.revenues,
            s=1,
            label="Data"
        )

        line_x = np.linspace(
            min(self.temperatures),
            max(self.temperatures),
            100
        )

        line_y = self.line_function(line_x)

        ax.plot(
            line_x,
            line_y,
            color="red",
            label="Trend Line"
        )

        ax.set_xlabel("Outdoor Temperature (C)")
        ax.set_ylabel("Revenue")
        ax.set_title("Ice Cream Sales vs Temperature")

        ax.text(
            min(self.temperatures),
            max(self.revenues),
            f"y = {self.coefficients[0]:.2f}x {self.coefficients[1]:+.2f}",
            color="red"
        )

        ax.spines["top"].set_visible(False)
        ax.spines["right"].set_visible(False)

        ax.legend()

        plt.show()


if __name__ == "__main__":

    app = QApplication([])

    window = IceCreamWindow()
    window.show()

    app.exec()
