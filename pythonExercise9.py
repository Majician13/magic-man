#Write a program that accepts sequence of lines as input and prints the lines after
#making all characters in the sentence capitalized.
#Suppose the following input is supplied to the program:
#Hello world
#Practice makes perfect
#Then, the output should be:
#HELLO WORLD
#PRACTICE MAKES PERFECT

print("enter sentences. press 'q' when done. ")

user = []
stop = "w"
while stop != "Q":
    userInput = input().upper()
    stop = userInput
    if userInput != "Q":
        user.append(userInput)
    
for sentence in user:
    print(sentence)


