# --- Day 4: High-Entropy Passphrases ---

# A new system policy has been put in place that requires all accounts to use a passphrase instead of simply a password. A passphrase consists of a series of words (lowercase letters) separated by spaces.

# To ensure security, a valid passphrase must contain no duplicate words.

# For example:

# aa bb cc dd ee is valid.
# aa bb cc dd aa is not valid - the word aa appears more than once.
# aa bb cc dd aaa is valid - aa and aaa count as different words.
# The system's full passphrase list is available as your puzzle input. How many passphrases are valid?

# Returns List[String]


def getInput(path):
    file = open(path, "r")
    lines = file.readlines()
    lines = list(map(lambda l: l.rstrip(), lines))
    return lines


# Phrases expects type List[String]
def partOne(phrases):
    numValid = 0
    for phrase in phrases:
        words = phrase.split()
        seen = set()
        valid = True
        for word in words:
            if word in seen:
                valid = False
                break
            else:
                seen.add(word)

        if valid:
            numValid += 1

    print('Num valid: ' + str(numValid))
    return numValid

testPhrases = getInput("partOne/tests")
assert(partOne(testPhrases) == 2)

partOne(getInput("input"))