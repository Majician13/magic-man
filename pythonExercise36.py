#Define a function which can generate and print a list where the
#values are square of numbers between 1 and 20 (both included).

def printList():
    pList = []
    for p in range(1, 21):
        pList.append(p**2)
    print(pList)
    
printList()