#Write a program which accepts a sequence of comma-separated numbers from console and
#generate a list and a tuple which contains every number.
#Suppose the following input is supplied to the program:
#34,67,55,33,12,98
#Then, the output should be:
#['34', '67', '55', '33', '12', '98']
#('34', '67', '55', '33', '12', '98')

list1 = []
toop = ()
i = 1

while i < 6:
    print("Type a number")
    numbers = int(input())
    list1.append(numbers)
    i += 1
    
print(list1)
toop = tuple(list1)
print(toop)
