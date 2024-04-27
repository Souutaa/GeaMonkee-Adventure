import arcade

from constants import *
from utils import load_texture_pair


class Entity(arcade.Sprite):
    def __init__(self, name_file, custom_scale=1):
        super().__init__()
        # Default to facing right
        self.facing_direction = RIGHT_FACING

        # Used for image sequences
        self.cur_texture = 0
        self.scale = custom_scale
        self.character_face_direction = RIGHT_FACING

        # main_path = f":resources:images/animated_characters/{name_folder}/{name_file}"
        main_path = ASSETS_PATH / 'images' / 'Enemies'

        self.idle_texture_pair = load_texture_pair(
            main_path / f"{name_file}.png")

        # Load textures for walking
        self.walk_textures = []
        self.walk_textures.append(
            load_texture_pair(main_path / f"{name_file}.png"))
        self.walk_textures.append(load_texture_pair(
            main_path / f"{name_file}_move.png"))

        # Set the initial texture
        self.texture = self.idle_texture_pair[0]

        # Hit box will be set based on the first image used. If you want to specify
        # a different hit box, you can do it like the code below.
        # set_hit_box = [[-22, -64], [22, -64], [22, 28], [-22, 28]]
        self.hit_box = self.texture.hit_box_points
