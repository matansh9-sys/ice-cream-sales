import numpy as np
import matplotlib.pyplot as plt

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


if __name__ == "__main__":

    temperatures, revenues = load_sales("Ice Cream.csv")

    coefficients, line_function = calculate_trendline(
        temperatures, revenues
    )

    fig, ax = plt.subplots(1, 1)

    fig, ax = plt.subplots(1, 1)

    ax.scatter(temperatures, revenues, s=1, label="Data")

    line_x = np.linspace(min(temperatures), max(temperatures), 100)
    line_y = line_function(line_x)

    ax.plot(line_x, line_y, color="red", label="Trend Line")

    ax.set_xlabel("Outdoor Temperature (C)")
    ax.set_ylabel("Revenue")
    ax.set_title("Ice Cream Sales vs Temperature")

    ax.text(
        min(temperatures),
        max(revenues),
        f"y = {coefficients[0]:.2f}x {coefficients[1]:+.2f}",
        color="red"
    )

    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)

    ax.legend()

    plt.show()

