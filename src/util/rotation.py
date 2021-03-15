from rlbot.utils.structures.game_data_struct import GameTickPacket
from rlbot.agents.base_agent import SimpleControllerState
from util.determin_location import LocationDetection
from util.drive import steer_toward_target
from util.vec import Vec3
from util.config.grid import gridTeamPositions, gridTeamCoordinates, gridPositionLogic

def rotation(controls: SimpleControllerState, location_grid: LocationDetection, my_location, ball_location: Vec3, my_team: int) -> SimpleControllerState:
        # if ball is in front of our goal drive towards it no mather what.
        if(location_grid.ball == location_grid.ownposition):
            controls.steer = steer_toward_target(my_location, ball_location)
            controls.throttle = 1.0
        else:
            ball_position: int = location_grid.ball
            new_position: int = gridPositionLogic[ball_position]["backup"]
            print("Rotate towards", new_position)
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