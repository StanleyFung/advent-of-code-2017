# Actual test input that will be scored
def getInput(fileName):
    input = []
    file = open(fileName, "r").readlines()
    for line in file:
        line = line.rstrip()
        nums = line.split()
        nums = list(map(lambda num: int(num), nums))
        input.append(nums)
    return input

# Personal test answers


def getCorrectAnswers(part):
    answerFile = open(part + "/tests-answer", "r")
    answers = []
    for line in answerFile:
        answers.append(int(line))
    return answers


def getTests(part):
    return getInput(part + "/tests")


def personalTests(part, operation):
    testInputs = getTests(part)
    correctAnswers = getCorrectAnswers(part)
    answer = operation(testInputs)
    correct = correctAnswers[0]

    if answer == correct:
        print("Correct!")
    else:
        print("Wrong...")
        print("Given: " + str(testInputs))
        print("Output: " + str(answer))
        print("Expected: " + str(correct))


def partOne(input):
    # Input is of type List[List[Int]]
    accum = 0
    for row in input:
        accum += max(row) - min(row)
    return accum


def partTwo(input):
    # Input is of type List[List[Int]]
    accum = 0
    for row in input:
        for i in range(0, len(row)):
            for j in range(i + 1, len(row)):
                val1 = row[i]
                val2 = row[j]
                valid = val1 % val2 == 0 or val2 % val1 == 0
                if valid:
                    if val1 % val2 == 0:
                        accum += val1 / val2
                    elif val2 % val1 == 0:
                        accum += val2 / val1
                    # Only one pair in each row is valid
                    break
    return accum


# personalTests("partOne", partOne)
personalTests("partTwo", partTwo)
# print()
# print("Input Result")

# print("Part One")
# print(partOne(getInput("input")))

print("Part Two")
print(partTwo(getInput("input")))
