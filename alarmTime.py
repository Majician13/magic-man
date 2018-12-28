print("What time is it now '0 - 24'")
hours = int(input())
print("how many hours from now for alarm?")
alarm = int(input())

alarmTime = int((hours + alarm)%24) 
print(alarmTime)