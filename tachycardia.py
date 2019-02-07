def is_tachycardic(stringToCheck):
    targetString = "tachycardic" # string to check against

    # Initialize variables
    testString = "" # string which will be built out in loop below
    typoCount = 0 # number of typos (uppercase excluded) in stringToCheck
    beginRange = 0
    endRange = 1

    # Clean input by remove trailing/leading spaces and punctuation and set to lowercase
    for char in stringToCheck:
        if char.isalpha() is False:
            stringToCheck = stringToCheck.replace(char, "")
    stringToCheck = stringToCheck.lower()
