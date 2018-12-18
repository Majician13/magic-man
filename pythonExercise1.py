#Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
#between 2000 and 3200 (both included).
#The numbers obtained should be printed in a comma-separated sequence on a single line.

num1 = 7
num2 = 5
numMod = []
for count in range(1999, 3201):
    if count % 7 == 0:
        if count % 5 != 0:
            numMod.append(count)
            
print(numMod)