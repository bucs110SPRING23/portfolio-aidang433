
#Part A
import turtle  # 1. import modules
import random
m = random.randrange(1,101) #x is or movement variable for the race
l = random.randrange(1,101) #and y
window = turtle.Screen()  # 2.  Create a screen
window.bgcolor("lightblue")

michelangelo = turtle.Turtle()  # 3.  Create two turtles
leonardo = turtle.Turtle()
michelangelo.color("orange")
leonardo.color("blue")
michelangelo.shape("turtle")
leonardo.shape("turtle")

michelangelo.up()  # 4. Pick up the pen so we don’t get lines
leonardo.up()
michelangelo.goto(-100, 20)
leonardo.goto(-100, -20)
#race 1
michelangelo.forward(m)
leonardo.forward(l)
michelangelo.goto(-100, 20)
leonardo.goto(-100, -20)
#race 2
for i in range(random.randrange(1,11)) :
    michelangelo.forward(random.randrange(1,101))
    leonardo.forward(random.randrange(1,101))

michelangelo.goto(-100, 20)
leonardo.goto(-100, -20)
window.exitonclick()




#Part B
import pygame
import math

pygame.init()
display = pygame.display.set_mode([500,500])
points =list()
num_sides = list[3,4,6,20,100,360]
side_length = 50
xpos = []
ypos = []

for i in range(num_sides):
    angle = 360/num_sides[i]
    radians = math.radians(angle*i)
    x = xpos + side_length * math.cos(radians)
    y = ypos + side_length * math.sin(radians)
    xpos.append(x)
    ypos.append(y)
    pygame.draw.polygon(display,"red",points)
    pygame.display.flip()
    pygame.time.wait(2000)
display.fill("black")
pygame.display.flip()
