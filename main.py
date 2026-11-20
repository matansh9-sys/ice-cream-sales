import numpy as np

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

    print("Number of records:", len(temperatures))
    print("Slope:", coefficients[0])
    print("Intercept:", coefficients[1])
    print("Predicted revenue at 25 degrees:", line_function(25))
