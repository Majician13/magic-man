#Write a program that computes the net amount of a bank account based a transaction
#log from console input. The transaction log format is shown as following:
#D 100
#W 200
#D means deposit while W means withdrawal.
#Suppose the following input is supplied to the program:
#D 300
#D 300
#W 200
#D 100
#Then, the output should be:
#500

d = {"D": 0, "W": 0}
x = 0
while x != 1:
    print("Enter 'D' for deposit or 'W' for withdrawal.")
    depWith = input().upper()
    print("Enter amount, if done, type 1")
    amt = int(input())
    
    x = amt
    
    if depWith == "D":
        d["D"] += amt
    if depWith == "W":
        d["W"] += amt
    else:
        pass
    
print(d)
total = d["D"] - d["W"]
print(total)