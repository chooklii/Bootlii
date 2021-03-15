from rlbot.utils.structures.game_data_struct import GameTickPacket
from util.config.grid import gridTeamPositions

class LocationDetection:

    def __init__(self):
        self.ball: int = 0
        self.ownposition: int = 0
        self.team: list[int] = []
        self.opponent: list[int] = []

    def update_positions(self, packet: GameTickPacket, own_team: int, own_index: int):
        # update all players positions
        list_index = 0
        self.team = []
        self.opponent = []
        for list_index in range(len(packet.game_cars)):
            grid_position = self.determinGrid(packet.game_cars[list_index].physics.location.x, packet.game_cars[list_index].physics.location.y, own_team)
            if(list_index == own_index):
                self.ownposition = grid_position
            if(packet.game_cars[list_index].team != own_team):
                self.opponent.append(grid_position)
            else:
                self.team.append(grid_position)
            list_index+=1

        # update the position of the ball
        self.ball = self.determinGrid(packet.game_ball.physics.location.x, packet.game_ball.physics.location.y, own_team)




    def determinGrid(self, x, y, own_team: int) -> int:
        indexList = gridTeamPositions[own_team]
        if(x < 0):
            if(y < 0):
                if(y < -2560):
                    if(x < -2048):
                        return indexList[33]
                    else:
                        return indexList[34]
                else:
                    if(x < -2048):
                        return indexList[43]
                    else:
                        return indexList[44]
            else:
                if(y > 2560):
                    if(x < -2048):
                        return indexList[14]
                    else:
                        return indexList[13]
                else:
                    if(x < -2048):
                        return indexList[24]
                    else:
                        return indexList[23]

        else:
            if(y < 0):
                if(y < -2560):
                    if(x > 2048):
                        return indexList[31]
                    else:
                        return indexList[32]
                else:
                    if(x > 2048):
                        return indexList[41]
                    else:
                        return indexList[42]
            else:
                if(y > 2560):
                    if(x > 2048):
                        return indexList[11]
                    else:
                        return indexList[12]
                else:
                    if(x > 2048):
                        return indexList[21]
                    else:
                        return indexList[22]
