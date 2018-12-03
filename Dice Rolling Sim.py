import random
min = 1
max = 6

rollAgain = "yes"

while rollAgain == "yes" or rollAgain == "y" or rollAgain == "Y" or rollAgain == "Yes":
    print ("Rolling the dice...")
    print ("The values are...")
    print (random.randint(min, max))
    print (random.randint(min, max))
    
    rollAgain = input("Roll the dice again? Y/N")