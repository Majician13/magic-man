#Write a program which can compute the factorial of a given numbers.
#The results should be printed in a comma-separated sequence on a single line.
#Suppose the following input is supplied to the program:
#8
#Then, the output should be:
#40320

print("enter a number to see factorial.")
i = int(input())

#i = 8
total = i
while i != 1:
    total = total * (i - 1)
    i -= 1
    
print(total)