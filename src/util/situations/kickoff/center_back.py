from util.sequence import Sequence, ControlStep
from rlbot.agents.base_agent import SimpleControllerState

def center_back_kickoff() -> Sequence:
    return Sequence([
        ControlStep(duration=0.05, controls=SimpleControllerState(throttle=1.0))
    ])