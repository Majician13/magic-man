# Main function uses printMessage(), but it isn't called until the main() is called.
def main():
    printMessage()
    return

# Must define function prior to using it.  
def printMessage():
    print("Hello, world!")
    return

main()  # This is where you call printMessage() function.

