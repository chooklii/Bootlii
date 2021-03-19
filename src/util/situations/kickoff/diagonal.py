from rlbot.agents.base_agent import BaseAgent
from rlbot.agents.base_agent import SimpleControllerState
from rlbot.messages.flat.QuickChatSelection import QuickChatSelection
from util.moves.speedFlip import speedFlip
from util.sequence import Sequence, ControlStep


def diagonal_kickoff(baseAgent: BaseAgent) -> Sequence:
    # if we are at the diagonal kickoff position we always go for ball no matter what
    baseAgent.send_quick_chat(team_only=True, quick_chat=QuickChatSelection.Information_IGotIt)
    return speedFlip()