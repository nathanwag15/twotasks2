#Target Practice
#Nathan Wagstaff
#1/31/2020

#The user will put in the coordinates to fire a point on the target.

#user instructions and input
print("Target Practice Fun!")
xPos = input("Enter X coordinate: ")
yPos = input("Enter Y coordinate: ")
xPos = int(xPos)
yPos = int(yPos)

#general turtle setup

import turtle

turtle.speed(1)

#position pen
turtle.penup()
turtle.goto(0, -200)
turtle.pendown()

#defining the radius
radius = 200

#outer circle
turtle.color("yellow")
turtle.fillcolor("yellow")
turtle.begin_fill()
turtle.circle(radius)
turtle.end_fill()

#position pen
turtle.penup()
turtle.goto(0, -150)
turtle.pendown()

#radius reset
radius = radius - 50

#1st middle circle
turtle.color("pink")
turtle.fillcolor("pink")
turtle.begin_fill()
turtle.circle(radius)
turtle.end_fill()

#position pen
turtle.penup()
turtle.goto(0, -100)
turtle.pendown()

#radius reset
radius = radius - 50

#2nd middle circle
turtle.color("orange")
turtle.fillcolor("orange")
turtle.begin_fill()
turtle.circle(radius)
turtle.end_fill()

#position pen
turtle.penup()
turtle.goto(0, -50)
turtle.pendown()

#radius reset
radius = radius - 50

#2nd middle circle
turtle.color("blue")
turtle.fillcolor("blue")
turtle.begin_fill()
turtle.circle(radius)
turtle.end_fill()

#position pen
turtle.penup()
turtle.goto(xPos, yPos)
turtle.pendown()

#draw circle
turtle.color("black")
turtle.fillcolor("black")
turtle.begin_fill()
turtle.circle(3)
turtle.end_fill()

turtle.done()

