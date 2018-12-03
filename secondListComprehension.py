import random

# Python program to illustrate the intersection 
# of two lists using set() method 
def intersection(a, b): 
    return list(set(a) & set(b)) 
  
# Driver Code 
a = random.sample(range(1,30), 12)
b = random.sample(range(1,30), 16)
print(a)
print(b)
print(intersection(a, b)) 