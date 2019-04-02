# Name: Rachada Chairangsaris (Bay)
# Assignment: Lab 6, Turtle (Draw Letters)
# Date: March 14th, 2019

import turtle

turtle.setup(900,600)

window = turtle.Screen()

window.title('Draw X, Y, Z, TURTLE Program')

# creat an object Turtle
the_turtle = turtle.getturtle()


turtle.colormode(255)
the_turtle.pencolor(83, 153, 81)
the_turtle.pensize(15)

def drawX():
    # X
    the_turtle.pencolor(247, 84, 195)
    the_turtle.shape('circle')
    the_turtle.penup()
    the_turtle.setposition(-170,180)
    the_turtle.pendown()
    the_turtle.right(45)
    the_turtle.forward(380)
    the_turtle.penup()
    the_turtle.setposition(100,180)
    the_turtle.pendown()
    the_turtle.right(90)
    the_turtle.forward(380)
    

def drawY():
    # Y
    the_turtle.pencolor(247, 84, 195)
    the_turtle.shape('circle')
    the_turtle.penup()
    the_turtle.setposition(-120,180)
    the_turtle.pendown()
    the_turtle.right(55)
    the_turtle.forward(180)
    the_turtle.penup()
    the_turtle.setposition(95,180)
    the_turtle.pendown()
    the_turtle.right(72)
    the_turtle.forward(380)


def drawZ():
    # Z
    the_turtle.pencolor(247, 84, 195)
    the_turtle.shape('circle')
    the_turtle.penup()
    the_turtle.setposition(-170,180)
    the_turtle.pendown()
    the_turtle.forward(300)
    the_turtle.right(135)
    the_turtle.forward(400)
    the_turtle.left(135)
    the_turtle.forward(300)


def drawTurtle():
    the_turtle = turtle.getturtle()
    # T
    the_turtle.shape('turtle')
    the_turtle.penup()
    the_turtle.setposition(-380,120)
    the_turtle.pendown()
    the_turtle.forward(100)
    the_turtle.right(180)
    the_turtle.forward(50)
    the_turtle.left(90)
    the_turtle.forward(150)

    # U
    the_turtle.shape('circle')
    the_turtle.penup()
    the_turtle.setposition(-250,120)
    the_turtle.pendown()
    the_turtle.forward(140)
    the_turtle.left(45)
    the_turtle.forward(20)
    the_turtle.left(45)
    the_turtle.forward(50)
    the_turtle.left(45)
    the_turtle.forward(20)
    the_turtle.left(45)
    the_turtle.forward(140)

    # R
    the_turtle.shape('triangle')
    the_turtle.penup()
    the_turtle.setposition(-130,120)
    the_turtle.pendown()
    the_turtle.left(180)
    the_turtle.forward(155)
    the_turtle.penup()
    the_turtle.setposition(-130,120)
    the_turtle.pendown()
    the_turtle.left(90)
    the_turtle.forward(65)
    the_turtle.right(45)
    the_turtle.forward(20)
    the_turtle.right(45)
    the_turtle.forward(30)
    the_turtle.right(45)
    the_turtle.forward(20)
    the_turtle.right(45)
    the_turtle.forward(65)
    the_turtle.left(130)
    the_turtle.forward(125)

    # T
    the_turtle.shape('square')
    the_turtle.penup()
    the_turtle.setposition(-20,120)
    the_turtle.pendown()
    the_turtle.left(50)
    the_turtle.forward(100)
    the_turtle.right(180)
    the_turtle.forward(50)
    the_turtle.left(90)
    the_turtle.forward(150)

    # L
    the_turtle.shape('classic')
    the_turtle.penup()
    the_turtle.setposition(110,120)
    the_turtle.pendown()
    the_turtle.forward(150)
    the_turtle.left(90)
    the_turtle.forward(70)

    # E
    the_turtle.shape('turtle')
    the_turtle.penup()
    the_turtle.setposition(210,120)
    the_turtle.pendown()
    the_turtle.right(90)
    the_turtle.forward(150)
    the_turtle.penup()
    the_turtle.setposition(210,120)
    the_turtle.pendown()
    the_turtle.left(90)
    the_turtle.forward(70)
    the_turtle.penup()
    the_turtle.setposition(210,50)
    the_turtle.pendown()
    the_turtle.forward(70)
    the_turtle.penup()
    the_turtle.setposition(210,-30)
    the_turtle.pendown()
    the_turtle.forward(70)

    # underline
    the_turtle.hideturtle()
    the_turtle.pencolor(226, 54, 54)
    the_turtle.pensize(12)
    the_turtle.penup()
    the_turtle.setposition(-390,-70)
    the_turtle.pendown()
    the_turtle.forward(750)
    the_turtle.right(150)
    the_turtle.forward(130)
    the_turtle.left(150)
    the_turtle.forward(100)
    the_turtle.penup()
    the_turtle.setposition(380,-135)
    the_turtle.pendown()
    the_turtle.pensize(18)
    the_turtle.forward(3)
    

which = ""
while which != 'x' and which != 'y' and which != 'z' and which != 'turtle':
    which = input("enter x, y, z, or turtle to draw the letter(s): ").lower()
    

if which == 'x':
    drawX()
elif which == 'y':
    drawY()
elif which == 'z':
    drawZ()
else:
    drawTurtle()
