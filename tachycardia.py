from Levenshtein import distance


def is_tachycardic(stringToCheck):
    targetString = "tachycardic"  # string to check against

    # Clean input by removing trailing/leading spaces and punctuation
    # and set to lowercase
    for char in stringToCheck:
        if char.isalpha() is False:
            stringToCheck = stringToCheck.replace(char, "")
    stringToCheck = stringToCheck.lower()

    # Use distance function from Levenshtein library to find the number of
    # differences between strings
    differenceCount = distance(stringToCheck, targetString)

    if differenceCount <= 2:  # maximum tolerance is 2 incorrect letters
        return True
    else:
        return False

<<<<<<< HEAD
#test
=======
>>>>>>> 5893100b221274d56641defee054ba483c63c2c1
