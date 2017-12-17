"""
--- Day 16: Permutation Promenade ---

You come upon a very unusual sight; a group of programs here appear to be dancing.

There are sixteen programs in total, named a through p. They start by standing in a line: a stands in position 0, b stands in position 1, and so on until p, which stands in position 15.

The programs' dance consists of a sequence of dance moves:

Spin, written sX, makes X programs move from the end to the front, but maintain their order otherwise. (For example, s3 on abcde produces cdeab).
Exchange, written xA/B, makes the programs at positions A and B swap places.
Partner, written pA/B, makes the programs named A and B swap places.
For example, with only five programs standing in a line (abcde), they could do the following dance:

s1, a spin of size 1: eabcd.
x3/4, swapping the last two programs: eabdc.
pe/b, swapping programs e and b: baedc.
After finishing their dance, the programs end up in order baedc.

You watch the dance for a while and record their dance moves (your puzzle input). In what order are the programs standing after their dance?

"""

class DanceMove(object):
    def __init__(self,action, A, B, X):
        self.action = action
        self.A = A
        self.B = B
        self.X = X

def getInput(path):
    file = open(path, "r")
    lines = file.readlines()
    assert(len(lines) == 1)
    commands = lines.pop().split(",")
    input = []
    for cmd in commands:
        action = cmd[0]
        move = None
        X = None
        A = None
        B = None
        if action == "s":
            X = int(cmd[1::])
        elif action == "x":
            positions = cmd[1::].split("/")
            A = int(positions[0])
            B = int(positions[1])
        elif action == "p":
            positions = cmd[1::].split("/")
            A = positions[0]
            B = positions[1]
        move = DanceMove(action, A, B, X)
        input.append(move)

    return input


def swapInList(progs, aIndx, bIndx):
    temp = progs[aIndx]
    progs[aIndx] = progs[bIndx]
    progs[bIndx] = temp
    return progs


assert(swapInList(list("abcde"), 0, 4) == list("ebcda"))


def spinList(lst, amnt):
    indx = len(lst) - amnt
    return lst[indx::] + lst[0:indx]


assert(spinList(list("abcde"), 1) == list("eabcd"))
assert(spinList(list("abcde"), 3) == list("cdeab"))
assert(spinList(list("abcde"), 4) == list("bcdea"))
assert(spinList(list("abcde"), 5) == list("abcde"))


def partOne(input, progs):
    for danceMove in input:
        if danceMove.action == "s":
            progs = spinList(progs, danceMove.X)
        elif danceMove.action == "x":
            progs = swapInList(progs, danceMove.A, danceMove.B)
        elif danceMove.action == "p":
            aIndx = progs.index(danceMove.A)
            bIndx = progs.index(danceMove.B)
            progs = swapInList(progs, aIndx, bIndx)

    answer = ''.join(progs)
    print(answer)
    return answer


assert(partOne(getInput("day16/test"),  list("abcde")) == "baedc")
partOne(getInput("day16/input"),  list("abcdefghijklmnop"))

"""
--- Part Two ---

Now that you're starting to get a feel for the dance moves, you turn your attention to the dance as a whole.

Keeping the positions they ended up in from their previous dance, the programs perform it again and again: including the first dance, a total of one billion (1000000000) times.

In the example above, their second dance would begin with the order baedc, and use the same dance moves:

s1, a spin of size 1: cbaed.
x3/4, swapping the last two programs: cbade.
pe/b, swapping programs e and b: ceadb.
In what order are the programs standing after their billion dances?
"""

def spinDict(progToIndx, indxToProg, amount):
    for p in progToIndx.keys():
        newIndx = (progToIndx[p] + amount) % len(progToIndx)
        progToIndx[p] = newIndx
        indxToProg[newIndx] = p

def swapInDictByIndx(progToIndx, indxToProg, aIndx, bIndx):
    a = indxToProg[aIndx]
    b = indxToProg[bIndx]
    progToIndx[a] = bIndx
    progToIndx[b] = aIndx
    indxToProg[aIndx] = b
    indxToProg[bIndx] = a

def swapInDictByName(progToIndx, indxToProg, a, b):
    aIndx = progToIndx[a]
    bIndx = progToIndx[b]
    progToIndx[a] = bIndx
    progToIndx[b] = aIndx
    indxToProg[aIndx] = b
    indxToProg[bIndx] = a

def partTwo(input, progs):
    """
    Current run time complexities of partOne are:
        Spin: O(n)
        Swap: O(1)
        Partner: O(n)
    We can make this more efficient at the cost of using more space by maintaining two dictionaries:
        progToIndx and indxToProg
    Then we can achieve:
    Spin: O(n)
    Swap: O(1)
    Partner: O(1)
    """
    progToIndx = {}
    indxToProg = {}
    for indx, p in enumerate(progs):
        progToIndx[p] = int(indx)
        indxToProg[indx] = p

    for i in range(0, 1000000000 % 24):
        for danceMove in input:
            if danceMove.action == "s":
                spinDict(progToIndx, indxToProg, danceMove.X)
            elif danceMove.action == "x":
                swapInDictByIndx(progToIndx, indxToProg, danceMove.A, danceMove.B)
            elif danceMove.action == "p":
                swapInDictByName(progToIndx, indxToProg, danceMove.A, danceMove.B)

    answer = ""
    for i in range(0, len(progToIndx)):
        answer += indxToProg[i]

    print(answer)
    return answer


partTwo(getInput("day16/input"),  list("abcdefghijklmnop"))

"""
Python is just slow to count to 1 billion, takes 80 seconds even without any calculations, possibly need to use
another language that is faster?

EDIT: After reimplementing in scala, we only have to calculate 1000000000%24 iterations
since the dance repeats after 24 iterations
"""