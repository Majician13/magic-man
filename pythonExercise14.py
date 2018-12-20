#Write a program that accepts a sentence and calculate the number of upper case
#letters and lower case letters.
#Suppose the following input is supplied to the program:
#Hello world!
#Then, the output should be:
#UPPER CASE 1
#LOWER CASE 9

print("Enter a sentence with capital and lower case letters. ")
userInput = input()

d = {"Capital":0, "Lower":0}

for letter in userInput:
    if letter.isupper():
        d["Capital"] += 1
    elif letter.islower():
        d["Lower"] +=1
    else:
        pass

print("Lower", d["Lower"])
print("Capital", d["Capital"])    
