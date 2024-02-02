import matplotlib.pyplot as plt
import numpy as np
import scipy.integrate as spi


def f(x):
    """Target function"""
    return x**2

# Defining the function and integration boundary
a = 0  # Lower bound
b = 2  # Upper bound


def draw_function():
    # Creating a range of values for x
    x = np.linspace(-0.5, 2.5, 400)
    y = f(x)

    # Creating a graph
    fig, ax = plt.subplots()

    # Drawing a function
    ax.plot(x, y, "r", linewidth=2)

    # Filling the area under the curve
    ix = np.linspace(a, b)
    iy = f(ix)
    ax.fill_between(ix, iy, color="gray", alpha=0.3)

    # Setting up the graph
    ax.set_xlim([x[0], x[-1]])
    ax.set_ylim([0, max(y) + 0.1])
    ax.set_xlabel("x")
    ax.set_ylabel("f(x)")

    # Adding integration limits and graph title
    ax.axvline(x=a, color="gray", linestyle="--")
    ax.axvline(x=b, color="gray", linestyle="--")
    ax.set_title("Graph of integration of f(x) = x^2 from " + str(a) + " to " + str(b))
    plt.grid()
    plt.show()


def calculate_integral():
    """To check the value of the integral"""
    result, error = spi.quad(f, a, b)
    print("Integral: ", result)


def main():
    # calculate the value of the integral of a function using the Monte Carlo method.
    # TODO create a model of the integral
    # TODO solve the model and print the results
    calculate_integral()


if __name__ == "__main__":
    main()
