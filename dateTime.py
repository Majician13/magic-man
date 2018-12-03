import datetime

#Print todays date.
currentDate = datetime.date.today()
print(currentDate.strftime("%b %d, %Y"))

#Print today's date in Python format, Just the month, just the Year.
print(currentDate)
print(currentDate.month)
print(currentDate.year)

#Print a special sentence including different aspects of the date.
print(currentDate.strftime("Please attend our event %A, %B %d in the year %Y"))

#Ask for and print someone's b-day
#Please uncomment lines 17, 18, 23, 25, 26 to use this section
birthday = input("What's your birthday? mm/dd/yyyy \n")
birthdate = datetime.datetime.strptime(birthday, "%m/%d/%Y").date()
#Why did we list datetime twice?
#because we are calling the strptime function
#Which is part of the datetime class
#which is in the datetime module
print("Your birth month is " + birthdate.strftime("%B"))

difference = (currentDate - birthdate)
print(difference.days)


#Time from here on
currentTime = datetime.datetime.now()
print(datetime.datetime.strftime(currentTime, "%I:%M %p"))
print(currentTime)
print(currentTime.hour)
print(currentTime.minute)
print(currentTime.second)
