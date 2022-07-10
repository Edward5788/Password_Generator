
# Imports
import time
import random
import socket
# Attempting to import colorama

try:
    from colorama import Fore, Back, Style
except:
    print("Unable to import colorama. Program will end.")
    exit()  # Ends program (works)
# End of imports


def exitProgram():  # This function is to exit the program in a safe way (wiping all stored info)
    """
    This function is to wipe all data the user has created
    ------------------------------------------------------
    To do list (/ = Complete, - =  Incomplete)
        - Wipe newPassword variable /
        - Wipe all stored data on the SavePasswords variable (future feature that stores all paswords -
    """

    newPassword = ""  # Wipes newPassword

    # Prints out password (which should contain nothing)
    print(str(newPassword))

    # Clearing user's clipboard free of possible stored SavePasswords
    # Imports funtion from Display to copy nothing to the clipboard
    from Display import exitProgramClipboardWiper
    # Function also prints if it's a sucess or not (clearing the clipboard)
    exitProgramClipboardWiper()

    # Ending the program
    try:
        exit()
    except:
        print("\nProgram unable to exit. However, all data has been wiped, therefore it's safe to exit\nhow you wish.\n")


def passwordManager():

    # Getting function to underline the title
    from TitleUnderliner import titleUnderliner

    titleName = "Password Manager"
    titleUnderlineObject = "-"
    titleUnderliner(titleName, titleUnderlineObject)  # Prints out the title

    def errorMessage():
        print("Invalid input, try again.")
        time.sleep(0.1)  # Short wait to add smoothness

    # generatedPasswordsCount = 0 # Setting the password counting variable
    PWManagerLoop = False
    while PWManagerLoop == False:
        """
        if generatedPasswordsCount > 1:
            print("\nTotal amount of generated passwords: " + str(generatedPasswordsCount) + "\n\n")

            titleName = "Next Password"
            titleUnderlineObject = "="
            titleUnderliner(titleName, titleUnderlineObject)
        elif generatedPasswordsCount == 1 or generatedPasswordsCount == 0:
            print("") # Prints out nothing just to continue through the program."""

        possibleYesAnswers = ["Y", "YES", "YE", "YEAH",
                              "YEA", "YER", "YAR", "OFC", "YEP", "ABSOLUTELY"]  # Variable to validate future inputs to for Y/N inputs.
        possibleNoAnswers = ["N", "NO", "NAH", "NOPE"]

        # Below decides if special characters will be in the password
        specialCharactersStatusLoop = False
        while specialCharactersStatusLoop == False:
            try:
                specialCharactersStatusQ = str(
                    input("Would you like your password to contain special characters? (Y/n)"))
                specialCharactersStatusQ = specialCharactersStatusQ.upper()

                if specialCharactersStatusQ in possibleYesAnswers or specialCharactersStatusQ in possibleNoAnswers:
                    if specialCharactersStatusQ in possibleYesAnswers:
                        # Changing the input to the original expected answer.
                        specialCharactersStatusQ = "Y"
                        specialCharactersStatus = True
                        specialCharactersStatusLoop = True  # Breaks loop

                    elif specialCharactersStatusQ in possibleNoAnswers:
                        # Changing the input to the original expected answer.
                        specialCharactersStatusQ = "N"
                        specialCharactersStatus = False
                        specialCharactersStatusLoop = True  # Breaks loop
                else:
                    errorMessage()

            except:
                errorMessage()

        # Below decides if numbers will be in the password
        basicNumbersStatusLoop = False
        while basicNumbersStatusLoop == False:
            try:
                basicNumbersStatusQ = input(
                    "Would you like your password to contain numbers? (Y/n)")
                basicNumbersStatusQ = basicNumbersStatusQ.upper()

                if basicNumbersStatusQ in possibleNoAnswers or basicNumbersStatusQ in possibleYesAnswers:
                    if basicNumbersStatusQ in possibleYesAnswers:
                        basicNumbersStatusQ = "Y"
                        basicNumbersStatusLoop = True
                    elif basicNumbersStatusQ in possibleNoAnswers:
                        basicNumbersStatusQ = "N"
                        basicNumbersStatusLoop = True
                else:
                    errorMessage()

            except:
                errorMessage()

        if basicNumbersStatusQ in possibleYesAnswers:
            basicNumbersStatusLoop = True  # Breaks loop
            basicNumbersStatus = True

        elif basicNumbersStatusQ in possibleNoAnswers:
            basicNumbersStatusLoop = True  # Breaks loop
            basicNumbersStatus = False

        # Below decides if lower case letters will be in the password
        lowerAlphabetStatusLoop = False
        while lowerAlphabetStatusLoop == False:
            try:
                lowerAlphabetStatusQ = str(
                    input("Would you like your password to contain lower case letters? (Y/n)"))
                lowerAlphabetStatusQ = lowerAlphabetStatusQ.upper()

                if lowerAlphabetStatusQ in possibleYesAnswers or lowerAlphabetStatusQ in possibleNoAnswers:
                    if lowerAlphabetStatusQ in possibleYesAnswers:
                        # Changing the input to the original expected answer.
                        lowerAlphabetStatusQ = "Y"
                        lowerAlphabetStatus = True
                        lowerAlphabetStatusLoop = True  # Breaks loop

                    elif lowerAlphabetStatusQ in possibleNoAnswers:
                        # Changing the input to the original expected answer.
                        lowerAlphabetStatusQ = "N"
                        lowerAlphabetStatus = False
                        lowerAlphabetStatusLoop = True  # Breaks loop
                else:
                    errorMessage()

            except:
                errorMessage()

        # Below decides if upper case letters will be in the passwordp
        upperAlphabetStatusLoop = False
        while upperAlphabetStatusLoop == False:
            try:
                upperAlphabetStatusQ = str(
                    input("Would you like your password to contain capital letters? (Y/n)"))
                upperAlphabetStatusQ = upperAlphabetStatusQ.upper()

                if upperAlphabetStatusQ in possibleYesAnswers or upperAlphabetStatusQ in possibleNoAnswers:
                    if upperAlphabetStatusQ in possibleYesAnswers:
                        # Changing the input to the original expected answer.
                        upperAlphabetStatusQ = "Y"
                        upperAlphabetStatusLoop = True  # Breaks loop
                        upperAlphabetStatus = True

                    elif upperAlphabetStatusQ in possibleNoAnswers:
                        # Changing the input to the original expected answer.
                        upperAlphabetStatusQ = "N"
                        upperAlphabetStatus = False
                        upperAlphabetStatusLoop = True  # Breaks loop
                else:
                    errorMessage()

            except:
                errorMessage()

        # Getting the password length
        passwordLengthComplete = False
        while passwordLengthComplete == False:

            try:
                passwordLength = str(
                    input("Enter the length of your password: "))

                try:  # Checking if the input is a digit
                    if passwordLength.isdigit():

                        # Validating if they've entered a password length graeter than 0
                        if int(passwordLength) >= 1:
                            passwordLengthComplete = True

                        else:  # IF the input is not greater than 0
                            print(
                                "Invalid input, please enter a number greater than 0")
                            # Waits a short amount of time to add smoothness to the program
                            time.sleep(0.1)

                    else:  # If input is not a digit
                        print("Invalid input, input is not a digit, try again")
                        time.sleep(0.1)

                except:  # Error code if input is not a digit
                    print("Invalid input, input is not a digit, try again")
                    time.sleep(0.1)

            except:  # Error code for if the program fails
                print("Invalid input, try again")
                time.sleep(0.1)

        # From here
        """
        specialCharactersStatus = True
        basicNumbersStatus = True
        lowerAlphabetStatus = True
        upperAlphabetStatus = True
        """
        newPassword = ""
        from PasswordGenerator import passwordGenerator
        passwordGenerator(newPassword, passwordLength, specialCharactersStatus,
                          basicNumbersStatus, lowerAlphabetStatus, upperAlphabetStatus)

        # After generated a password now asking if they woould lke the same again.

        # Creating new password
        afterPasswordloop = False
        while afterPasswordloop == False:
            print("\nType '" + Fore.GREEN + "R" + Fore.WHITE +
                  "' to regenerate another password using your current saved requirements")
            print("Type '" + Fore.RED + "E" + Fore.WHITE +
                  "' to exit the program and wipe all data used")
            print("Press " + Fore.BLUE + "Enter" + Fore.WHITE +
                  " to continue on and make a new password with different requirements")

            def nextPasswordInputErrorCode():  # This is code for below in the event of an error on both the user and the programs's side
                print("Invalid input, try again.")
                time.sleep(0.8)

            # Adding possible inputs to an array to validate it - note that "" means the enter button has been pressed
            possibleNextPasswordOptions = ["R", "", "L", "E"]
            nextPasswordOptionsLoop = False
            while nextPasswordOptionsLoop == False:
                try:
                    nextPasswordOptions = input("\nEnter an answer: ")
                    # Converting the input to upper case
                    nextPasswordOptions = nextPasswordOptions.upper()

                    # If user input is in the array above then it will proceed
                    if nextPasswordOptions in possibleNextPasswordOptions:
                        nextPasswordOptionsLoop = True
                    else:  # Handling wrong inputs
                        nextPasswordInputErrorCode()
                except:  # If error then will execute this
                    nextPasswordInputErrorCode()

            if nextPasswordOptions == "R":  # Regenerating using their saved password requirements
                newPassword = ""
                from PasswordGenerator import passwordGenerator
                passwordGenerator(newPassword, passwordLength, specialCharactersStatus,
                                  basicNumbersStatus, lowerAlphabetStatus, upperAlphabetStatus)

            elif nextPasswordOptions == "":  # If the user presses enter
                afterPasswordloop = True  # Breaks loop
            elif nextPasswordOptions == "E":  # If the user types "E" then it exits the program here

                exitProgramConfirmationLoop = False
                while exitProgramConfirmationLoop == False:

                    print("Exit program has been selected")
                    try:
                        exitProgramConfirmationInput = str(
                            input("\nType 'Y' to confirm, or 'N' to cancel\nEnter an answer: "))  # Taking input from user
                        # Converts input to upper case
                        exitProgramConfirmationInput = exitProgramConfirmationInput.upper()

                        if exitProgramConfirmationInput in possibleYesAnswers:  # Validating it
                            exitProgramConfirmationLoop = True  # Ends loop
                            exitProgram()  # Runs function to safely exit the program
                        elif exitProgramConfirmationInput in possibleNoAnswers:
                            print("\nExit program cancelled")
                            exitProgramConfirmationLoop = True  # Breaks out of loop
                        else:
                            print("Invalid input, enter 'Y' or 'N' to continue")
                    except:
                        print("Invalid input, enter 'Y' or 'N' to continue")
                        time.sleep(0.1)

        # Ends here

        """ # Key variables that were filled out by the user inputs 
        specialCharactersStatus = True
        basicNumbersStatus = True
        lowerAlphabetStatus = True
        upperAlphabetStatus = True
        """
        newPassword = ""  # Wipes data in current newPassword variable in order to replace it with a new password
        from PasswordGenerator import passwordGenerator
        passwordGenerator(newPassword, passwordLength, specialCharactersStatus,
                          basicNumbersStatus, lowerAlphabetStatus, upperAlphabetStatus)


start_time = time.time()  # Gets the start time that the user started the program


passwordManager()
