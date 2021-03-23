from rlbot.agents.base_agent import BaseAgent, SimpleControllerState
from rlbot.messages.flat.QuickChatSelection import QuickChatSelection
from rlbot.utils.structures.game_data_struct import GameTickPacket

from util.ball_prediction_analysis import find_slice_at_time
from util.boost_pad_tracker import BoostPadTracker
from util.drive import steer_toward_target
from util.sequence import Sequence, ControlStep
from util.vec import Vec3
from util.grid.locationDetection import update_positions
from util.grid.Grid import Grid
from util.rotation import rotation
from util.situations.kickoff.kickoff import kickoff

"""
0 -> blue
1 -> orange
"""
class MyBot(BaseAgent):

    def __init__(self, name, team, index):
        super().__init__(name, team, index)
        self.active_sequence: Sequence = Sequence().set_empty()
        self.boost_pad_tracker = BoostPadTracker()
        self.location_grid = Grid()
        self.kickoff_mode = True
        self.last_reset_time = None

    def initialize_agent(self):
        # Set up information about the boost pads now that the game is active and the info is available
        self.boost_pad_tracker.initialize_boosts(self.get_field_info())

    def reset_to_start(self, packet):
        # reset some parameters back to start
        self.kickoff_mode = False
        self.last_reset_time = packet.game_info.game_time_remaining
        self.active_sequence = Sequence()

    def get_output(self, packet: GameTickPacket) -> SimpleControllerState:
        # Keep our boost pad info updated with which pads are currently active
        self.boost_pad_tracker.update_boost_status(packet)
        # Keep our grid system updates with all players current position
        self.location_grid = update_positions(packet, self.team, self.index)
        my_car = packet.game_cars[self.index]
        ball_location = Vec3(packet.game_ball.physics.location)

        # if we have not init a kickoff and it is kickoff time init a kickoff
        if not self.kickoff_mode:
            self.kickoff_mode = True
            self.active_sequence = kickoff(self, packet, self.location_grid, self.team)
        # if we are currently in a state like goal replay we return empty and reset some parameters back to default
        if not packet.game_info.is_round_active and self.last_reset_time != packet.game_info.game_time_remaining:
            self.reset_to_start(packet)
        if not packet.game_info.is_round_active:
            return SimpleControllerState()

        # if their is an active sequence of play given, return this
        if self.active_sequence is not None and not self.active_sequence.done:
            controls = self.active_sequence.tick(packet)
            if controls is not None:
                return controls
        else:
            controls = SimpleControllerState()



            #controls = rotation(controls, self.location_grid, my_car, ball_location, self.team)


        return controls
