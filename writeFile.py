import csv

#Write to file
with open("module11.txt", "w") as myFile :
    myFile.write("Jody,40 \n")
    myFile.write("Chris,42 \n")
    myFile.write("Austin,5 \n")
    myFile.write("Larry,70 \n")
    print("File written successfully \n")
    
#Read from file line by line and word by word
with open("module11.txt", "r") as myFile :
    files = csv.reader(myFile)
    for currentRow in files :
        print(",".join(currentRow)) #displays data without brackets
        for word in currentRow :
            print(word)