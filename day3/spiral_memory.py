# --- Day 3: Spiral Memory ---

# You come across an experimental new kind of memory stored on an infinite two-dimensional grid.

# Each square on the grid is allocated in a spiral pattern starting at a location marked 1 and then counting up while spiraling outward. For example, the first few squares are allocated like this:

# 17  16  15  14  13
# 18   5   4   3  12
# 19   6   1   2  11  ^
# 20   7   8   9  10  |
# 21  22  23  24  25 ->
# While this is very space-efficient (no squares are skipped), requested data must be carried back to square 1 (the location of the only access port for this memory system) by programs that can only move up, down, left, or right. They always take the shortest path: the Manhattan Distance between the location of the data and square 1.

# For example:

# Data from square 1 is carried 0 steps, since it's at the access port.
# Data from square 12 is carried 3 steps, such as: down, left, left.
# Data from square 23 is carried only 2 steps: up twice.
# Data from square 1024 must be carried 31 steps.
# How many steps are required to carry the data from the square identified in your puzzle input all the way to the access port?


def main(input):
    print("Input: " + str(input))
    if input == 1:
        return 0

    n = 1

    while pow(n + 2, 2) < input:
        n += 2

    # At this point, the input number must be on the boundaries of the spiral
    # Each side of the spiral has a range of n + 1
    # If n*n is the current perfect square at the bottom right, then
    # With 1 being the center of the cartesian plane at (0,0)
    # n*n + (n+1) is the value in coordinate (n+2 /2, n+2 /2), top right hand corner
    # n*n + 2(n+1) is the value in coordinate (-n+2 /2, n+2 /2), top left hand corner
    # n*n + 3(n+1) is the value in coordinate (-n+2 /2, -n+2 /2), top left hand corner
    # n*n + 4(n+1) will yield the next perfect square

    nSquared = pow(n, 2)
    TOP_RIGHT_VAL = nSquared + (n + 1)
    print("TOP_RIGHT_VAL " + str(TOP_RIGHT_VAL))
    TOP_LEFT_VAL = nSquared + 2 * (n + 1)
    print("TOP_LEFT_VAL " + str(TOP_LEFT_VAL))
    BOTTOM_LEFT_VAL = nSquared + 3 * (n + 1)
    print("BOTTOM_LEFT_VAL " + str(BOTTOM_LEFT_VAL))

    inputX = 0
    inputY = 0
    if input <= TOP_RIGHT_VAL:
        # Right border
        inputX = int((n + 2) / 2)
        inputY = int((-(n + 2) / 2)) + input - nSquared
    elif input <= TOP_LEFT_VAL:
        # Top border
        inputX = int((n + 2) / 2) - (input - TOP_RIGHT_VAL)
        inputY = int((n + 2) / 2)
    elif input <= BOTTOM_LEFT_VAL:
         # Left Border
        inputX = int(-(n + 2) / 2)
        inputY = int((n + 2) / 2) - (input - TOP_LEFT_VAL)
    else:
        # Bottom Border
        inputX = int(-(n + 2) / 2) + (input - BOTTOM_LEFT_VAL)
        inputY = int(-(n + 2) / 2)

    return abs(inputX) + abs(inputY)

assert(main(1) == 0)
assert(main(2) == 1)
assert(main(4) == 1)
assert(main(7) == 2)
assert(main(25) == 4)
print(main(368078))

# --- Part Two ---

# As a stress test on the system, the programs here clear the grid and then store the value 1 in square 1. Then, in the same allocation order as shown above, they store the sum of the values in all adjacent squares, including diagonals.

# So, the first few squares' values are chosen as follows:

# Square 1 starts with the value 1.
# Square 2 has only one adjacent filled square (with value 1), so it also stores 1.
# Square 3 has both of the above squares as neighbors and stores the sum of their values, 2.
# Square 4 has all three of the aforementioned squares as neighbors and stores the sum of their values, 4.
# Square 5 only has the first and fourth squares as neighbors, so it gets the value 5.
# Once a square is written, its value does not change. Therefore, the first few squares would receive the following values:

# 147  142  133  122   59
# 304    5    4    2   57
# 330   10    1    1   54
# 351   11   23   25   26
# 362  747  806--->   ...
# What is the first value written that is larger than your puzzle input?
