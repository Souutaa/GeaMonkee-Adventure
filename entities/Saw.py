from Enemy import Enemy


class Saw(Enemy):
    def __init__(self):

        # Set up parent class
        super().__init__("saw", 0.5)
        self.health = 9999999
