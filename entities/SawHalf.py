from entities.Enemy import Enemy


class SawHalf(Enemy):
    def __init__(self):

        # Set up parent class
        super().__init__("sawHalf")
        self.health = 50
