from util.situations.kickoff.KickoffPosition import KickOffPosition

class PlayerPosition:

    def __init__(self, x: int, y: int, grid: int, boost: int, driving_to_ball: bool, driving_away_from_ball: bool):
        self.x = x
        self.y = y
        self.grid = grid
        self.boost = boost
        self.driving_to_ball = driving_to_ball
        self.driving_away_from_ball = driving_away_from_ball

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_grid(self):
        return self.grid

    def get_boost(self):
        return self.boost

    def get_driving_to_ball(self):
        return self.driving_to_ball

    def get_driving_away_from_ball(self):
        return self.driving_away_from_ball

    def set_x(self, x: int):
        self.x = x

    def set_y(self, y: int):
        self.y = y

    def set_grid(self, grid: int):
        self.grid = grid

    def set_boost(self, boost: int):
        self.boost = boost

    def set_driving_to_ball(self, driving_to_ball: bool):
        self.driving_to_ball = driving_to_ball

    def set_driving_away_from_ball(self, driving_away_from_ball: bool):
        self.driving_away_from_ball = driving_away_from_ball

    # check if player is in given kickoff position
    def equals_kickoff(self, kickoff_position: KickOffPosition):
        return self.x == kickoff_position.get_x() and self.y == kickoff_position.get_y()
