from rlbot.utils.structures.game_data_struct import GameTickPacket
from rlbot.agents.base_agent import BaseAgent, SimpleControllerState
from rlbot.messages.flat.QuickChatSelection import QuickChatSelection
from util.grid.Grid import Grid
from util.sequence import Sequence, ControlStep
from util.situations.kickoff.center_back import center_back_kickoff
from util.situations.kickoff.center_left import center_left_kickoff
from util.situations.kickoff.center_right import center_right_kickoff
from util.situations.kickoff.diagonal import diagonal_kickoff
from util.situations.kickoff.KickOffOptions import KickOffOptions

def kickoff(baseAgent: BaseAgent, packet: GameTickPacket, grid: Grid, team_index: int) -> Sequence:
    kickoff_options: KickOffOptions = KickOffOptions(team_index)
    if grid.ownposition.equals_kickoff(kickoff_options.diagonal_left) or grid.ownposition.equals_kickoff(kickoff_options.diagonal_right):
        return diagonal_kickoff(baseAgent)
    elif grid.ownposition.equals_kickoff(kickoff_options.center_left):
        return center_left_kickoff(baseAgent, grid, kickoff_options)
    elif grid.ownposition.equals_kickoff(kickoff_options.center_right):
        return center_right_kickoff(baseAgent, grid, kickoff_options)
    elif grid.ownposition.equals_kickoff(kickoff_options.center_back):
        return center_back_kickoff(baseAgent, grid, kickoff_options)


    baseAgent.send_quick_chat(team_only=False, quick_chat=QuickChatSelection.Information_IGotIt)
    return Sequence([
        ControlStep(duration=0.05, controls=SimpleControllerState(throttle=1.0))
    ])
