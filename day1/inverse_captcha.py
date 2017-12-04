# The captcha requires you to review a sequence of digits (your puzzle input) and find the sum of all digits that match the next digit in the list. The list is circular, so the digit after the last digit is the first digit in the list.

# For example:

# 1122 produces a sum of 3 (1 + 2) because the first digit (1) matches the second digit and the third digit (2) matches the fourth digit.
# 1111 produces 4 because each digit (all 1) matches the next.
# 1234 produces 0 because no digit matches the next.
# 91212129 produces 9 because the only digit that matches the next one is the last digit, 9.
# What is the solution to your captcha?

# Your puzzle answer was 1177.

# Actual test input that will be scored
def getInput():
    return open("input", "r").read()

# Personal test answers
def getCorrectAnswers(part):
    answerFile=open(part + "/tests-answer", "r")
    answers = []
    for line in answerFile:
        answers.append(int(line))
    return answers

# Personal tests
def getTests(part):
    testFile=open(part + "/tests", "r")
    tests = []
    for line in testFile:
        tests.append(line.rstrip())
    return tests

def personalTests(part, operation):
    testInputs = getTests(part)
    correctAnswers = getCorrectAnswers(part)
    for indx, test in enumerate(testInputs):
        print("Test " + str(indx+1))
        answer = operation(test)
        correct = correctAnswers[indx]

        if answer == correct:
            print("Correct!")
        else:
            print("Wrong...")
            print("Given: " + str(test))
            print("Output: " + str(answer))
            print("Expected: " + str(correct))

def partOne(inputString):
    accum = 0
    for i in range(0, len(inputString)):
        current = inputString[i]
        next = inputString[i+1] if i < len(inputString) - 1 else inputString[0]
        if current == next:
            accum += int(current)
    return accum

def partTwo(inputString):
    accum = 0
    halfway = int(len(inputString) / 2)
    for i in range(0, len(inputString)):
        current = inputString[i]
        nextPlusHalfWay = i + halfway
        nextIndex = nextPlusHalfWay % len(inputString)
        next = inputString[nextIndex]
        if current == next:
            accum += int(current)
    return accum

personalTests("partOne", partOne)
personalTests("partTwo", partTwo)
print()
print("Input Result")

print("Part One")
print(partOne(getInput()))

print("Part Two")
print(partTwo(getInput()))