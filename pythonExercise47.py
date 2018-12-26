#Write a program which can filter() to make a list
#whose elements are even number between 1 and 20
#(both included).

li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evenNumbers = filter(lambda x: x%2 == 0, li)
print(evenNumbers)