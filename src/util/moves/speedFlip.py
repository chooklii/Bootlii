from util.sequence import Sequence, ControlStep
from rlbot.agents.base_agent import SimpleControllerState

def speedFlip() -> Sequence:
    return Sequence([
        ControlStep(duration= 0.1, controls=SimpleControllerState(throttle= 1.0, jump= True, pitch= 1.0)),
        ControlStep(duration= 0.1, controls=SimpleControllerState(throttle= 1.0, jump= False, pitch= 1.0)),
        ControlStep(duration= 0.05, controls=SimpleControllerState(throttle= 1.0, jump= True, pitch= -1.0, roll= -0.3)),
        ControlStep(duration= 0.2, controls=SimpleControllerState(throttle= 1.0, jump= False, pitch= -1.0, roll= -1.0, yaw= -1.0))
    ])