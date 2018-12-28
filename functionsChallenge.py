def fileWrite():
    userText = input("What text would you like in the file?  \n")
    userFile = input("What file name do you want? \n")
    
    with open(userFile, "w") as textFile:
        userFile.write(userText)
    return(userFile)
        
def printText():
    with open(userFile, "r") as textFile:
        files = csv.reader(textFile)
    for currentRow in files :
        print(",".join(currentRow)) #displays data without brackets
        for word in currentRow :
            print(word)

def main():
    fileWrite()
    printText()
    
    return
    