guestList = []
guests = "1"

while guests != "0" :
    guests = input("What are the guest names? Enter '0' when done. ").capitalize()
    guestList.append(guests)
    
guestList.sort()
guestList.remove("0")

print(guestList)