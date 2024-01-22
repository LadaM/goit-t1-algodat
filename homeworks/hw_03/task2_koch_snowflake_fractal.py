import turtle


# Angle of rotation for each recursive call
ROTATION_DEGREES = 120  # divisible by 60 & 360 is divisible by this number (180 looks strange)
MAX_DEGREES = 360
BACKGROUND_COLOR = "navy"
SNOWFLAKE_COLOR = "lightblue"
TURTLE_SPEED = 0  # will move at max when set to 0

def koch_snowflake_recursive(turtle, order, size):
    if order == 0:
        turtle.forward(size)
    else:
        for angle in [ROTATION_DEGREES//2, -ROTATION_DEGREES, ROTATION_DEGREES//2, 0]:
            koch_snowflake_recursive(turtle, order - 1, size / (MAX_DEGREES // ROTATION_DEGREES))
            turtle.left(angle)

def draw_koch_snowflake_recursive(order, size, start_x=0, start_y=0):
    screen = turtle.Screen()
    screen.bgcolor(BACKGROUND_COLOR)
    
    fractal_turtle = turtle.Turtle()
    fractal_turtle.color(SNOWFLAKE_COLOR)
    fractal_turtle.speed(TURTLE_SPEED)
    fractal_turtle.hideturtle() # hiding the pointer 

    # placing the turtle in the initial position
    fractal_turtle.penup()
    fractal_turtle.goto(start_x, start_y)
    fractal_turtle.pendown()

    for _ in range(MAX_DEGREES//ROTATION_DEGREES):
        koch_snowflake_recursive(fractal_turtle, order, size)
        fractal_turtle.right(ROTATION_DEGREES)

    screen.exitonclick()

# Set the order of the fractal, the initial size of the triangle
# and the initial position of the turtle
order = 4 # more than 4 is very slow
initial_size = 400
start_x = -200
start_y = 125

draw_koch_snowflake_recursive(order, initial_size, start_x=start_x, start_y=start_y)
