import csv

grandpaText = input("Enter the text you would like translated.  \n").upper()

with open("grandpaText.txt", mode = 'r') as fileText:
    allFileContents = csv.reader(fileText)
#        print(allFileContents)
#        translateText(allFileContents)
        
    for line in allFileContents:
        if grandpaText in line:
#            translation.append(word)
            print (line)