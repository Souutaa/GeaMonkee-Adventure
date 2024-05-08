import arcade

from constants import *

import main as main


class GameOverView(arcade.View):
    """Class to manage the game overview"""
    def __init__(self, high_score = 0 ):
        super().__init__();
        self.high_score = high_score
        
        imgPath = ASSETS_PATH / 'images' / 'MainMenuBackground'
        self.backgroundImg = arcade.load_texture(imgPath / f'third.jpg')
    def on_show(self):
        """Called when switching to this view"""
        arcade.set_background_color(arcade.color.BLACK)

    def on_draw(self):
        """Draw the game overview"""
        self.clear()
        arcade.draw_texture_rectangle(
            center_x= SCREEN_WIDTH / 2,
            center_y= SCREEN_HEIGHT / 2,
            width= SCREEN_WIDTH,
            height= SCREEN_HEIGHT,
            texture=self.backgroundImg
        )
        arcade.draw_text(
            "Game Over",
            SCREEN_WIDTH / 2,\
            SCREEN_HEIGHT / 2 + 100,
            arcade.color.BLACK,
            30,
            anchor_x="center",
        )
        arcade.draw_text(
            "High Score: " + str(self.high_score),
            SCREEN_WIDTH / 2,
            SCREEN_HEIGHT / 2 ,
            arcade.color.BLACK,
            30,
            anchor_x="center",
        )

        arcade.draw_text(
            "Click to return to main menu!",
            SCREEN_WIDTH / 2,
            SCREEN_HEIGHT / 2 - 100,
            arcade.color.BLACK,
            30,
            anchor_x="center",
        )

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        """Use a mouse press to advance to the 'game' view."""
        my_window = main.MyWindow()
        self.window.show_view(my_window)
