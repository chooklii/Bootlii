from rlbot.agents.base_agent import BaseAgent
from util.sequence import Sequence, ControlStep
from rlbot.agents.base_agent import SimpleControllerState
from rlbot.messages.flat.QuickChatSelection import QuickChatSelection
from util.grid.Grid import Grid
from util.situations.kickoff.KickOffOptions import KickOffOptions

def center_back_kickoff(baseAgent: BaseAgent, grid: Grid, kickoff_options: KickOffOptions) -> Sequence:
    if grid.team.kickoff_position_used_by_team(kickoff_options.center_left) or grid.team.kickoff_position_used_by_team(kickoff_options.center_right):
        # if any of both positions in front of us is used, go for boost
        baseAgent.send_quick_chat(team_only=True, quick_chat=QuickChatSelection.Information_GoForIt)
        return center_back_go_for_boost()
    elif grid.team.kickoff_position_used_by_team(kickoff_options.diagonal_left) or grid.team.kickoff_position_used_by_team(kickoff_options.diagonal_right):
        # if any of the diagonal positions is used, also go for boost
        baseAgent.send_quick_chat(team_only=True, quick_chat=QuickChatSelection.Information_AllYours)
        return center_back_go_for_boost()
    else:
        # if we are alone on the field, go for ball
        return center_back_go_for_ball()

def center_back_go_for_boost():
    return Sequence([
        ControlStep(duration=0.05, controls=SimpleControllerState(throttle=1.0))
    ])

def center_back_go_for_ball():
    return Sequence([
        ControlStep(duration=0.05, controls=SimpleControllerState(throttle=1.0))
    ])