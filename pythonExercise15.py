#Write a program that computes the value of a+aa+aaa+aaaa with a given digit
#as the value of a.
#Suppose the following input is supplied to the program:
#9
#Then, the output should be:
#11106

print("Enter a number")
userInput = input()

first = userInput
second = userInput * 2
third = userInput * 3
fourth = userInput * 4

total = int(first) + int(second) + int(third) + int(fourth)

print(total)