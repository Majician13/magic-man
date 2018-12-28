import csv

def readText():
    with open("grandpaText.csv", mode = 'r') as fileText:
        allFileContents = fileText.read()
        # print(allFileContents)
        translateText(allFileContents)
        spamreader = fileText.reader("grandpaText.csv", delimiter=' ', quotechar='|')
        for row in spamreader:
            print(', '.join(row))
    return(allFileContents)

def translateText(allFileContents):
    # translation = []
    
    # for line in allFileContents:
    #     line = line.rstrip()
    #     if not line.startswith(grandpaText) : continue
    #     words = line.split()
    #     print(words)

    # if grandpaText in allFileContents:
        # print(' '.join([str(grandpaText) for grandpaText in allFileContents]))
        # for row in allFileContents:
        #     for elem in row:
        #         print(elem, end=' ')
    



    # if any(word in allFileContents for word in grandpaText):
        # words = word.split()
        # print(words)
    # else: 
    #     print("Are you sure you entered the correct text?  Please try again.  ")
    # print(words)
    return 

grandpaText = input("Enter the text you would like translated.  \n").upper()    
# readText()

# ["foo", "bar", "baz"].index("bar")
#  print(' '.join([str(elem) for elem in row]))
# for row in a:
#     for elem in row:
#         print(elem, end=' ')
# with open('eggs.csv', newline='') as csvfile:
#      spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
#      for row in spamreader:
#          print(', '.join(row))
