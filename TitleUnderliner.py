def titleUnderliner(titleName, titleUnderlineObject):
    
    print(titleName) # Prints the title
    titleNameLength = len(titleName) # Gets how many characters are in the title
    
    titleNameCounter = 0
    titleUnderlineLoop = False
    while titleUnderlineLoop == False:
        
        print(titleUnderlineObject, end = '') # Prints the object until the loop ends
        
        titleNameCounter = titleNameCounter + 1 # Adds 1 to the counter for the counter
        
        if titleNameCounter == titleNameLength:
            print("\n")
            titleUnderlineLoop = True # Breaks loop.