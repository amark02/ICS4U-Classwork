import math
import random
import arcade


class Sprite: # A sprite class takes an x and y location
    def __init__(self, x: int, y: int, x_speed: int = 0, y_speed: int = 0):
        self.x = x
        self.y = y
        self.x_speed = x_speed
        self.y_speed = y_speed
        self.size = 25

    def draw(self):
        arcade.draw_circle_filled(self.x, self.y, self.size, arcade.color.BLUE)

    def update(self):
        self.x += self.x_speed
        self.y += self.y_speed

        if self.x > WIDTH or self.x < 0:
            self.x_speed = -self.x_speed

        if self.y > HEIGHT or self.y < 0:
            self.y_speed = -self.y_speed

    def collides_with_point(self, x: int, y: int):
        a = self.x - x
        b = self.y - y
        distance = math.sqrt(a**2 + b**2)
        return distance < self.size

WIDTH = 640
HEIGHT = 480

window = arcade.open_window(WIDTH, HEIGHT, "My Arcade Game")

sprites = []
for _ in range(10):
    x = random.randrange(WIDTH)
    y = random.randrange(HEIGHT)
    x_speed = random.randrange(-5, 5)
    y_speed = random.randrange(-5, 5)
    s = Sprite(x, y, x_speed, y_speed)
    sprites.append(s)



def setup():
    arcade.set_background_color(arcade.color.WHITE)
    arcade.schedule(update, 1/60)
    arcade.run()


def update(delta_time):
    # usually you need to state the global variable (e.x. global player)
    #player.x += player.x_speed
    #player.y += player.y_speed
    #player.update()
    for sprite in sprites:
        sprite.update()


@window.event
def on_draw():
    arcade.start_render()
    # Draw in here...
    #player.draw()
    for sprite in sprites:
        sprite.draw()


@window.event
def on_key_press(key, modifiers):
    pass


@window.event
def on_key_release(key, modifiers):
    pass


@window.event
def on_mouse_press(x, y, button, modifiers):
    pass

arcade.Sprite()
@window.event
def on_mouse_motion(x, y, dx, dy):
    for sprite in sprites:
        if sprite.collides_with_point(x, y)
            sprite.x = random.randrange(WIDTH)
            sprite.y = random.randrange(HEIGHT)


if __name__ == '__main__':
    setup()