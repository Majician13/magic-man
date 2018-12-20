#Define a function that can accept two strings as input and
#concatenate them and then print it in console.

def convertToStr():
    print("Type 2 numbers with a space between them. EX: 5 7")
    userInput = input()

    useNum = userInput.split(" ")
    first = (useNum[0])
    second = (useNum[1])
    total = first + second
    print(total)
    return()

convertToStr()