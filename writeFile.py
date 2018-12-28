import csv

def main():
    writeUserFile()
    readUserFile(myFile)
    return

#Write to file
def writeUserFile():
    userText = input("Text Here! \n")
    userFile = input("Filname Here! \n")
    with open(userFile, "w") as myFile :
        userFile.write(userText)
        print("File written successfully \n")
    return(myFile)
    
#Read from file line by line and word by word
def readUserFile():
    with open("module11.txt", "r") as myFile :
        files = csv.reader(myFile)
        for currentRow in files :
            print(",".join(currentRow)) #displays data without brackets
            for word in currentRow :
                print(word)
    return()

