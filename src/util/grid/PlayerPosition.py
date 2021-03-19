from util.situations.kickoff.KickoffPosition import KickOffPosition

class PlayerPosition:

    def __init__(self, x: int, y: int, grid: int):
        self.x = x
        self.y = y
        self.grid = grid

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_grid(self):
        return self.grid

    def set_x(self, x: int):
        self.x = x

    def set_y(self, y: int):
        self.y = y

    def set_grid(self, grid: int):
        self.grid = grid

    # check if player is in given kickoff position
    def equals_kickoff(self, kickoff_position: KickOffPosition):
        return self.x == kickoff_position.get_x() and self.y == kickoff_position.get_y()
