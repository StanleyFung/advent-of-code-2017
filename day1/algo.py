# Actual test input that will be scored
def getInput():
    return open("input", "r").read()

# Personal test answers
def getCorrectAnswers():
    answerFile=open("tests-answer", "r")
    answers = []
    for line in answerFile:
        answers.append(int(line))
    return answers

# Personal tests
def getTests():
    testFile=open("tests", "r")
    tests = []
    for line in testFile:
        tests.append(line.rstrip())
    return tests

def personalTests():
    testInputs = getTests()
    correctAnswers = getCorrectAnswers()
    for indx, test in enumerate(testInputs):
        print("Test " + str(indx+1))
        answer = partOne(test)
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

personalTests()
print()
print("Input Result")
print(partOne(getInput()))