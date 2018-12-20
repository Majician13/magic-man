#Use a list comprehension to square each odd number in a list. The list is input
#by a sequence of comma-separated numbers.
#Suppose the following input is supplied to the program:
#1,2,3,4,5,6,7,8,9
#Then, the output should be:
#1,3,5,7,9

print("Enter numbers separated by comma with no spaces ")
userInput = input()

holder = []

for number in userInput.split(","):
    intNumber = int(number)
    if intNumber%2 != 0:
        total = intNumber * intNumber
        holder.append(total)

print(holder)