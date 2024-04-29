
from entities.Enemy import Enemy

class Fly(Enemy):
    def __init__(self):

        # Set up parent class
        super().__init__("fly", 0.5)
        self.health = 50
        self.points = 30
