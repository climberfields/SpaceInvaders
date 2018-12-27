import turtle
import os
import math
import random

#Screen set up
mainscreen = turtle.Screen()
mainscreen.bgcolor("black")
mainscreen.title("Space Invaders")

#register shapes
turtle.register_shape("invader.gif")
turtle.register_shape("spaceship.gif")

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

#Make Score
score = 0

#Draw Score
score_pen = turtle.Turtle()
score_pen.speed(0)
score_pen.color("white")
score_pen.penup()
score_pen.setposition(-290, 280)
scorestring = "Score :%s " %score
score_pen.write(scorestring, False, align= "left", font=("Arial", 14, "normal"))
# Make player

player = turtle.Turtle()
player.color("blue")
# player.shape("spaceship.gif")
player.shape("triangle")
player.penup()
player.speed(0)
player.setposition(0, -250)
player.setheading(90)

playerspeed = 15

# Aliens

enemy = turtle.Turtle()
enemy.color("red")
# enemy.shape("invader.gif")
enemy.shape("circle")
enemy.penup()
enemy.speed(0)
enemy.setposition(-200, 250)

enemyspeed = 2

#Number of enemies
number_of_enemies = 5
#Create an empty list of enemies
enemies = []

#Add to the list
for i in range(number_of_enemies):
    enemies.append(turtle.Turtle())

for enemy in enemies:
    enemy.color("red")
    enemy.shape("circle")
    enemy.penup()
    enemy.speed(0)
    x = random.randint(-200, 200)
    y = random.randint(100, 250)
    enemy.setposition(x, y)

enemyspeed = 2

# Bullet state
# Player Bullet
bullet = turtle.Turtle()
bullet.color("yellow")
bullet.shape("triangle")
bullet.penup()
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(0.5, 0.5)
bullet.hideturtle()

bulletspeed = 20

#ready
bulletstate = "ready"
#fire


# Moving the player

def move_left():
    x = player.xcor()
    x -= playerspeed
    if x < -280:
        x = -280
    player.setx(x)

def move_right():
    x = player.xcor()
    x += playerspeed
    if x > 280:
        x = 280
    player.setx(x)


def fire_bullet():
    global bulletstate
    if bulletstate == "ready":
        bulletstate = "fire"
        x = player.xcor()
        y = player.ycor() + 10
        bullet.setposition(x, y)
        bullet.showturtle()

def isCollision(t1, t2):
    distance = math.sqrt(math.pow(t1.xcor() - t2.xcor(),2) + math.pow(t1.ycor()-t2.ycor(), 2))
    if distance < 15:
        return True
    else:
        return False


#Keyboard Bindings
turtle.listen()
turtle.onkey(move_left, "Left")
turtle.onkey(move_right, "Right")
turtle.onkey(fire_bullet, "space")




#Game Loop
while True:
    x = enemy.xcor()
    x += enemyspeed
    enemy.setx(x)

    for enemy in enemies:
        x= enemy.xcor()
        x += enemyspeed
        enemy.setx(x)

# Alien back and forth movement
        if enemy.xcor() > 280:
            for e in enemies:
                y = enemy.ycor()
                y -= 40
                e.sety(y)
            enemyspeed *= -1

        if enemy.xcor() < -280:
            for e in enemies:
                y = enemy.ycor()
                y -= 40
                e.sety(y)
            enemyspeed *= -1
    #checking for bullet collision
        if isCollision(bullet, enemy):
            #Reset Bullet
            bullet.hideturtle()
            bulletstate = "ready"
            bullet.setposition(0, -400)
            #Reset Enemy
            enemy.setposition(-200, 250)
            #adding score
            score += 10
            scorestring = "Score: %s" %score
            score_pen.clear()
            score_pen.write(scorestring, False, align= "left", font=("Arial", 14, "normal"))

        if isCollision(enemy, player):
            player.hideturtle()
            enemy.hideturtle()
            print ("Game Over")
            break
#bullet movement
    if bulletstate == "fire":
        y = bullet.ycor()
        y += bulletspeed
        bullet.sety(y)

    if bullet.ycor() > 275:
        bullet.hideturtle()
        bulletstate = "ready"


delay = input(" Press enter to finish.")