import csv

with open("module11.txt", "r") as fileAnimal :
    allRowsList = csv.reader(fileAnimal)
    
    for currentRow in allRowsList :
        for currentWord in currentRow :
            print(currentWord)