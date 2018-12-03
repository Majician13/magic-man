import time
inventory = []
bathroomItems = ["soap", "deodorant", "towel", "toilet", "shower"]
kitchenItems = ["knife", "fork", "frying pan"]
            
def restart():
    restartChoice = input("Would you like to try again? 'y/n' ")
    if (restartChoice == "y"):
        main()
    else:
        print("Goodbye cruel world!!!")
        
def beginning():
    
    print("You awaken in a field.  It appears that a dark forest ")
    print("lies behind you.  There is an old house in front of you.")
    print("The sun is going down.  It's getting dark fast.")
    userChoice = input("What would you like to do?  'forest/house'")
    
    if (userChoice == "forest"):
        print("A terrible creature has devoured your flesh.")
        restart()
                
    elif (userChoice == "house"):
        hallway()
    else:
        print("You have already chosen incorrectly.  I hear Hello Kitty is a great game to play for someone with your...  Eh...  Capabilities. ")
        restart()
    
        
def hallway():
    
    print("You enter into a long, dark hallway.  There are six doors, three on each wall '1, 2, 3 on left, 4, 5, 6 on right'")
    print("and a seventh door '7' is at ")
    print("the other end of the hallway from where you are now.")
    roomChoice = int(input("Which door would you like to choose? '1-7'"))
    if (roomChoice == 1):
        bathroomChoice = input("You have entered the bathroom.  I know it is frightening here, but must you relieve yourself now? 'y/n' ")
        if (bathroomChoice == "y"):
            print("OK.  OK.  I'll wait.  HURRY UP!")
            time.sleep(5)
            roomOne()
        else:
            roomOne()
    elif (roomChoice == 2):
        roomTwo()
        

def roomOne():
    

    print("Looking around the room, you see ")
    print(bathroomItems)
    
    bathroomChoices()    

def bathroomChoices():
    bathroomChoice = input("Would you like to try to take anything from this room? 'y/n' ")
    if (bathroomChoice == "y"):
        print(bathroomItems)
        takeBathroom = input("What would you like to take? ")
        if (takeBathroom == "toilet" or takeBathroom == "shower"):
            print("Here are the items in the bathroom.  Unfortunately, the toilet and shower are too heavy to carry around. Please try again. ")
            roomOne()
        elif (takeBathroom == "soap"):
            bathroomItems.remove(takeBathroom)
            inventory.append(takeBathroom)
            print("You took ")
            print(takeBathroom)
            print("Your inventory" )
            print(inventory)
            bathroomChoices()
        elif (takeBathroom == "deodorant"):
            print("Oh thank God.  I thought I'd never get a break from that God-awful smell.  What's that?  You aren't going to use it ")
            print("on yourself right away?  Forget I said anything then.")
            bathroomItems.remove(takeBathroom)
            inventory.append(takeBathroom)
            print("You took ")
            print(takeBathroom)
            print("Your inventory" )
            print(inventory)
            bathroomChoices()
        elif (takeBathroom == "towel"):
            print("Very wise choice.  This is a very scary house.  You may need that for your pants a bit later. It is also good ")
            print("to always know where your towel is, as we learned from the Hitchhiker's Guide to the Galaxy. ")
            bathroomItems.remove(takeBathroom)
            inventory.append(takeBathroom)
            print("You took ")
            print(takeBathroom)
            print("Your inventory" )
            print(inventory)
            bathroomChoices()
        else:
            print("It's beginning to become clear that A: You don't read very good.  B: You aren't that bright if you don't read well and you chose to ")
            print("play a text based game. ")
            bathroomChoices()
    elif (bathroomChoice == "n"):
        leaveBathroom = input("Are you ready to leave the bathroom now? 'y/n' ")
        if (leaveBathroom == "y"):
            hallway()
        elif (leaveBathroom == "n"):
            scratchingChoice = input("Would you like to examine the scratching noises at the window? 'y/n'")
            if (scratchingChoice == "y"):
                bathroomWindow()
            else:
                bathroomChoices()
        else:
            print("Again?  Really?  Do you have the bladder of a child?  Is this really that scary?  By the way, look out for th...")
            print("You took too long using the bathroom and the beast has broken into the house and devoured your soul.  You are doomed.")
            restart()
    else:
        print("Not the brightest star in the galaxy, are you? ")
        bathroomChoices()
    
def bathroomWindow():
    print("Looking at the window, you see complete darkness outside.  Suddenly there is a bright flash of lightning. ")
    print("Prior to the light blinding your eyes and the thunderous sound that follows, you appear to be able to make out a shadow of ")
    print("something that doesn't appear to be quite human.  The only details you can make out are two very sharp yellow eyes staring ")
    print("back at you. ")
    windowChoice = input("Would you like to more closely inspect the window where this hellish beast is, or would you rather run out of the room screaming and hoping you don't wet yourself? 'look/run'")
    if (windowChoice == "look"):
        print("WOW!  Have you never seen a horror movie?  Have you lost your head?  Umm...  Actually, you did lose your ")
        print("head.  While leaning in closer to inspect the window and what was outside, the beast quickly smashed his ")
        print("clawed hand through the glass, grabbed the back of your head, and effortlessly pulled it clean off of your ")
        print("neck.  The good news is that you won't have to worry about that nasty beast stalking you anymore. ")
        restart()
    elif (windowChoice == "run"):
        print("You run out of the bathroom screaming and flailing your arms behind you.  Unfortunately, your hopes of not wetting ")
        print("yourself did not carry through to your bladder. ")
        hallway()
        
