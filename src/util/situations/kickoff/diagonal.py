from util.moves.speedFlip import speedFlip
from rlbot.agents.base_agent import BaseAgent
from util.sequence import Sequence, ControlStep
from rlbot.agents.base_agent import SimpleControllerState
from rlbot.messages.flat.QuickChatSelection import QuickChatSelection

def diagonal_kickoff(baseAgent: BaseAgent) -> Sequence:
    baseAgent.send_quick_chat(team_only=True, quick_chat=QuickChatSelection.Information_IGotIt)
    return speedFlip()