from util.situations.kickoff.KickoffPosition import KickOffPosition

class KickOffOptions:

    def __init__(self, teamid: int):
        if(teamid == 1):
            self.diagonal_left = KickOffPosition(-2048, 2560)
            self.diagonal_right = KickOffPosition(2048, 2560)
            self.center_left = KickOffPosition(-256, 3840)
            self.center_right = KickOffPosition(256, 3840)
            self.center_back = KickOffPosition(0, 4608)
        else:
            self.diagonal_left = KickOffPosition(2048, -2560)
            self.diagonal_right = KickOffPosition(-2048, -2560)
            self.center_left = KickOffPosition(256, -3840)
            self.center_right = KickOffPosition(-256, -3840)
            self.center_back = KickOffPosition(-0, -4608)
