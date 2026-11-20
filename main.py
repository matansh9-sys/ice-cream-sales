import numpy as np
import matplotlib.pyplot as plt


from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QPushButton,
    QVBoxLayout,
    QFileDialog
)

from About import AboutWindow

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

        self.temperatures = []
        self.revenues = []
        self.coefficients = []
        self.line_function = None


        self.setWindowTitle("Ice Cream Sales")
        self.resize(600, 250)

        layout = QVBoxLayout()

        self.title = QLabel("Ice Cream Sales Analysis")
        layout.addWidget(self.title)

        self.graph_button = QPushButton("Show Graph")
        layout.addWidget(self.graph_button)

        self.graph_button.clicked.connect(self.draw_graph)
        self.graph_button.setEnabled(False)

        self.open_button = QPushButton("Choose CSV File")
        layout.addWidget(self.open_button)

        self.open_button.clicked.connect(self.choose_file)

        
        self.status_label = QLabel("No CSV file loaded")
        layout.addWidget(self.status_label)

        self.about_button = QPushButton("About")
        layout.addWidget(self.about_button)

        self.about_button.clicked.connect(self.open_about)

        self.setLayout(layout)

    def choose_file(self):

        result = QFileDialog.getOpenFileName(
            self,
            "Choose CSV File",
            "",
            "CSV Files (*.csv)"
        )

        filename = result[0]

        if filename == "":
            return

        try:
            temperatures, revenues = load_sales(filename)

            coefficients, line_function = calculate_trendline(
                temperatures, revenues
            )

        except Exception as error:
            self.status_label.setText("Error: " + str(error))
            return

        self.temperatures = temperatures
        self.revenues = revenues
        self.coefficients = coefficients
        self.line_function = line_function

        self.status_label.setText("Loaded: " + filename)

        self.graph_button.setEnabled(True)

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

    def open_about(self):

        self.about_window = AboutWindow()
        self.about_window.show()




if __name__ == "__main__":

    app = QApplication([])

    with open("style.qss", "r") as file:
        app.setStyleSheet(file.read())

    window = IceCreamWindow()
    window.show()

    app.exec()
