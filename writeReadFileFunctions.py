def writeText(data, filename):
    with open(filename, mode = 'w') as file:
        file.write(data)
    return

def readText(filename):
    with open(filename, mode = 'r') as fileText:
        allFileContents = fileText.read()
        print(allFileContents)
    return



getText = input("enter your text here.  ")
getFileName = input("enter filename here.  ")
writeText(getText, getFileName)
print("file written successfully")

readText(getFileName)