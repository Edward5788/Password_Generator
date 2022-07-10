from Display import passwordDisplay
import time
import random


def passwordGenerator(newPassword, passwordLength, specialCharactersStatus, basicNumbersStatus, lowerAlphabetStatus, upperAlphabetStatus):

    global specialCharacters
    # Setting values to be used for the pw generation
    specialCharacters = "`¬!£$%^&*()_+-={[}]:;@'~#<,>.?/'}\|\""

    global basicNumbers
    basicNumbers = "1234567890"

    global lowerAlphabet
    lowerAlphabet = "abcdefghijklmnopqrstuv"

    global upperAlphabet
    upperAlphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    # The code below gets the number of how many lists to generate the password from and then only

    statusCount = 0

    if specialCharactersStatus == True:
        statusCount = statusCount + 1

    if basicNumbersStatus == True:
        statusCount = statusCount + 1

    if lowerAlphabetStatus == True:
        statusCount = statusCount + 1

    if upperAlphabetStatus == True:
        statusCount = statusCount + 1  # Adds up the True's to see if there are any

    if statusCount <= 0:  # If there are no true's above then it gives an error code to the user
        print("\nYou have entered nothing to be in your password.")
        time.sleep(0.8)
        print("Try again.\n\n\n\n")

        from Main import passwordManager
        passwordManager()

    newPassword = ""  # Pre defining
    characterCounter = 0

    newPasswordGatherer = ""

    passwordGeneratorLoop = False
    while passwordGeneratorLoop == False:
        newCharacter = False

        # Picks a random number betwween 1 and 4
        passwordContainerDecider = random.randint(1, 4)

        # If the random number is this (1) then it grabs the contents of 1
        if passwordContainerDecider == 1:
            if specialCharactersStatus == True:
                newCharacter = True
                # Picks a random character from the variable to add to the pw
                newPasswordGatherer = random.choice(specialCharacters)
            else:
                characterCounter = characterCounter - 1

        elif passwordContainerDecider == 2:
            if basicNumbersStatus == True:
                newCharacter = True
                newPasswordGatherer = random.choice(basicNumbers)
            else:
                characterCounter = characterCounter - 1  # Losing 1 from the character count

        elif passwordContainerDecider == 3:
            if lowerAlphabetStatus == True:
                newCharacter = True
                newPasswordGatherer = random.choice(lowerAlphabet)
            else:
                characterCounter = characterCounter - 1

        elif passwordContainerDecider == 4:
            if upperAlphabetStatus == True:
                newCharacter = True
                newPasswordGatherer = random.choice(upperAlphabet)
            else:
                characterCounter = characterCounter - 1
        elif statusCount <= 0:
            # Kind of a note for me.
            print("Error - Need to have atleast 1 enabled.")

        else:
            print(
                "\n\nError creating a random number to decide which pasword family to go from\n\n")

        if newCharacter == True:
            # Adding up each new character to the password variable (newPassword)
            newPassword = newPassword + newPasswordGatherer

        characterCounter = characterCounter + 1  # Counting 1 up each time

        # Breaking the loop if the counter is >= value of the pasword length specified.
        if characterCounter >= int(passwordLength):
            passwordGeneratorLoop = True
            copyToClipboardOn = True
            passwordDisplay(copyToClipboardOn, newPassword)
