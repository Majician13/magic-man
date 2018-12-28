def main():
    names = ["Chris", "Jody", "Austin"]
    newName = input("Enter last guest: ")
    names.append(newName)
    
    printNames(names)
    return

def printNames(list):
    for name in list:
        print(name)
    return

main()