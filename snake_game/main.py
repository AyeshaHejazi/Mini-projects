import turtle
import time
import random

# ---------------- WINDOW ----------------
wn = turtle.Screen()
wn.title("Neon Snake ✨")
wn.bgcolor("#050505")  # deep black
wn.setup(width=600, height=600)
wn.tracer(0)

# ---------------- VARIABLES ----------------
delay = 0.08
score = 0

# Neon colors (gradient effect)
colors = ["#00FFFF", "#00E5FF", "#00CCFF", "#00B2FF", "#0099FF"]

# ---------------- HEAD ----------------
head = turtle.Turtle()
head.shape("square")
head.color("#00FFFF")  # bright neon cyan
head.penup()
head.goto(0, 0)
head.direction = "stop"

# ---------------- FOOD ----------------
food = turtle.Turtle()
food.shape("circle")
food.color("#FF0055")  # neon pink/red
food.penup()
food.goto(0, 100)

segments = []

# ---------------- SCORE ----------------
pen = turtle.Turtle()
pen.hideturtle()
pen.color("#00FFFF")
pen.penup()
pen.goto(0, 260)

def update_score():
    pen.clear()
    pen.write(f"Score: {score}",
              align="center", font=("Courier", 16, "bold"))

update_score()

# ---------------- CONTROLS ----------------
def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_left():
    if head.direction != "right":
        head.direction = "left"

def go_right():
    if head.direction != "left":
        head.direction = "right"

wn.listen()
wn.onkeypress(go_up, "w")
wn.onkeypress(go_down, "s")
wn.onkeypress(go_left, "a")
wn.onkeypress(go_right, "d")

# ---------------- MOVE ----------------
def move():
    if head.direction == "up":
        head.sety(head.ycor() + 20)
    if head.direction == "down":
        head.sety(head.ycor() - 20)
    if head.direction == "left":
        head.setx(head.xcor() - 20)
    if head.direction == "right":
        head.setx(head.xcor() + 20)

# ---------------- GAME LOOP ----------------
while True:
    wn.update()

    move()

    # Border collision
    if abs(head.xcor()) > 290 or abs(head.ycor()) > 290:
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "stop"

        for s in segments:
            s.goto(1000, 1000)
        segments.clear()

        score = 0
        delay = 0.08
        update_score()

    # Food collision
    if head.distance(food) < 20:
        food.goto(random.randint(-280, 280), random.randint(-280, 280))

        # Create glowing segment
        new_segment = turtle.Turtle()
        new_segment.shape("square")
        new_segment.penup()

        # Assign gradient color
        color_index = len(segments) % len(colors)
        new_segment.color(colors[color_index])

        segments.append(new_segment)

        score += 10
        delay -= 0.001
        update_score()

    # Move body
    for i in range(len(segments)-1, 0, -1):
        segments[i].goto(segments[i-1].xcor(), segments[i-1].ycor())

    if segments:
        segments[0].goto(head.xcor(), head.ycor())

    # Self collision
    for seg in segments[1:]:
        if seg.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"

            for s in segments:
                s.goto(1000, 1000)
            segments.clear()

            score = 0
            delay = 0.08
            update_score()

    time.sleep(delay)

wn.mainloop()