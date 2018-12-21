#Write a program which accepts a string as input to print "Yes"
#if the string is "yes" or "YES" or "Yes", otherwise print "No".

print("Type yes or no ")
userInput = input().upper()

if userInput == "YES":
    print("Yes")
else:
    print("No")
    