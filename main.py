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


if __name__ == "__main__":

    temperatures, revenues = load_sales("Ice Cream.csv")

    print("Number of records:", len(temperatures))
    print("First temperature:", temperatures[0])
    print("First revenue:", revenues[0])
