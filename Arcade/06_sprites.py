import arcade

WIDTH = 800
HEIGHT = 600


class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        arcade.set_background_color(arcade.color.WHITE)

        self.sprite1 = arcade.Sprite(center_x=100, center_y=200)
        self.sprite1.texture = arcade.make_soft_square_texture(50, arcade.color.BLACK, outer_alpha=255)
        self.sprite1.change_x = 3

        # add a sprite2
        # give it a texture (Blue)
        # place it at the opposite end of the screen
        # draw in draw

        self.sprite2 = arcade.Sprite(center_x=700, center_y=200)
        self.sprite2.texture = arcade.make_soft_square_texture(30, arcade.color.BLUE, outer_alpha=255)

    def on_draw(self):
        arcade.start_render()  # keep as first line

        # Draw everything below here.
        self.sprite1.draw()
        self.sprite2.draw()

    def update(self, delta_time):
        self.sprite1.update()
        self.sprite2.update()
        if self.sprite1.collides_with_sprite(self.sprite2):
            print("COLLIDING")
            # change size of a particular sprite
            # make one vanish
            # bounce the black one back
            # change the color

        # on mouse press
            # create a new sprite at the original black location
            # give it a velocity to the left
            # requires a sprite list to be made

def main():
    game = MyGame(WIDTH, HEIGHT, "My Game")
    arcade.run()


if __name__ == "__main__":
    main()