def roomTwo():
    print("You walk into what used to be a beautiful, large kitchen.  Now it's covered with cobwebs.  As you walk in, you believe ")
    print("you see, out of the corner of your eye, a shadow vanishing in a dark corner of the room. ")
    kitchenChoice = input("Would you like to look around, or would you rather do the opposite of what you know you should do and chase the shadow? 'look/chase'")
    if (kitchenChoice == "look"):
        print("You look around the kitchen and take note of the items you wish to steal from this house that doesn't belong to you. ")
        print(kitchenItems)
        kitchenChoices()
    elif (kitchenChoice == "chase"):
        print("The human intellect, or lack thereof, never ceases to amaze me.  You carefully sneak over to the darkness of the corner ")
        print("where you see a pair of yellow eyes staring back at you.  Before you can even think a thought, or scream for that matter, ")
        print("the beast has already pounced and commenced eating your puny brain, which doesn't even whet his appetite. Congratulations ")
        print("you are now deceased.  Welcome to the afterlife.  It appears they'll just let anyone in here. ")
        restart()
        
def kitchenChoices():
    kitchenChoice = input("Would you like to try to take anything from this room? 'y/n' ")
    if (kitchenChoice == "y"):
        print(kitchenItems)
        takeKitchen = input("What would you like to take? ")
        if (takeKitchen == "knife"):
            kitchenItems.remove(takeKitchen)
            inventory.append(takeKitchen)
            print("You pick up the knife by the blade, cutting yourself. ")
            print("You took ")
            print(takeKitchen)
            print("Your inventory" )
            print(inventory)
            kitchenChoices()
        elif (takeKitchen == "fork"):
            kitchenItems.remove(takeKitchen)
            inventory.append(takeKitchen)
            print("You pick up the fork and resist the very strong urge to jab it into your eye. ")
            print("You took ")
            print(takeKitchen)
            print("Your inventory" )
            print(inventory)
            kitchenChoices()
        elif (takeKitchen == "frying pan"):
            print("Interesting.  Is food really all you can think about at a time like this? ")
            kitchenItems.remove(takeKitchen)
            inventory.append(takeKitchen)
            print("You took ")
            print(takeKitchen)
            print("Your inventory" )
            print(inventory)
            kitchenChoices()
        else:
            print("It's beginning to become clear that A: You don't read very good.  B: You aren't that bright if you don't read well and you chose to ")
            print("play a text based game. ")
            kitchenChoices()
    if (kitchenChoice == "n"):
        leaveKitchen = input("Are you ready to leave the kitchen now? 'y/n' ")
        if (leaveKitchen == "y"):
            hallway()
        elif (leaveKitchen == "n"):
            print("You continue to stare into the kitchen.  The whole time, wondering if that shadow was real.")
            kitchenChoiceTwo = input("Would you like to continue standing in the kitchen, stealing, I mean, gathering more items, or are you ready to leave the kitchen now? 'stand/steal/leave' ")
            if (kitchenChoiceTwo == "stand"):
                kitchenChoicesTwo()
            elif (kitchenChoiceTwo == "steal"):
                kitchenChoices()
            elif (kitchenChoiceTwo == "leave"):
                hallway()
            else:
                kitchenChoices()
        else:
            print("Congratulations.  I'm ensuring that the beast eats the meat off of every bone in your body because you failed ")
            print("to read the directions clearly one too many times.  You are dead.  It's not just a flesh wound. ")
            restart()
    else:
        print("Not the brightest star in the galaxy, are you? ")
        kitchenChoices()
def kitchenChoicesTwo():
    kitchenChoiceTwo = input("Would you like to continue standing in the kitchen, stealing, I mean, gathering more items, or are you ready to leave the kitchen now? 'stand/steal/leave' ")
    if (kitchenChoiceTwo == "stand"):
        print("You gallant stand with your hands on your hips, surveying everything you don't own.")
        kitchenChoicesTwo()
    elif (kitchenChoiceTwo == "steal"):
        print("Oh, using your five finger discount I see.  Fine. If you must. ")
        kitchenChoices()
    elif (kitchenChoiceTwo == "leave"):
        print("Scratching your head, you finally decide to leave the kitchen with most of your fingers in tact. ")
        hallway()
    else:
        print("I'm honestly not finding this funny anymore.  The reality of how ignorant you are is starting to get quite sad so ")
        print("I have decided to put you out of your misery and save myself a few tears in the process. ")
        restart()

def main():
    
    playerName = input("What is your name?  ")
    print("Welcome {}.  You are in grave danger." .format(playerName.upper()))
    beginning()
    
if __name__ == '__main__':
    main()

    

    