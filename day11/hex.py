"""
--- Day 11: Hex Ed ---

Crossing the bridge, you've barely reached the other side of the stream when a program comes up to you, clearly in distress. "It's my child process," she says, "he's gotten lost in an infinite grid!"

Fortunately for her, you have plenty of experience with infinite grids.

Unfortunately for you, it's a hex grid.

The hexagons ("hexes") in this grid are aligned such that adjacent hexes can be found to the north, northeast, southeast, south, southwest, and northwest:

  \ n  /
nw +--+ ne
  /    \
-+      +-
  \    /
sw +--+ se
  / s  \
You have the path the child process took. Starting where he started, you need to determine the fewest number of steps required to reach him. (A "step" means to move from the hex you are in to any adjacent hex.)

For example:

ne,ne,ne is 3 steps away.
ne,ne,sw,sw is 0 steps away (back where you started).
ne,ne,s,s is 2 steps away (se,se).
se,sw,se,sw,sw is 3 steps away (s,s,sw).
"""


def getInput(path):
    file = open(path, "r")
    input = file.readlines().pop().split(",")
    return input


def partOne(input):
    # Row represents what row we are on if we consider lines cutting through SW to NE
    row = 0
    # Columns cut through the vertex between NW and N and S and SE
    column = 0
    # See explanation.png to see how grid is represented
    for direction in input:
        if direction == "sw":
            column -= 2
        elif direction == "ne":
            column += 2
        elif direction == "n":
            row += 1
            column += 1
        elif direction == "nw":
            row += 1
            column -= 1
        elif direction == "se":
            row -= 1
            column += 1
        elif direction == "s":
            row -= 1
            column -= 1
        # print(str(row) + "," + str(column))

    answer = abs(row / 2) + abs(column / 2)
    print(answer)
    return answer

def partTwo(input):
    # Row represents what row we are on if we consider lines cutting through SW to NE
    row = 0
    # Columns cut through the vertex between NW and N and S and SE
    column = 0
    # See explanation.png to see how grid is represented
    maxDistance = 0
    for direction in input:
        if direction == "sw":
            column -= 2
        elif direction == "ne":
            column += 2
        elif direction == "n":
            row += 1
            column += 1
        elif direction == "nw":
            row += 1
            column -= 1
        elif direction == "se":
            row -= 1
            column += 1
        elif direction == "s":
            row -= 1
            column -= 1
        distance = abs(row / 2) + abs(column / 2)
        maxDistance = max(maxDistance, distance)

    print(maxDistance)
    return maxDistance


assert(partOne(['ne', 'ne', 'ne']) == 3)
assert(partOne(['ne', 'ne', 'sw', 'sw']) == 0)
assert(partOne(['ne', 'ne', 's', 's']) == 2)
assert(partOne(['se', 'sw', 'se', 'sw', 'sw']) == 3)
partOne(getInput("day11/input"))
partTwo(getInput("day11/input"))