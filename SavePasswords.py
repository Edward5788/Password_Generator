def savePasswordMenu():
    
    def savePasswordErrorCodeFunction():
        print(savePasswordErrorCode1)
        savePasswordAnswerOriginalFull = savePasswordAnswerOriginalFull + savePasswordAnswerOriginal # Adding to the full responce
        savePasswordAnswerOriginal = "" # Wiping the variable clean
        
    savePasswordErrorCode1 = "\nInvalid input, either type 'SP' to save passwords or enter to continue.\nYou typed '" + str(savePasswordAnswerOriginal) + "'" # Making the error code a variable to be used more than once
    savePasswordAnswerOriginal = ""
    savePasswordAnswerOriginalFull = "" # This is used to add up all the original responces from the user
    savePasswordPossibleAnswers = ["", "SP"]
    savePasswordQLoop = False
    while savePasswordQLoop == False:
        try:
            savePasswordAnswer = str(input("\nType " + savePasswordPossibleAnswers[1] + " to save your passwords (you can wipe them later)\nOr press enter to continue\n\nEnter an answer: "))
            
            savePasswordAnswerOriginal = savePasswordAnswerOriginal + savePasswordAnswer # Saving the user's raw input, used later for the custom error code
            
            savePasswordAnswer = savePasswordAnswer.upper() # Capitalising the input
        
            
            if savePasswordAnswer in savePasswordPossibleAnswers: #savePasswordAnswer == "SP" or savePasswordAnswer == "":
                savePasswordQLoop = True
                print("This made it. MK II")
            else:
                savePasswordErrorCodeFunction()
                
        except:
            savePasswordErrorCodeFunction()
                    
        print("Program ended, orginal responce: " + str(savePasswordAnswerOriginalFull))
            
savePasswordMenu()