from rlbot.agents.base_agent import BaseAgent
from rlbot.agents.base_agent import SimpleControllerState
from rlbot.messages.flat.QuickChatSelection import QuickChatSelection
from util.moves.halfFlip import halfFlip
from util.sequence import Sequence, ControlStep
from util.grid.Grid import Grid
from util.situations.kickoff.KickOffOptions import KickOffOptions

def diagonal_kickoff(baseAgent: BaseAgent, grid:Grid, kickoff_options: KickOffOptions) -> Sequence:
    # if we are at the diagonal kickoff position we always go for ball no matter what
    baseAgent.send_quick_chat(team_only=True, quick_chat=QuickChatSelection.Information_IGotIt)
    if grid.ownposition.equals_kickoff(kickoff_options.diagonal_left):
        return diagonal_left_go_for_ball()
    else:
        return diagonal_right_go_for_ball()

def diagonal_left_go_for_ball() -> Sequence:
    return Sequence([
        ControlStep(duration=0.65, controls=SimpleControllerState(throttle=1.0, boost=True, steer=-0.03)),
        ControlStep(duration= 0.05, controls=SimpleControllerState(throttle= 1.0, boost=True, jump= True)),
        ControlStep(duration= 0.05, controls=SimpleControllerState(throttle= 1.0, boost=True, jump= True)),
        ControlStep(duration= 0.1, controls=SimpleControllerState(throttle= 1.0, boost=True, jump= False, pitch= 1.0)),
        ControlStep(duration= 0.05, controls=SimpleControllerState(throttle= 1.0, jump= True, pitch= -1.0, roll= -0.3)),
        ControlStep(duration= 0.2, controls=SimpleControllerState(throttle= 1.0, boost=True, jump= False, pitch= -1.0, roll= -1.0, yaw= -1.0))
    ])

def diagonal_right_go_for_ball() -> Sequence:
    return Sequence([
        ControlStep(duration=0.65, controls=SimpleControllerState(throttle=1.0, boost=True, steer=0.03)),
        ControlStep(duration= 0.05, controls=SimpleControllerState(throttle= 1.0, boost=True, jump= True)),
        ControlStep(duration= 0.05, controls=SimpleControllerState(throttle= 1.0, boost=True, jump= True)),
        ControlStep(duration= 0.1, controls=SimpleControllerState(throttle= 1.0, boost=True, jump= False, pitch= 1.0)),
        ControlStep(duration= 0.05, controls=SimpleControllerState(throttle= 1.0, jump= True, pitch= -1.0, roll= 0.3)),
        ControlStep(duration= 0.2, controls=SimpleControllerState(throttle= 1.0, boost=True, jump= False, pitch= -1.0, roll= 1.0, yaw= 1.0))
    ])