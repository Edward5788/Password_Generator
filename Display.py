def addToClipBoard(clipboardItem):
    import pyperclip
    pyperclip.copy(clipboardItem)
    spam = pyperclip.paste()


generatedPasswordsCount = 0


def passwordDisplay(copyToClipboardOn, newPassword):

    if copyToClipboardOn == True:
        global clipboardItem
        clipboardItem = ""
        clipboardItem = clipboardItem + newPassword

        addToClipBoard(clipboardItem)

        print("\nPassword: " + str(newPassword))

        # Getting length of new passsword.
        newPasswordLength = len(newPassword)
        # Formats the password length to add a comma if the number goes above 1000 making it 1,000
        print("Password length: " + "{:,}".format(newPasswordLength))

        print("Password is sucessfully copied to clipbaord")
        """
        generatedPasswordsCount = generatedPasswordsCount + 1
        
        if generatedPasswordsCount > 1: # If the counter is above 1 then it prints out 
            print("Total amount of generated passwords: " + str(generatedPasswordsCount) + "\n\n")
            """

    else:
        print("Password not copied to clipboard.")


def exitProgramClipboardWiper():

    global clipboardItem
    clipboardItem = ""  # Makes the clipboard nothing

    # Wipes cliupboard by adding "" (nothing) to the clipboard
    try:
        addToClipBoard(clipboardItem)
        print("Clipboard is sucessfully cleared")
    except:
        print("Program failed to clear clipboard, try copying something else to yoru clipboard instead")


""" Testing
copyToClipboardOn = True
newPassword = "If you see this, it's copied to clipboard."
passwordDisplay(copyToClipboardOn, newPassword)
"""
# ----Testing if the new wiping funtion works----
exitProgramClipboardWiper()
