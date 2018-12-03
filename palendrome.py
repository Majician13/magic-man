name = input("Type a word  ")
a = name[0::]
b = name[::-1]

if a == b:
    print("This is a palendrome.  ")
else:
    print("This is NOT a palendrom.  ")