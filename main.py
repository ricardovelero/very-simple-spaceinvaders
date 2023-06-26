import turtle
import os
from scoreboard import Scoreboard

score = Scoreboard(lives=5)

# Set up the screen
window = turtle.Screen()
window.title("Space Invaders")
window.bgcolor("black")
window.setup(width=800, height=600)
window.tracer(0)

# Create the player
player = turtle.Turtle()
player.color("blue")
player.shape("triangle")
player.penup()
player.speed(0)
player.goto(0, -250)
player.direction = "stop"

# Create the enemy
enemy = turtle.Turtle()
enemy.color("red")
enemy.shape("circle")
enemy.penup()
enemy.speed(0)
enemy.goto(0, 250)

# Create the bullet
bullet = turtle.Turtle()
bullet.color("yellow")
bullet.shape("triangle")
bullet.penup()
bullet.speed(0)
bullet.shapesize(0.5, 0.5)
bullet.hideturtle()
bullet.goto(0, -400)
bullet.state = "ready"

# Define the player's movement


def move_left():
    player.direction = "left"


def move_right():
    player.direction = "right"


def stop_player():
    player.direction = "stop"


def fire_bullet():
    print("fire")
    if bullet.state == "ready":
        bullet.state = "fire"
        x = player.xcor()
        y = player.ycor() + 10
        bullet.goto(x, y)
        bullet.showturtle()


# Keyboard bindings
window.listen()
window.onkeypress(move_left, "Left")
window.onkeypress(move_right, "Right")
window.onkeypress(fire_bullet, "space")
window.onkeyrelease(stop_player, "Left")
window.onkeyrelease(stop_player, "Right")

# Define the enemy's movement
enemy_speed = 2

# Main game loop
while True:
    window.update()

    # Move the player
    if player.direction == "left":
        x = player.xcor()
        x -= 3
        if x < -380:
            x = -380
        player.setx(x)

    if player.direction == "right":
        x = player.xcor()
        x += 3
        if x > 380:
            x = 380
        player.setx(x)

    # Move the enemy
    x = enemy.xcor()
    x += enemy_speed
    enemy.setx(x)

    # Reverse enemy direction and move down
    if enemy.xcor() > 380:
        enemy_speed *= -1
        y = enemy.ycor()
        y -= 40
        enemy.sety(y)

    if enemy.xcor() < -380:
        enemy_speed *= -1
        y = enemy.ycor()
        y -= 40
        enemy.sety(y)

    # Move the bullet
    if bullet.state == "fire":
        y = bullet.ycor()
        y += 5
        bullet.sety(y)

    # Check for bullet collision with enemy
    if bullet.distance(enemy) < 20:
        score.increase_score()
        bullet.hideturtle()
        bullet.state = "ready"
        bullet.goto(0, -400)
        enemy.goto(0, 250)

    # Check if bullet passed screen
    if bullet.ycor() >= 300:
        bullet.hideturtle()
        bullet.state = "ready"
        bullet.goto(0, -400)

    # Check for game over
    if enemy.ycor() < -250:
        player.hideturtle()
        enemy.hideturtle()
        bullet.hideturtle()
        print("Game Over")
        break
