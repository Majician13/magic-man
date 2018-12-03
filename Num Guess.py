import random

num = random.randint(1, 99)
n = int(input("I have a number, please guess what it is. \n" ))

while n != num:
    if n > num:
        n = int(input("Guess a lower number please."))       
    elif n < num:
        n = int(input("Guess a higher number please."))
        
print("Congratulations!  You guessed my number.")