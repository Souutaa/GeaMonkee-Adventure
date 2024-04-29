
import arcade
import arcade.gui

from constants import *
from views.game import GameView
from views.menu import MenuView


class QuitButton(arcade.gui.UIFlatButton):
    def on_click(self, event: arcade.gui.UIOnClickEvent):
        arcade.exit()


class MyWindow(arcade.View):
    def __init__(self):
        # --- Required for all code that uses UI element,
        # a UIManager to handle the UI.
        super().__init__()
        self.manager = arcade.gui.UIManager()
        self.manager.enable()
        imgPath = ASSETS_PATH / 'images' / 'MainMenuBackground'
        self.backgroundImg = arcade.load_texture(imgPath / f'Main.jpg')
        # Set background color
        arcade.set_background_color(arcade.color.DARK_BLUE_GRAY)

        # Create a vertical BoxGroup to align buttons
        self.v_box = arcade.gui.UIBoxLayout()

        # Create the buttons
        start_button = arcade.gui.UIFlatButton(text="Start Game", width=200)
        self.v_box.add(start_button.with_space_around(bottom=20))

        tutorial_button = arcade.gui.UIFlatButton(text="Tutorial", width=200)
        self.v_box.add(tutorial_button.with_space_around(bottom=20))

        # Again, method 1. Use a child class to handle events.
        quit_button = QuitButton(text="Quit", width=200)
        self.v_box.add(quit_button)

        # --- Method 2 for handling click events,
        # assign self.on_click_start as callback
        start_button.on_click = self.on_click_start

        # --- Method 3 for handling click events,
        # use a decorator to handle on_click events
        @tutorial_button.event("on_click")
        def on_click_tutorial(event):
            self.manager.disable()
            menu_view = MenuView()
            self.window.show_view(menu_view)

        # Create a widget to hold the v_box widget, that will center the buttons
        self.manager.add(
            arcade.gui.UIAnchorWidget(
                anchor_x="center_x",
                anchor_y="center_y",
                child=self.v_box)
        )

    def on_click_start(self, event):
        self.manager.disable()
        game_view = GameView()
        self.window.show_view(game_view)

    def on_draw(self):
        self.clear()
        arcade.draw_texture_rectangle(
            center_x=SCREEN_WIDTH / 2,
            center_y=SCREEN_HEIGHT / 2,
            width=SCREEN_WIDTH,
            height=SCREEN_HEIGHT,
            texture=self.backgroundImg
        )
        self.manager.draw()


def main():
    window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    game_start = MyWindow()
    window.show_view(game_start)
    arcade.run()


if __name__ == "__main__":
    main()
