import random


def draw_circle(x: int, y: int, radius: int=0):
    if radius is None:
        radius = random.randrange(50)
    print(f"Drawing cricle at {x}, {y}, with radius {radius}.")

draw_circle(50, 50)
draw_circle(100, 100)
draw_circle(200, 200, 75)
draw_circle(300, 300, 0)