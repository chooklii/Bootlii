from util.grid.PlayerPosition import PlayerPosition
from util.situations.kickoff.KickoffPosition import KickOffPosition

class Grid:

    def __init__(
        self,
        ball: int = 0,
        ownposition: PlayerPosition = PlayerPosition(0, 0, 0),
        team = [],
        opponent = []
        ):
        self.ball: int = ball
        self.ownposition: PlayerPosition = ownposition
        self.team: list(PlayerPosition) = team
        self.opponent: list(PlayerPosition) = opponent

    def add_team(self, position: PlayerPosition):
        self.team.append(position)

    def add_opponent(self, position: PlayerPosition):
        self.opponent.append(position)

    def update_own_position(self, position: PlayerPosition):
        self.ownposition = position

    def update_ball_position(self, position: int):
        self.ball = position

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
