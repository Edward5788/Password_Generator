def titleUnderliner(titleName, titleUnderlineObject):

    print(titleName)  # Prints the title
    # Gets how many characters are in the title
    titleNameLength = len(titleName)

    titleNameCounter = 0
    titleUnderlineLoop = False
    while titleUnderlineLoop == False:

        # Prints the object until the loop ends
        print(titleUnderlineObject, end='')

        # Adds 1 to the counter for the counter
        titleNameCounter = titleNameCounter + 1

        if titleNameCounter == titleNameLength:
            print("\n")
            titleUnderlineLoop = True  # Breaks loop.
