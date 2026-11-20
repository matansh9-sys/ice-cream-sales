import numpy as np
import matplotlib.pyplot as plt
from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QPushButton,
    QVBoxLayout
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
