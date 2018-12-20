#Define a function that can accept an integer number as
#input and print the "It is an even number" if the number is
#even, otherwise print "It is an odd number".

def evenOdd():
    print("Type a number")
    userInput = int(input())
    if userInput%2 == 0:
        print("It is an even number")
    elif userInput%2 != 0:
        print("It is an odd number")
    else:
        pass
    
evenOdd()
    