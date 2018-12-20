import turtle


nbrsides = int(input("How many sides do you want?  "))
               
for steps in range(nbrsides):
    turtle.forward(50)
    turtle.right(360/nbrsides)
    for moreSteps in range(nbrsides):
        turtle.forward(25)
        turtle.right(360/nbrsides)
        