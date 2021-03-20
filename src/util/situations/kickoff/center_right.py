from rlbot.agents.base_agent import BaseAgent
from util.sequence import Sequence, ControlStep
from rlbot.agents.base_agent import SimpleControllerState
from rlbot.messages.flat.QuickChatSelection import QuickChatSelection
from util.grid.Grid import Grid
from util.situations.kickoff.KickOffOptions import KickOffOptions

def center_right_kickoff(baseAgent: BaseAgent, grid: Grid, kickoff_options: KickOffOptions) -> Sequence:
    if grid.kickoff_position_used_by_team(kickoff_options.diagonal_left) or grid.kickoff_position_used_by_team(kickoff_options.diagonal_right):
        # if a player is positioned diagonal we asume they are going for the ball
        if grid.kickoff_position_used_by_team(kickoff_options.center_left):
            # if center left is used, we go for boost
            return center_right_go_for_boost()
        # else we go for ball
        return center_right_cheat_up()
    elif grid.kickoff_position_used_by_team(kickoff_options.center_left):
        # if their is a player to the left of us -> left drives rule nr. 2
        baseAgent.send_quick_chat(team_only=True, quick_chat=QuickChatSelection.Information_GoForIt)
        return center_right_go_for_boost()
    else:
        # if no player is in those upper positions we need to go for the ball
        baseAgent.send_quick_chat(team_only=True, quick_chat=QuickChatSelection.Information_IGotIt)
        return center_right_go_for_ball()



def center_right_go_for_boost():
    return Sequence([
        ControlStep(duration=0.4, controls=SimpleControllerState(throttle=1.0, steer=1)),
        ControlStep(duration=0.4, controls=SimpleControllerState(throttle=1.0)),
        ControlStep(duration=0.4, controls=SimpleControllerState(throttle=1.0, jump=True, pitch=-1))
    ])

def center_right_go_for_ball():
    return Sequence([
        ControlStep(duration=0.65, controls=SimpleControllerState(throttle=1.0, boost=True, steer=-0.01)),
        ControlStep(duration= 0.05, controls=SimpleControllerState(throttle= 1.0, boost=True, jump= True)),
        ControlStep(duration= 0.05, controls=SimpleControllerState(throttle= 1.0, boost=True, jump= True)),
    ])

def center_right_cheat_up():
    return Sequence([
        ControlStep(duration=0.2, controls=SimpleControllerState(throttle=1.0))
    ])
