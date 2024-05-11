import arcade

from constants import *
import main as main


class MultiPlayerCompleteView(arcade.View):
    """Class to manage the game overview"""
    def __init__(self, high_score = 0, other_score = 0):
        super().__init__();
        self.high_score = high_score
        self.other_score = other_score
    def on_show(self):
        """Called when switching to this view"""
        arcade.set_background_color(arcade.color.BLACK)

    def on_draw(self):
        """Draw the game overview"""
        self.clear()
        arcade.draw_text(
            "Thanks for playing!",
            SCREEN_WIDTH / 2,\
            SCREEN_HEIGHT / 2 + 200,
            arcade.color.WHITE,
            30,
            anchor_x="center",
        )
        arcade.draw_text(
            "You completed Geamonkee Adventure!",
            SCREEN_WIDTH / 2,\
            SCREEN_HEIGHT / 2 + 100,
            arcade.color.WHITE,
            30,
            anchor_x="center",
        )
        arcade.draw_text(
            "High Score: " + str(self.high_score) + "," + str(self.other_score),
            SCREEN_WIDTH / 2,
            SCREEN_HEIGHT / 2 ,
            arcade.color.WHITE,
            30,
            anchor_x="center",
        )

        arcade.draw_text(
            "You Won" if self.high_score > self.other_score else "You Loose",
            SCREEN_WIDTH / 2,
            SCREEN_HEIGHT / 2 - 100,
            arcade.color.WHITE,
            30,
            anchor_x="center",
        )

        arcade.draw_text(
            "Click to return to main menu!",
            SCREEN_WIDTH / 2,
            SCREEN_HEIGHT / 2 - 200,
            arcade.color.WHITE,
            30,
            anchor_x="center",
        )
        

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        """Use a mouse press to advance to the 'game' view."""
        my_window = main.MainWindow()
        self.window.show_view(my_window)