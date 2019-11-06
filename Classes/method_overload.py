
# Method overloading (Python version)

# optional/default parameters
# Key-word arguments

# Allows us to create one function or method with a variety of ways to call it


def draw_rectangle(x, y, w=100, h=100, color=arcade.color.BLUE):
    pass


draw_rectangle(50, 50) # draws rectangle at 50, 50 of width 100, height 100

draw_rectangle(x=100, y=50) # sets x to 100 and y to 50, draws rectangle at 100, 50

draw_rectangle(100, 200, 5)

draw_rectangle(500, 200, 50, 50)

draw_rectangle(10, 10, 5, 5, arcade.color.WHITE)

"""draw_rectangle(15, 5, arcade.color.WHITE) doesn't work"""

draw_rectangle(75, 10, color=arcade.color.WHITE) # third argument can only be color if you set the variable to a new color
