P = 10000
n = 12
r = .08

t = int(input("How many years?  "))

interest = P * ((1 + (.08 / 12)) ** (12 * t))
print(interest)