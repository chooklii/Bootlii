from util.grid.PlayerPosition import PlayerPosition
from util.situations.kickoff.KickoffPosition import KickOffPosition

# check if given kickoff_position is used by and player from the list
def position_in_use(players: list[PlayerPosition], kickoff_position: KickOffPosition)-> bool:
    for player in players:
        if(players.get_x == kickoff_position.get_x and player.get_y == kickoff_position.get_y):
            return True
    return False