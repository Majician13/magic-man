#Define a function that can accept two strings as input
#and print the string with maximum length in console.
#If two strings have the same length, then the function
#should print al l strings line by line.

def longSent():
    while True:
        userInput = input()
        if not userInput:
            break
        
        sents = userInput.split(",")
        one = sents[0]
        two = sents[1]
        lenOne = len(sents[0])
        lenTwo = len(sents[1])
        
        if lenOne > lenTwo:
            print(one)
        elif lenTwo > lenOne:
            print(two)
        else:
            print(one)
            print(two)
    
    return()

longSent()