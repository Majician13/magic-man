days = {"SU" : 0, "M" : 1,
        "TU" : 2, "W" : 3,
        "TH" : 4, "F" : 5,
        "SA" : 6
        }

print("what day are you leaving?")
dayLeaving = input().upper()

print("length of stay?")
vacaLen = int(input())

if dayLeaving in days:
    dayLeaving == int(days[dayLeaving])

vacaReturn = (int(days[dayLeaving]) + int(vacaLen)) % 7


print(list(days.keys())[list(days.values()).index(vacaReturn)])