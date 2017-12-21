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
"""
--- Part Two ---

For added security, yet another system policy has been put in place. 
Now, a valid passphrase must contain no two words that are anagrams of each other - that is, 
a passphrase is invalid if any word's letters can be rearranged to form any other word in the passphrase.

For example:

abcde fghij is a valid passphrase.
abcde xyz ecdab is not valid - the letters from the third word can be rearranged to form the first word.
a ab abc abd abf abj is a valid passphrase, because all letters need to be used when forming another word.
iiii oiii ooii oooi oooo is valid.
oiii ioii iioi iiio is not valid - any of these words can be rearranged to form any other word.
"""
def partTwo(phrases):
    numValid = 0
    for phrase in phrases:
        words = phrase.split()
        seen = set()
        valid = True
        for word in words:
            word =  ''.join(sorted(word))
            if word in seen:
                valid = False
                break
            else:
                seen.add(word)

        if valid:
            numValid += 1

    print('Num valid: ' + str(numValid))
    return numValid

testPhrases = getInput("partTwo/tests")
assert(partTwo(testPhrases) == 3)

partTwo(getInput("input"))