#Write a program that accepts a sentence and calculate the number of letters and digits.
#Suppose the following input is supplied to the program:
#hello world! 123
#Then, the output should be:
#LETTERS 10
#DIGITS 3

print("enter letters and/or numbers ")
userInput = input()

d = {"Digits":0, "Letters":0}

for c in userInput:
    if c.isdigit():
        d["Digits"] += 1
    elif c.isalpha():
        d["Letters"] += 1
    else:
        pass

print("Letters", d["Letters"])
print("Digits", d["Digits"])
        
