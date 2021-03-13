from rlbot.utils.structures.game_data_struct import GameTickPacket

gridTeamPositions = {
    0: {
        11: 44,
        12: 43,
        13: 42,
        14: 41,
        21: 34,
        22: 33,
        23: 32,
        24: 31,
        31: 24,
        32: 23,
        33: 22,
        34: 21,
        41: 14,
        42: 13,
        43: 12,
        44: 11
    },
    1: {
        11: 11,
        12: 12,
        13: 13,
        14: 14,
        21: 21,
        22: 22,
        23: 23,
        24: 24,
        31: 31,
        32: 32,
        33: 33,
        34: 34,
        41: 41,
        42: 42,
        43: 43,
        44: 44
    }
}

gridTeamCoordinates: {
    0: {
        11: {"x": -3072, "y": -1280 },
        12: {"x": -1024, "y": -1280 },
        13: {"x": 1024,  "y": -1280 },
        14: {"x": 3072,  "y": -1280 },
        21: {"x": -3072, "y": -1280},
        22: {"x": -1024, "y": -1280 },
        23: {"x": 1024,  "y": -1280 },
        24: {"x": 3072,  "y": -1280 },
        31: {"x": -3072, "y": 1280 },
        32: {"x": -1024, "y": 1280 },
        33: {"x": 1024,  "y": 1280 },
        34: {"x": 3072,  "y": 1280 },
        41: {"x": -3072, "y": 3840 },
        42: {"x": -1024, "y": 3840},
        43: {"x": 1024,  "y": 3840 },
        44: {"x": 3072,  "y": 3840 }
    },
    1: {
        11: {"x": 3072,  "y": 3840 },
        12: {"x": 1024,  "y": 3840 },
        13: {"x": -1024, "y": 3840},
        14: {"x": -3072, "y": 3840 },
        21: {"x": 3072,  "y": 1280 },
        22: {"x": 1024,  "y": 1280 },
        23: {"x": -1024, "y": 1280 },
        24: {"x": -3072, "y": 1280 },
        31: {"x": 3072,  "y": -1280 },
        32: {"x": 1024,  "y": -1280 },
        33: {"x": -1024, "y": -1280 },
        34: {"x": -3072, "y": -1280},
        41: {"x": 3072,  "y": -1280 },
        42: {"x": 1024,  "y": -1280 },
        43: {"x": -1024, "y": -1280 },
        44: {"x": -3072, "y": -1280 }
    }
}

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





