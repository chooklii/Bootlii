from rlbot.utils.structures.game_data_struct import GameTickPacket
from rlbot.agents.base_agent import SimpleControllerState
from util.determin_location import LocationDetection
from util.drive import steer_toward_target
from util.vec import Vec3

def rotation(controls: SimpleControllerState, location_grid: LocationDetection, my_location, ball_location: Vec3, my_team: int) -> SimpleControllerState:

        gridTeamCoordinates = {
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

        # if ball is in front of our goal drive towards it no mather what.
        if(location_grid.ball == 12 or location_grid.ball == 13):
            controls.steer = steer_toward_target(my_location, ball_location)
            controls.throttle = 1.0
        # if a teammate is in same grid element as the ball right now position center behind him
        if(location_grid.ball in location_grid.team):
            # position ist ungerade -> positionieren uns in der x2 Box
            if(location_grid.ball % 2):
                first_digit = repr(location_grid.ball)[0]
                new_position = first_digit + "2"
                if(first_digit == 1):
                    new_position = 12
                grid_position = Vec3(gridTeamCoordinates[my_team][int(new_position)]["x"], gridTeamCoordinates[my_team][int(new_position)]["y"])
                controls.steer = steer_toward_target(my_location, grid_position)
                controls.throttle = 1.0
            # position ist gerade, positionieren uns in der x3 box
            else:
                first_digit = repr(location_grid.ball)[0]
                new_position = first_digit + "3"
                if(first_digit == 1):
                    new_position = 13
                grid_position = Vec3(gridTeamCoordinates[my_team][int(new_position)]["x"], gridTeamCoordinates[my_team][int(new_position)]["y"])
                controls.steer = steer_toward_target(my_location, grid_position)
                controls.throttle = 1.0



        # Wer ist im Angriff?

        # Wenn wir, muss ich den Ball spielen?

        # Wenn wir, muss ich absichern?

        # Wenn wir, muss ich in die Box?

        # Wenn wir, muss ich raustorieren?


        # Wenn nicht wir, muss ich auf den Ball?

        # wenn nicht wir, muss ich ins Tor?
        return controls