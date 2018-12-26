import turtle
import os

#Screen set up
mainscreen = turtle.Screen()
mainscreen.bgcolor("black")
mainscreen.title("Space Invaders")

#Draw Border

border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color("white")
border_pen.penup()
border_pen.setposition(-300, -300)
border_pen.pendown()
border_pen.pensize(3)
for side in range(4):
    border_pen.fd(600)
    border_pen.lt(90)
border_pen.hideturtle()

# Make player

player = turtle.Turtle()
player.color("blue")
player.shape("triangle")
player.penup()
player.speed(0)
player.setposition(0, -250)



delay = input(" Press enter to finish.")