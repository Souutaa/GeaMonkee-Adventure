from entities.Enemy import Enemy


class SlimeGreen(Enemy):
    def __init__(self):

        # Set up parent class
        super().__init__("slimeGreen")
        self.health = 50
        self.points = 20