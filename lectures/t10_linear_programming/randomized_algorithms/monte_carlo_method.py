import random


def is_inside(a, b, x, y):
    """Checking if the point is inside the triangle."""
    return y <= (b / a) * x


def monte_carlo_simulation(a, b, num_experiments):
    average_area = 0

    for _ in range(num_experiments):
        # generate random points
        points = [(random.uniform(0, a), random.uniform(0, b)) for _ in range(15000)]
        # choosing the points inside the triangle
        inside_points = [point for point in points if is_inside(a, b, point[0], point[1])]

        # calculating the area
        m = len(inside_points)
        n = len(points)
        area = (m / n) * (a * b)

        # adding the area to the average
        average_area += area

    # averaging the area
    average_area /= num_experiments
    return average_area


if __name__ == "__main__":
    # rectangular size
    a = 10  # rectangular width
    b = 5  # rectangular height
    S = (a * b) / 2  # theoretical area

    # number of experiments
    num_experiments = 100

    average_area = monte_carlo_simulation(a, b, num_experiments)
    print(f"Theoretically calculated area: {S}")
    print(f"Average area calculated with {num_experiments} experiments: {average_area}")
