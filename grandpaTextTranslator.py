import csv

def readText():
    with open("grandpaText.txt", mode = 'r') as fileText:
        allFileContents = csv.reader(fileText)
#        print(allFileContents)
        translateText(allFileContents)
    return(allFileContents)

def translateText(allFileContents):
#    translation = []
    for line in allFileContents:
        if grandpaText in line:
#            translation.append(word)
            print (line)

#        else:
#            print("Are you sure you entered the correct text?  Please try again.  ")
#    
    return 

grandpaText = input("Enter the text you would like translated.  \n").upper()    
readText()

