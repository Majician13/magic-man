#Define a function which can generate a list where the values
#are square of numbers between 1 and 20 (both included). Then
#the function needs to print the last 5 elements in the list.

def printList():
    pL = list()
    for p in range(1, 21):
        pL.append(p**2)
    print(pL[-5:])
    
printList()