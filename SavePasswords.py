"""
This module is to add a feature to the rest of the program to save passwords for the user, therefore if the user forgets and needs an old password, they can retrieve it from memory.
All paswords will be automatically wiped before the program ends. This is for both security and privacy of the user.

    Aims:
        - Add a input for the user to have the choice whether they want to log tyheir passwords or not
        - 
"""


def savePasswordMenu():

    def savePasswordErrorCodeFunction():
        print(savePasswordErrorCode1)
        savePasswordAnswerOriginalFull = savePasswordAnswerOriginalFull + \
            savePasswordAnswerOriginal  # Adding to the full responce
        savePasswordAnswerOriginal = ""  # Wiping the variable clean

    savePasswordErrorCode1 = "\nInvalid input, either type 'SP' to save passwords or enter to continue.\nYou typed '" + \
        str(savePasswordAnswerOriginal) + \
        "'"  # Making the error code a variable to be used more than once
    savePasswordAnswerOriginal = ""
    # This is used to add up all the original responces from the user
    savePasswordAnswerOriginalFull = ""
    savePasswordPossibleAnswers = ["", "SP"]
    savePasswordQLoop = False
    while savePasswordQLoop == False:
        try:
            savePasswordAnswer = str(input(
                "\nType " + savePasswordPossibleAnswers[1] + " to save your passwords (you can wipe them later)\nOr press enter to continue\n\nEnter an answer: "))

            # Saving the user's raw input, used later for the custom error code
            savePasswordAnswerOriginal = savePasswordAnswerOriginal + savePasswordAnswer

            savePasswordAnswer = savePasswordAnswer.upper()  # Capitalising the input

            # savePasswordAnswer == "SP" or savePasswordAnswer == "":
            if savePasswordAnswer in savePasswordPossibleAnswers:
                savePasswordQLoop = True
                print("This made it. MK II")
            else:
                savePasswordErrorCodeFunction()

        except:
            savePasswordErrorCodeFunction()

        print("Program ended, orginal responce: " +
              str(savePasswordAnswerOriginalFull))


savePasswordMenu()
