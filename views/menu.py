import arcade

from constants import *


class MenuView(arcade.View):
    """Class that manages the 'menu' view."""
    def __init__(self):
        super().__init__()
        imgPath = ASSETS_PATH / 'images' / 'MainMenuBackground'
        self.backgroundImg = arcade.load_texture(imgPath / f'secondary.jpg')
    def on_show(self):
        """Called when switching to this view."""
        arcade.set_background_color(arcade.color.WHITE)

    def on_draw(self):
        """Draw the menu"""
        self.clear()
        arcade.draw_texture_rectangle(
            center_x= SCREEN_WIDTH / 2,
            center_y= SCREEN_HEIGHT / 2,
            width= SCREEN_WIDTH,
            height= SCREEN_HEIGHT,
            texture=self.backgroundImg
        )
        arcade.draw_text(
            "Main Menu - Click to play game",
            SCREEN_WIDTH / 2,
            SCREEN_HEIGHT / 2,
            arcade.color.BLACK,
            font_size=30,
            anchor_x="center",
        )
        
        arcade.draw_text(
            "Move: W, S, A, D",
            SCREEN_WIDTH / 2,
            SCREEN_HEIGHT / 2 - 40,
            arcade.color.BLACK,
            font_size=30,
            anchor_x="center",
        )
        
        arcade.draw_text(
            "Attack: SPACE",
            SCREEN_WIDTH / 2,
            SCREEN_HEIGHT / 2 - 80,
            arcade.color.BLACK,
            font_size=30,
            anchor_x="center",
        )
        


    def on_mouse_press(self, _x, _y, _button, _modifiers):
        """Use a mouse press to advance to the 'game' view."""
        game_view = GameView()
        self.window.show_view(game_view)