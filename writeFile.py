filename = "module11.txt"

myFile = open(filename, "w")
myFile.write("This is a test 1 \n")
myFile.close()

myFile = open(filename, 'a')
myFile.write("This is appended")
myFile.close()

print("File written successfully")
