class Positioning: 
    """
    determin position of player and ball on the
    field based on a 16 grids system
    """


def determinGrid(x, y) -> int:
    if(x < 0):
        if(y < 0):
            if(y < -2560):
                if(x < -2048):
                    return 11
                else:
                    return 12
            else: 
                if(x < -2048):
                    return 15
                else:
                    return 16
        else:
            if(y > 2560):
                if(x < -2048):
                    return 4
                else:
                    return 3
            else: 
                if(x < -2048):
                    return 8
                else:
                    return 7

    else:
        if(y < 0):
            return 1
        else:
            return 2


