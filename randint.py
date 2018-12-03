import random


x = 1
while x == 1:
    
    num = random.randint(1, 9)
    
    print(num)
    
    usrGuess = int(input("Guess the number "))
    print(usrGuess)
    i = 1
    
    while (usrGuess != num):
        i += 1
        if (usrGuess > num):
            usrGuess = int(input("Guess lower "))
            print(usrGuess)
        elif (usrGuess < num):
            usrGuess = int(input("Guess higher "))
            print(usrGuess)
        
        if (usrGuess == num):
            exit = str(input('Do you want to play another game, yes or no?\n'))
            if (exit == "no"):
                print('game over.')
                break
            
        
        
                
    if (exit == "no"):
        print("You guessed " + str(i) + " times")
        break 
        