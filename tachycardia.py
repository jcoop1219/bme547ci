from Levenshtein import distance


def main():
    stringToCheck = getInput()
    output = is_tachycardic(stringToCheck)
    provideFeedback(output)


def getInput():
    stringToCheck = input("\n\nEnter String: ")
    return stringToCheck


def provideFeedback(output):
    if output is True:
        print("\nThe entered word matches 'tachycardic'.")
    else:
        print("\nThe entered word does NOT match 'tachycardic'.")
    print("\n")


def is_tachycardic(stringToCheck):
    targetString = "tachycardic"  # string to check against

    # Clean input by removing trailing/leading non-alphabetic characters
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

if __name__ == "__main__":
    main()
