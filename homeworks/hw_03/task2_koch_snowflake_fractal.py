import turtle


# Angle of rotation for each recursive call
ROTATION_DEGREES = (
    120  # divisible by 60 & 360 is divisible by this number (180 looks strange)
)
MAX_DEGREES = 360
BACKGROUND_COLOR = "navy"
SNOWFLAKE_COLOR = "lightblue"
TURTLE_SPEED = 0  # will move at max when set to 0
MIN_ORDER = 0
MAX_ORDER = 7


def koch_snowflake_recursive(fractal_turtle, order, size):
    if order == 0:
        fractal_turtle.forward(size)
    else:
        for angle in [
            ROTATION_DEGREES // 2,
            -ROTATION_DEGREES,
            ROTATION_DEGREES // 2,
            0,
        ]:
            koch_snowflake_recursive(
                fractal_turtle, order - 1, size / (MAX_DEGREES // ROTATION_DEGREES)
            )
            fractal_turtle.left(angle)


def draw_koch_snowflake_recursive(order, size, start_x=0, start_y=0):
    screen = turtle.Screen()
    screen.bgcolor(BACKGROUND_COLOR)

    fractal_turtle = turtle.Turtle()
    fractal_turtle.color(SNOWFLAKE_COLOR)
    fractal_turtle.speed(TURTLE_SPEED)
    fractal_turtle.hideturtle()  # hiding the pointer

    # placing the turtle in the initial position
    fractal_turtle.penup()
    fractal_turtle.goto(start_x, start_y)
    fractal_turtle.pendown()

    for _ in range(MAX_DEGREES // ROTATION_DEGREES):
        koch_snowflake_recursive(fractal_turtle, order, size)
        fractal_turtle.right(ROTATION_DEGREES)

    screen.exitonclick()


def main():
    default_order = 4  # more than 4 is very slow
    order_input = input("Enter the order of the fractal: ")
    order = None
    if order_input:
        try:
            order = int(order_input)
        except ValueError:
            print("Invalid input. Integer is expected.")
        finally:
            if not order:
                order = default_order
            elif order < MIN_ORDER:
                print(f"Order {order} is too low. Minimum order is {MIN_ORDER}")
                order = MIN_ORDER
            elif order > MAX_ORDER:
                print(f"Order {order} is too high. Maximum order is {MAX_ORDER}")
                order = MAX_ORDER
    else:
        order = default_order

    # Setting the initial size of the triangle and the initial position of the turtle
    initial_size = 400
    start_x = -200
    start_y = 125

    draw_koch_snowflake_recursive(order, initial_size, start_x=start_x, start_y=start_y)


if __name__ == "__main__":
    main()
