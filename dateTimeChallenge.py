import datetime

currentDate = datetime.date.today()
deadLine = input("What's your deadline? mm/dd/yyyy \n")
deadLineDate = datetime.datetime.strptime(deadLine, "%m/%d/%Y").date()

difference = (deadLineDate - currentDate)

weeks = (difference.days / 7)

print(difference.days)

#Prints weeks with decimal places IE: 4.571428
print(weeks)

#Prints weeks with no decimal places
result = (deadLineDate-currentDate).days//7
print(result)