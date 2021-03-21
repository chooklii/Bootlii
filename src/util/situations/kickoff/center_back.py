from rlbot.agents.base_agent import BaseAgent
from util.sequence import Sequence, ControlStep
from rlbot.agents.base_agent import SimpleControllerState
from rlbot.messages.flat.QuickChatSelection import QuickChatSelection
from util.grid.Grid import Grid
from util.situations.kickoff.KickOffOptions import KickOffOptions

def center_back_kickoff(baseAgent: BaseAgent, grid: Grid, kickoff_options: KickOffOptions) -> Sequence:
    if grid.kickoff_position_used_by_team(kickoff_options.center_left) or grid.kickoff_position_used_by_team(kickoff_options.center_right):
        # if any of both positions in front of us is used, go for boost
        baseAgent.send_quick_chat(team_only=True, quick_chat=QuickChatSelection.Information_GoForIt)
        return center_back_go_for_boost()
    elif grid.kickoff_position_used_by_team(kickoff_options.diagonal_left) or grid.kickoff_position_used_by_team(kickoff_options.diagonal_right):
        # if any of the diagonal positions is used, also go for boost
        baseAgent.send_quick_chat(team_only=True, quick_chat=QuickChatSelection.Information_AllYours)
        return center_back_go_for_boost()
    else:
        # if we are alone on the field, go for ball
        return center_back_go_for_ball()

def center_back_go_for_boost():
    return Sequence([
        ControlStep(duration=0.7, controls=SimpleControllerState(throttle=1.0, steer=-1)),
        ControlStep(duration= 0.05, controls=SimpleControllerState(throttle= 1.0, boost=True)),
        ControlStep(duration= 0.05, controls=SimpleControllerState(throttle= 1.0, boost=True, jump=True)),
        ControlStep(duration= 0.05, controls=SimpleControllerState(boost=True, jump=False, pitch= 1.0)),
        ControlStep(duration= 0.05, controls=SimpleControllerState(jump= True, pitch= -1.0))
    ])

def center_back_go_for_ball():
    return Sequence([
        ControlStep(duration=0.65, controls=SimpleControllerState(throttle=1.0, boost=True)),
        ControlStep(duration= 0.05, controls=SimpleControllerState(throttle= 1.0, boost=True, jump=True)),
        ControlStep(duration= 0.05, controls=SimpleControllerState(throttle= 1.0, boost=True, jump=True)),
        ControlStep(duration= 0.1, controls=SimpleControllerState(throttle= 1.0, boost=True, jump=False, pitch= 1.0)),
        ControlStep(duration= 0.05, controls=SimpleControllerState(throttle= 1.0, jump= True, pitch= -1.0)),
        ControlStep(duration= 0.6, controls=SimpleControllerState(throttle= 1.0, boost=True, jump= False, pitch= -1.0,yaw= -1.0))
    ])