
# Add more comments... ;)


def passwordManager():
    
    # Attempting to import colorama
    
    try:
        from colorama import Fore, Back, Style
    except:
        print("Unable to import colorama. Program will end.")
        exit() # Ends program (works)
    
    """
    import colorama
    from colorama import Fore, Back, Style
    colorama.init(autoreset=True)
    print(Fore.BLUE + "Shalom all " + Fore.WHITE + "Jackie")
    """ # Colorama exampleD

    from TitleUnderliner import titleUnderliner # Getting function to underline the title

    titleName = "Password Manager"
    titleUnderlineObject = "-"
    titleUnderliner(titleName, titleUnderlineObject) # Prints out the title


    # Imports
    import time
    import random
    import socket
    # End of imports

    def errorMessage():
        print("Invalid input, try again.")
        time.sleep(0.1) # Short wait to add smoothness



        
    #generatedPasswordsCount = 0 # Setting the password counting variable
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



        
        # Below decides if special characters will be in the password
        possibleYesAnswers = ["Y", "YES", "YE", "YEAH", "YEA", "YER", "YAR", "OFC", "YEP", "ABSOLUTELY"]
        possibleNoAnswers = ["N", "NO", "NAH", "NOPE"]
        specialCharactersStatusLoop = False
        while specialCharactersStatusLoop == False:
            try:
                specialCharactersStatusQ = str(input("Would you like your password to contain special characters? (Y/n)"))
                specialCharactersStatusQ = specialCharactersStatusQ.upper()

                if specialCharactersStatusQ in possibleYesAnswers or specialCharactersStatusQ in possibleNoAnswers:
                    if specialCharactersStatusQ in possibleYesAnswers:
                        specialCharactersStatusQ = "Y" # Changing the input to the original expected answer.
                        specialCharactersStatus = True
                        specialCharactersStatusLoop = True # Breaks loop

                    elif specialCharactersStatusQ in possibleNoAnswers:
                        specialCharactersStatusQ = "N" # Changing the input to the original expected answer.
                        specialCharactersStatus = False
                        specialCharactersStatusLoop = True # Breaks loop
                else:
                    errorMessage()

                    
            except:
                errorMessage()



        # Below decides if numbers will be in the password
        basicNumbersStatusLoop = False
        while basicNumbersStatusLoop == False:
            try:
                basicNumbersStatusQ = input("Would you like your password to contain numbers? (Y/n)")
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
            basicNumbersStatusLoop = True # Breaks loop
            basicNumbersStatus = True

        elif basicNumbersStatusQ in possibleNoAnswers:
            basicNumbersStatusLoop = True # Breaks loop
            basicNumbersStatus = False
        
        
        

        # Below decides if lower case letters will be in the password
        lowerAlphabetStatusPossibleYesAnswers = ["Y", "YES", "YE", "YEAH"]
        lowerAlphabetStatusPossibleNoAnswers = ["N", "NO", "NAH", "NOPE"]
        lowerAlphabetStatusLoop = False
        while lowerAlphabetStatusLoop == False:
            try:
                lowerAlphabetStatusQ = str(input("Would you like your password to contain lower case letters? (Y/n)"))
                lowerAlphabetStatusQ = lowerAlphabetStatusQ.upper()

                if lowerAlphabetStatusQ in lowerAlphabetStatusPossibleYesAnswers or lowerAlphabetStatusQ in lowerAlphabetStatusPossibleNoAnswers:
                    if lowerAlphabetStatusQ in lowerAlphabetStatusPossibleYesAnswers:
                        lowerAlphabetStatusQ = "Y" # Changing the input to the original expected answer.
                        lowerAlphabetStatus = True
                        lowerAlphabetStatusLoop = True # Breaks loop

                    elif lowerAlphabetStatusQ in lowerAlphabetStatusPossibleNoAnswers:
                        lowerAlphabetStatusQ = "N" # Changing the input to the original expected answer.
                        lowerAlphabetStatus = False
                        lowerAlphabetStatusLoop = True # Breaks loop
                else:
                    errorMessage()

                    
            except:
                errorMessage()

                
        

        # Below decides if upper case letters will be in the password
        upperAlphabetStatusPossibleYesAnswers = ["Y", "YES", "YE", "YEAH"]
        upperAlphabetStatusPossibleNoAnswers = ["N", "NO", "NAH", "NOPE"]
        upperAlphabetStatusLoop = False
        while upperAlphabetStatusLoop == False:
            try:
                upperAlphabetStatusQ = str(input("Would you like your password to contain capital letters? (Y/n)"))
                upperAlphabetStatusQ = upperAlphabetStatusQ.upper()

                if upperAlphabetStatusQ in upperAlphabetStatusPossibleYesAnswers or upperAlphabetStatusQ in upperAlphabetStatusPossibleNoAnswers:
                    if upperAlphabetStatusQ in upperAlphabetStatusPossibleYesAnswers:
                        upperAlphabetStatusQ = "Y" # Changing the input to the original expected answer.
                        upperAlphabetStatusLoop = True # Breaks loop
                        upperAlphabetStatus = True

                    elif upperAlphabetStatusQ in upperAlphabetStatusPossibleNoAnswers:
                        upperAlphabetStatusQ = "N" # Changing the input to the original expected answer.
                        upperAlphabetStatus = False
                        upperAlphabetStatusLoop = True # Breaks loop
                else:
                    errorMessage()

                    
            except:
                errorMessage()
        


        # Getting the password length
        passwordLengthComplete = False
        while passwordLengthComplete == False:
                
            try:
                passwordLength = str(input("Enter the length of your password: "))
                    
                try: # Checking if the input is a digit
                    if passwordLength.isdigit():
                            
                        if int(passwordLength) >= 1: # Validating if they've entered a password length graeter than 0
                                passwordLengthComplete = True
                                
                        else: # IF the input is not greater than 0
                            print("Invalid input, please enter a number greater than 0")
                            time.sleep(0.1) # Waits a short amount of time to add smoothness to the program
                            
                    else: # If input is not a digit
                        print("Invalid input, input is not a digit, try again")
                        time.sleep(0.1)
                        
                except: # Error code if input is not a digit
                    print("Invalid input, input is not a digit, try again")
                    time.sleep(0.1)
                    
                        
            except: # Error code for if the program fails
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
        passwordGenerator(newPassword, passwordLength, specialCharactersStatus, basicNumbersStatus, lowerAlphabetStatus, upperAlphabetStatus)

        # After generated a password now asking if they woould lke the same again.

        

        # Creating new password
        afterPasswordloop = False
        while afterPasswordloop == False:
            print("\nType '" + Fore.GREEN + "R" + Fore.WHITE + "' to regenerate another password using your current saved requirements")
            print("Type '" + Fore.RED + "E" + Fore.WHITE + "' to exit the program and wipe all data used")
            print("Press " + Fore.BLUE + "Enter" + Fore.WHITE + " to continue on and make a new password with different requirements")

            def nextPasswordInputErrorCode(): # This is code for below in the event of an error on both the user and the programs's side
                print("Invalid input, try again.")
                time.sleep(0.8)
                
            possibleNextPasswordOptions = ["R", "", "L"] # Adding possible inputs to an array to validate it - note that "" means the enter button has been pressed
            nextPasswordOptionsLoop = False
            while nextPasswordOptionsLoop == False:
                try:
                    nextPasswordOptions = input("\nEnter an answer: ")
                    nextPasswordOptions = nextPasswordOptions.upper() # Converting the input to upper case

                    if nextPasswordOptions in possibleNextPasswordOptions: # If user input is in the array above then it will proceed
                        nextPasswordOptionsLoop = True
                    else: # Handling wrong inputs
                        nextPasswordInputErrorCode()
                except: # If error then will execute this
                    nextPasswordInputErrorCode()

            if nextPasswordOptions == "R": # Regenerating using their saved password requirements
                newPassword = ""
                from PasswordGenerator import passwordGenerator
                passwordGenerator(newPassword, passwordLength, specialCharactersStatus, basicNumbersStatus, lowerAlphabetStatus, upperAlphabetStatus)


            elif nextPasswordOptions == "":
                afterPasswordloop = True # Breaks loop           

        # Ends here



        """ # Key variables that were filled out by the user inputs 
        specialCharactersStatus = True
        basicNumbersStatus = True
        lowerAlphabetStatus = True
        upperAlphabetStatus = True
        """
        newPassword = ""
        from PasswordGenerator import passwordGenerator
        passwordGenerator(newPassword, passwordLength, specialCharactersStatus, basicNumbersStatus, lowerAlphabetStatus, upperAlphabetStatus)


import time
start_time = time.time() # Gets the start time that the user started the program

passwordManager()

