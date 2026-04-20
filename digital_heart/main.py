import turtle 
import math
#Screen setup
screen = turtle.Screen()
screen.bgcolor("black")
#Turtle setup
heart = turtle.Turtle()
heart.speed(3) 
turtle.shape("turtle")
heart.color("red")
heart.width(2)

heart.hideturtle()
#Function to draw a heart
def draw_heart():
    heart.penup()
    for t in range(0, 360):
        x = 16 * math.sin(math.radians(t)) ** 3
        y = 13 * math.cos(math.radians(t)) - 5 * math.cos(math.radians(2 * t)) - 2 * math.cos(math.radians(3 * t)) - math.cos(math.radians(4 * t))
        heart.goto(x*15, y*15)
        heart.pendown()
#call the function to draw the heart 
import time       
while True:
    draw_heart()
    heart.clear()
    time.sleep(0.1)

    