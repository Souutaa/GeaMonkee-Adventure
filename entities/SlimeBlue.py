from Enemy import Enemy


class SlimeBlue(Enemy):
    def __init__(self):

        # Set up parent class
        super().__init__("slimeBlue")
        self.health = 50
        self.points = 20
