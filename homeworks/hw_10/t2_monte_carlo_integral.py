import matplotlib.pyplot as plt
import numpy as np
import scipy.integrate as spi
import random


def f(x):
    """Target function"""
    return x**2


def draw_function(a, b):
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
    ax.set_title("Graph of integration of f(x) = x^2 from " +
                 str(a) + " to " + str(b))
    plt.grid()
    plt.show()


def is_point_below_line(func, x, y):
    """
    A function to check if a given point is below a line defined by a function.
    Takes in the line function f_x, x-coordinate of the point, and y-coordinate of the point.
    """
    # Evaluate the line function at x
    line_y = func(x)

    # Check if the point is below the line
    return y <= line_y


def monte_carlo_simulation(func, a, b, num_experiments=100, num_points_per_experiment=1000):
    """
    Perform a Monte Carlo simulation to estimate the area under the curve.

    Args:
        a (float): lower limit of the integration
        b (float): upper limit of the integration
        num_experiments (int, optional): The number of experiments to run. Defaults to 100.
        num_points_per_experiment (int, optional): The number of points to sample per experiment. Defaults to 1000.
    Returns:
        float: The estimated integral.
    """
    total_integral_estimate = 0

    for _ in range(num_experiments):
        x_values = np.random.uniform(a, b, num_points_per_experiment)
        y_values = np.random.uniform(
            0, max(func(a), func(b)), num_points_per_experiment)

        points_under_curve = np.sum([is_point_below_line(
            func, x, y) for x, y in zip(x_values, y_values)])
        ratio_under_curve = points_under_curve / num_points_per_experiment
        integral_estimate = ratio_under_curve * (b - a) * max(func(a), func(b))

        total_integral_estimate += integral_estimate

    return total_integral_estimate / num_experiments


def calculate_integral(func, a, b):
    """To check the value of the integral given the integration limits"""
    result, error = spi.quad(func, a, b)

    return result


def main():
    # Defining the function and integration boundary
    a = 0  # Lower bound
    b = 2  # Upper bound
    estimated_area = monte_carlo_simulation(f, a, b)
    print("Estimated area under the curve: ", estimated_area)
    integral_value = calculate_integral(f, a, b)
    print("Value of the integral: ", integral_value)

    # Checking if the estimated area is close to the integral value
    is_close = round(estimated_area, 2) == round(integral_value, 2)
    print("Is the estimated area close to the integral value? ", is_close)  
    draw_function(a, b)


if __name__ == "__main__":
    main()
