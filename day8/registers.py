# --- Day 8: I Heard You Like Registers ---

# You receive a signal directly from the CPU. Because of your recent assistance with jump instructions, it would like you to compute the result of a series of unusual register instructions.

# Each instr consists of several parts: the register to modify, whether to increase or decrease that register's value, the amount by which to increase or decrease it, and a condition. If the condition fails, skip the instr without modifying the register. The registers all start at 0. The instructions look like this:

# b inc 5 if a > 1
# a inc 1 if b < 5
# c dec -10 if a >= 1
# c inc -20 if c == 10
# These instructions would be processed as follows:

# Because a starts at 0, it is not greater than 1, and so b is not modified.
# a is increased by 1 (to 1) because b is less than 5 (it is 0).
# c is decreased by -10 (to 10) because a is now greater than or equal to 1 (it is 1).
# c is increased by -20 (to -10) because c is equal to 10.
# After this process, the largest value in any register is 1.

# You might also encounter <= (less than or equal to) or != (not equal to). However, the CPU doesn't have the bandwidth to tell you what all the registers are named, and leaves that to you to determine.

# What is the largest value in any register after completing the instructions in your puzzle input?


class instr(object):

    def __init__(self, register, action, actionValue, conditionalRegister, condition, conditionalValue):
        self.register = register
        self.action = action
        self.actionValue = actionValue
        self.conditionalRegister = conditionalRegister
        self.condition = condition
        self.conditionalValue = conditionalValue

# Every line contains the following parts
# register | inc/dec | value | if | register | {==,!=,<,<=, >, >=} | value


def getInput(path):
    file = open(path, "r")
    instructions = []
    registry = {}
    for line in file.readlines():
        line = line.rstrip()
        parts = line.split()
        assert(len(parts) == 7)
        instructions.append(instr(parts[0], parts[1], int(
            parts[2]), parts[4], parts[5], int(parts[6])))
        registry[parts[0]] = 0

    return registry, instructions


def partOne(registry, instructions):
    # Holds register and their values
    for instr in instructions:
        conditionSatisfied = False
        if instr.condition == "==":
            conditionSatisfied = registry[instr.conditionalRegister] == instr.conditionalValue
        elif instr.condition == "!=":
            conditionSatisfied = registry[instr.conditionalRegister] != instr.conditionalValue
        elif instr.condition == "<":
            conditionSatisfied = registry[instr.conditionalRegister] < instr.conditionalValue
        elif instr.condition == "<=":
            conditionSatisfied = registry[instr.conditionalRegister] <= instr.conditionalValue
        elif instr.condition == ">":
            conditionSatisfied = registry[instr.conditionalRegister] > instr.conditionalValue
        elif instr.condition == ">=":
            conditionSatisfied = registry[instr.conditionalRegister] >= instr.conditionalValue

        if conditionSatisfied:
            if instr.action == "inc":
                registry[instr.register] += instr.actionValue
            elif instr.action == "dec":
                registry[instr.register] -= instr.actionValue

    # Find largest value of all registers
    maxRegister = max(registry.values())
    print(maxRegister)
    return maxRegister


registry, instructions = getInput("day8/test")
assert(partOne(registry, instructions) == 1)

registry, instructions = getInput("day8/input")
partOne(registry, instructions)

""""
--- Part Two ---

To be safe, the CPU also needs to know the highest value held 
in any register during this process so that it can decide how 
much memory to allocate to these operations. 
For example, in the above instructions, 
the highest value ever held was 10 (in register c after the third instruction was evaluated).
"""

def partTwo(registry, instructions):
    # Holds register and their values
    maxValueOverAll = 0
    for instr in instructions:
        conditionSatisfied = False
        if instr.condition == "==":
            conditionSatisfied = registry[instr.conditionalRegister] == instr.conditionalValue
        elif instr.condition == "!=":
            conditionSatisfied = registry[instr.conditionalRegister] != instr.conditionalValue
        elif instr.condition == "<":
            conditionSatisfied = registry[instr.conditionalRegister] < instr.conditionalValue
        elif instr.condition == "<=":
            conditionSatisfied = registry[instr.conditionalRegister] <= instr.conditionalValue
        elif instr.condition == ">":
            conditionSatisfied = registry[instr.conditionalRegister] > instr.conditionalValue
        elif instr.condition == ">=":
            conditionSatisfied = registry[instr.conditionalRegister] >= instr.conditionalValue

        if conditionSatisfied:
            if instr.action == "inc":
                registry[instr.register] += instr.actionValue
            elif instr.action == "dec":
                registry[instr.register] -= instr.actionValue

        maxValueOverAll = max(maxValueOverAll, registry[instr.register])


    print(maxValueOverAll)
    return maxValueOverAll

registry, instructions = getInput("day8/test")
assert(partTwo(registry, instructions) == 10)

registry, instructions = getInput("day8/input")
partTwo(registry, instructions)