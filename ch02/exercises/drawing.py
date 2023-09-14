import turtle 

sides = int(input("How many sides do you want? "))
length = int(input("How long do you want each side to be? "))
angle = 360 / sides
for i in range(sides):
    turtle.forward(length)
    turtle.left(angle)
    

donatello = turtle.Turtle()
screen = turtle.Screen()
donatello.color("purple")
turtle.done()
turtle.Screen().exitonclick

