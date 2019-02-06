def is_tachycardic(stringToCheck):
    targetString = "tachycardic" # string to check against

    # Initialize variables
    testString = "" # string which will be built out in loop below
    typoCount = 0 # number of typos (uppercase excluded) in stringToCheck
    beginRange = 0
    endRange = 1

    convertedString = stringToCheck.lower()
    for char in targetString:
        testString = testString + char
        if testString not in convertedString[beginRange:endRange]:
            typoCount += 1
            testString = ""
            beginRange = endRange - 1
        else:
            endRange += 1

    if typoCount <= 2: # maximum tolerance is 2 missing or misspelled letters
        return True
    else:
        return False
