#Define a function that can receive two integral numbers
#in string form and compute their sum and then print it in console.

def convertToStr():
    print("Type 2 numbers with a space between them. EX: 5 7")
    userInput = input()

    useNum = userInput.split(" ")
    first = int(useNum[0])
    second = int(useNum[1])
    total = first + second
    print(total)
    return()

convertToStr()
        