from util.sequence import Sequence, ControlStep
from rlbot.agents.base_agent import SimpleControllerState

def halfFlip() -> Sequence:
    return Sequence([
        ControlStep(duration=0.75, controls=SimpleControllerState(throttle=-1)),
        ControlStep(duration=0.25, controls=SimpleControllerState(jump=True)),
        ControlStep(duration=0.05, controls=SimpleControllerState(jump=False)),
        ControlStep(duration=0.2, controls=SimpleControllerState(jump=True, pitch=1)),
        ControlStep(duration=0.5, controls=SimpleControllerState(pitch=-1)),
        ControlStep(duration=0.25, controls=SimpleControllerState(roll=-1)),
        ControlStep(duration=0.25, controls=SimpleControllerState(roll=1))
    ])