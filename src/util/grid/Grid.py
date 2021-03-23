from util.grid.PlayerPosition import PlayerPosition
from util.situations.kickoff.KickoffPosition import KickOffPosition
from util.grid.Ball import Ball
class Grid:

    def __init__(
        self,
        ball: Ball,
        ownposition: PlayerPosition,
        team: list(PlayerPosition),
        opponent: list(PlayerPosition)
        ):
        self.ball = ball
        self.ownposition = ownposition
        self.team = team
        self.opponent = opponent

    def add_team(self, position: PlayerPosition):
        self.team.append(position)

    def add_opponent(self, position: PlayerPosition):
        self.opponent.append(position)

    def update_own_position(self, position: PlayerPosition):
        self.ownposition = position

    def update_ball_position(self, ball: Ball):
        self.ball = ball

    def reset_team(self):
        self.team = []

    def reset_opponent(self):
        self.opponent = []

    # return boolean depending on if own team is using kickoff position
    def kickoff_position_used_by_team(self, kickoff_position: KickOffPosition) -> bool:
        for single_player in self.team:
            if single_player.equals_kickoff(kickoff_position):
                return True
        return False
