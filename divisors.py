num = int(input("Enter a number  "))

x = range(1, num)

for i in x:
    if ((num % i) == 0):
        print(i)
        