def is_tachycardic(stringToCheck):
    targetString = "tachycardic" # string to check against

    # Initialize variables
    testString = "" # string which will be built out in loop below
    typoCount = 0 # number of typos (uppercase excluded) in stringToCheck

    convertedString = stringToCheck.lower()
    for char in targetString:
        testString = testString + char
        if testString not in convertedString:
            typoCount += 1
            testString = ""
    if typoCount <= 2: # maximum tolerance is 2 missing or misspelled letters
        return True
    else:
        return False
