"""
https://leetcode.com/problems/robot-bounded-in-circle/
"""


def robot(instructions):
    # start robot not facing in X direction and make it face Y direction forward
    dirX, dirY = 0, 1
    # position at (0, 0)
    posX, posY = 0, 0

    # loop through string
    for i in instructions:
        if i == "G":
            # we have to move the robot in whatever direction it is facing and add it to wherever it is in position
            posX, posY, = (
                posX + dirX,
                posY + dirY,
            )
        elif i == "L":
            # we would never to swap the values because they can never not have at least one value that is 0
            # we need to multiply by negative 1 to get that left direction because left is -1
            dirX, dirY = -1 * dirY, dirX
        elif i == "R":
            # we would have to negate the negative X direction (left) and make it position and face it up
            dirX, dirY = dirY, -1 * dirX
    # if the position is back at the origin or if the direciton is not NOT chagned, we can say the robot is truly bouded in a circle
    return (posX, posY) == (0, 0) or (dirX, dirY) != (0, 1)


# test
print(robot("GGLLGGLL"))
