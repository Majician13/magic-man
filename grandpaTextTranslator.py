import csv

def readText():
    with open("grandpaText.txt", mode = 'r') as fileText:
        allFileContents = fileText.read()
        print(allFileContents)
        translateText(allFileContents)
    return(allFileContents)

def translateText(allFileContents):
    translation = []
    for word in grandpaText:
        if word in allFileContents:
            translation.append(word)
        else:
            print("Are you sure you entered the correct text?  Please try again.  ")
    print(translation)
    return 

grandpaText = input("Enter the text you would like translated.  \n")    
readText()


