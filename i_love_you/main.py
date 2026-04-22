import turtle
import math
import time
import random

# 🖤 Screen setup
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("For You ❤️")
screen.tracer(0)

pen = turtle.Turtle()
pen.hideturtle()
pen.speed(0)

# 💖 Draw heart function
def draw_heart(scale, color):
    pen.color(color)
    pen.begin_fill()
    pen.penup()
    pen.goto(0, -100 * scale)
    pen.pendown()
    pen.setheading(140)
    pen.forward(180 * scale)
    pen.circle(-90 * scale, 200)
    pen.left(120)
    pen.circle(-90 * scale, 200)
    pen.forward(180 * scale)
    pen.end_fill()

# 🌈 Glow layers
def glow_heart(scale):
    glow_colors = ["#ff99cc", "#ff66b2", "#ff3385", "#ff0066"]
    
    for i, color in enumerate(glow_colors):
        draw_heart(scale + i*0.05, color)

# ✨ Sparkles
sparkles = []

def create_sparkles():
    for _ in range(15):
        x = random.randint(-200, 200)
        y = random.randint(-200, 200)
        sparkles.append((x, y))

def draw_sparkles():
    pen.penup()
    for (x, y) in sparkles:
        pen.goto(x, y)
        pen.dot(random.randint(2, 5), "white")

create_sparkles()

# 💓 Animation loop
for i in range(120):
    pen.clear()
    
    # heartbeat effect
    scale = 1 + 0.08 * math.sin(i * 0.2)
    
    glow_heart(scale)
    draw_sparkles()
    
    screen.update()
    time.sleep(0.03)

# 💌 Text
pen.penup()
pen.goto(0, -40)
pen.color("white")
pen.write("I Love You ❤️", align="center", font=("Verdana", 26, "bold"))

screen.update()
turtle.done()