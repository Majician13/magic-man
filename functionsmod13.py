def getMessage():
    getName = input("Text you want entered? ")
    userFile = input("What filename? ")
    with open(userFile, "w") as usersFile:
        usersFile.write(getName)
    message = "File written successfully"
    
#    output = getMessage(getName)
#    printMessage(output)
    return message

def printMessage(message):
    print(message)
    return

getMessage()
printMessage()
    

