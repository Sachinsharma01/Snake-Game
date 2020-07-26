# Snake game
import turtle
import time
import random

delay = 0.01

# Set up the Screen
w = turtle.Screen()
w.title("Snake Game!!")
w.bgcolor("white")
w.setup(width=600, height=600)
w.tracer(0)  # turn off the screen updates

# Create a snake head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("red")
head.penup()
head.goto(0, 0)
head.direction = "stop"

# Snake Food
food = turtle.Turtle()
food.speed(0)
food.shape("square")
food.color("black")
food.penup()
food.goto(0, 100)

segment = []

# Score
score = 0
highScore = 0

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("black")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score : 0   High Score : 0", align="center", font=("Courier", 18, "normal"))


# Functions
def go_up():
    if head.direction != "down":
        head.direction = "up"


def go_down():
    if head.direction != "up":
        head.direction = "down"


def go_right():
    if head.direction != "left":
        head.direction = "right"


def go_left():
    if head.direction != "right":
        head.direction = "left"


def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)


# Keyboard bindings
w.listen()
w.onkeypress(go_up, "w")
w.onkeypress(go_down, "s")
w.onkeypress(go_right, "d")
w.onkeypress(go_left, "a")

# Main Game Loop
while True:
    w.update()

    # Check for a collision with border
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "stop"

        # Hide the segment
        for j in segment:
            j.goto(1000, 1000)
            # Clean the Segment list
        segment.clear()

        # Reset the score
        score = 0
        pen.clear()
        pen.write("Score : {}   High Score : {}".format(score, highScore), align="center",
                  font=("Courier", 18, "normal"))

    # Check for collision with food
    if head.distance(food) < 20:
        # move food to random location
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x, y)

        # Add a Segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("red")
        new_segment.penup()
        segment.append(new_segment)

        score += 10
        if score > highScore:
            highScore = score
        pen.clear()
        pen.write("Score : {}   High Score : {}".format(score, highScore), align="center",
                  font=("Courier", 18, "normal"))

    # Move the end segment first in reverse order
    for i in range(len(segment) - 1, 0, -1):
        x = segment[i - 1].xcor()
        y = segment[i - 1].ycor()
        segment[i].goto(x, y)

    # Move segment 0 to the head
    if len(segment) > 0:
        x = head.xcor()
        y = head.ycor()
        segment[0].goto(x, y)

    move()

    # Check for head collisions
    for k in segment:
        if k.distance(head) < 20:
            head.goto(0, 0)
            head.direction = "stop"

            for j in segment:
                j.goto(1000, 1000)
                # Clean the Segment list
            segment.clear()

            # Reset the Score
            score = 0
            pen.clear()
            pen.write("Score : {}   High Score : {}".format(score, highScore), align="center",
                      font=("Courier", 18, "normal"))
    time.sleep(delay)  
w.mainloop()
