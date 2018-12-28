print("Do you have Celsius 'C' or Fahrenheit 'F'")
FC = input().upper()
print("What is the temp?")
temp = float(input())

if FC == "C":
    conv = (temp * (9/5)) + 32
    print("Temp in Fahrenheit is " + str(conv))
else:
    conv = (temp - 32) * (5/9)
    print("Temp in Celsius is " + str(conv))

