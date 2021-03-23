from rlbot.utils.structures.game_data_struct import GameTickPacket
from util.grid.config import gridTeamPositions
from util.grid.Grid import Grid
from util.grid.PlayerPosition import PlayerPosition
from util.grid.Ball import Ball

def update_positions(packet: GameTickPacket, own_team: int, own_index: int) -> Grid:
    ball: Ball = init_ball(packet, own_team)
    grid = Grid(Ball, None, None, None)
    # update all players positions
    list_index = 0
    for list_index in range(len(packet.game_cars)):
        position_x = packet.game_cars[list_index].physics.location.x
        position_y = packet.game_cars[list_index].physics.location.y
        grid_position = determinGrid(position_x, position_y, own_team)
        boost = packet.game_cars[list_index].boost
        driving_to_ball = check_if_driving_to_ball()
        driving_away_from_ball = check_if_driving_away_from_ball()
        player_position = PlayerPosition(position_x, position_y, grid_position, boost, driving_to_ball, driving_away_from_ball)
        if(list_index == own_index):
            grid.update_own_position(player_position)
        elif(packet.game_cars[list_index].team != own_team):
            grid.add_opponent(player_position)
        else:
            grid.add_team(player_position)
        list_index+=1

    # update the position of the ball
    ball: int = determinGrid(packet.game_ball.physics.location.x, packet.game_ball.physics.location.y, own_team)
    grid.update_ball_position(ball)

    return grid

# check if given car is driving towards ball
def check_if_driving_to_ball():
    return False

# check if given car is driving away from ball
def check_if_driving_away_from_ball():
    return False

# init Ball
def init_ball(packet, own_team: int) -> Ball:
    ball: Ball = Ball(
        packet.game_ball.physics.location.x,
        packet.game_ball.physics.location.y,
        packet.game_ball.physics.location.z,
        packet.game_ball.physics.rotation.pitch,
        packet.game_ball.physics.rotation.yaw,
        packet.game_ball.physics.rotation.roll,
        packet.game_ball.physics.velocity.x,
        packet.game_ball.physics.velocity.y,
        packet.game_ball.physics.velocity.z,
        packet.game_ball.physics.angular_velocity.x,
        packet.game_ball.physics.angular_velocity.y,
        packet.game_ball.physics.angular_velocity.z,
        None,
        None,
        None,
        determinGrid(packet.game_ball.physics.location.x, packet.game_ball.physics.location.y, own_team)
    )
    ball.set_towards_neutral(check_if_ball_moving_neutral_way(ball))
    ball.set_towards_our_goal(check_if_ball_moving_our_way(ball))
    ball.set_towards_their_goal(check_if_ball_moving_opponent_way(ball))
    return ball

def check_if_ball_moving_our_way(ball: Ball) -> bool:
    return False

def check_if_ball_moving_opponent_way(ball: Ball) -> bool:
    return False

def check_if_ball_moving_neutral_way(ball: Ball) -> bool:
    return False

def determinGrid(x, y, own_team: int) -> int:
    indexList = gridTeamPositions[own_team]
    if(x < 0):
        if(y < 0):
            if(y < -2560):
                if(x < -2048):
                    return indexList[33]
                else:
                    return indexList[34]
            else:
                if(x < -2048):
                    return indexList[43]
                else:
                    return indexList[44]
        else:
            if(y > 2560):
                if(x < -2048):
                    return indexList[14]
                else:
                    return indexList[13]
            else:
                if(x < -2048):
                    return indexList[24]
                else:
                    return indexList[23]

    else:
        if(y < 0):
            if(y < -2560):
                if(x > 2048):
                    return indexList[31]
                else:
                    return indexList[32]
            else:
                if(x > 2048):
                    return indexList[41]
                else:
                    return indexList[42]
        else:
            if(y > 2560):
                if(x > 2048):
                    return indexList[11]
                else:
                    return indexList[12]
            else:
                if(x > 2048):
                    return indexList[21]
                else:
                    return indexList[22]
