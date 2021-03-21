from rlbot.agents.base_agent import BaseAgent
from util.sequence import Sequence, ControlStep
from rlbot.agents.base_agent import SimpleControllerState
from rlbot.messages.flat.QuickChatSelection import QuickChatSelection
from util.grid.Grid import Grid
from util.situations.kickoff.KickOffOptions import KickOffOptions

def center_left_kickoff(baseAgent: BaseAgent, grid: Grid, kickoff_options: KickOffOptions) -> Sequence:
    if grid.kickoff_position_used_by_team(kickoff_options.diagonal_left) or grid.kickoff_position_used_by_team(kickoff_options.diagonal_right):
        # if a player is positioned diagonal we asume they are going for the ball and cheat up a little bit
        return center_left_cheat_up()
    else:
        # if no player is in those upper positions we need to go for the ball
        baseAgent.send_quick_chat(team_only=True, quick_chat=QuickChatSelection.Information_IGotIt)
        return center_left_go_for_ball()


def center_left_go_for_ball():
    return Sequence([
        ControlStep(duration=0.65, controls=SimpleControllerState(throttle=1.0, boost=True, steer=0.05)),
        ControlStep(duration= 0.05, controls=SimpleControllerState(throttle= 1.0, boost=True, jump=True)),
        ControlStep(duration= 0.05, controls=SimpleControllerState(throttle= 1.0, boost=True, jump=True)),
        ControlStep(duration= 0.1, controls=SimpleControllerState(throttle= 1.0, boost=True, jump=False, pitch= 1.0)),
        ControlStep(duration= 0.05, controls=SimpleControllerState(throttle= 1.0, jump= True, pitch= -1.0)),
        ControlStep(duration= 0.2, controls=SimpleControllerState(throttle= 1.0, boost=True, jump= False, pitch= -1.0,yaw= -1.0))
    ])

def center_left_cheat_up():
    return Sequence([
        ControlStep(duration=2, controls=SimpleControllerState(throttle=1.0))
    ])
