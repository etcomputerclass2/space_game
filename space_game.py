import turtle
import time
import random

delay = 0.1

# Score
score = 0
deaths = 0
high_score = 0
pe = turtle.Turtle()
pe.speed(0)
pe.shape("square")
pe.color("white")
pe.penup()
pe.hideturtle()
pe.goto(350, 300)
pe.write("Forward-w, Right-d, Left-a, Down-s, cannot go backwards, shoot-space", align="right", font=("Courier", 16, "normal"))

# Set up the screen
wn = turtle.Screen()
wn.title("Shooter Game by Ethan (Forked from @TokyoEdTech)")
wn.bgcolor("blue")
wn.setup(width=1900, height=1000)
wn.tracer(0) # Turns off the screen updates

# Snake head
head = turtle.Turtle()
head.speed(0)
head.shape("circle")
head.color("white")
head.penup()
head.goto(0,0)
head.direction = "stop"

shot = turtle.Turtle()
shot.speed(0)
shot.shape("circle")
shot.color("red")
shot.penup()
shot.goto(10000,10000)
shot.direction = "stop"

sot = turtle.Turtle()
sot.speed(0)
sot.shape("circle")
sot.color("green")
sot.penup()
sot.goto(10000,10000)
sot.direction = "stop"

comet = turtle.Turtle()
comet.speed(0)
comet.shape("circle")
comet.color("brown")
comet.penup()
comet.goto(10000,10000)
comet.direction = "stop"

comt = turtle.Turtle()
comt.speed(0)
comt.shape("circle")
comt.color("brown")
comt.penup()
comt.goto(10000,10000)
comt.shapesize(2,2)
comt.direction = "stop"

cmet = turtle.Turtle()
cmet.speed(0)
cmet.shape("circle")
cmet.color("brown")
cmet.penup()
cmet.goto(10000,10000)
cmet.shapesize(3,3)
cmet.direction = "stop"

shstar = turtle.Turtle()
shstar.speed(0)
shstar.shape("circle")
shstar.color("yellow")
shstar.penup()
shstar.goto(10000,10000)
shstar.direction = "stop"

# Snake food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("grey")
food.penup()
x = random.randint(-900, 900)
y = random.randint(-450, 450)
food.goto(x,y)
food.direction = "stop"

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score: 0  High Score: 0", align="center", font=("Courier", 24, "normal"))

# Functions
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

def shoot():
    if head.direction != "stop":
        shot.sety(head.ycor())
        shot.setx(head.xcor())
        shot.direction = head.direction

def moveshot():
    if shot.direction == "up":
        y = shot.ycor()
        shot.sety(y + 50)

    if shot.direction == "down":
        y = shot.ycor()
        shot.sety(y - 50)

    if shot.direction == "left":
        x = shot.xcor()
        shot.setx(x - 50)

    if shot.direction == "right":
        x = shot.xcor()
        shot.setx(x + 50)

def sotd():
    if sot.xcor() > 900 or sot.xcor() < -900 or sot.ycor() > 450 or sot.ycor() < -450:
        sot.sety(food.ycor())
        sot.setx(food.xcor())
        sot.direction = food.direction

def movesot():
    if sot.direction == "up":
        y = sot.ycor()
        sot.sety(y + 50)

    if sot.direction == "down":
        y = sot.ycor()
        sot.sety(y - 50)

    if sot.direction == "left":
        x = sot.xcor()
        sot.setx(x - 50)

    if sot.direction == "right":
        x = sot.xcor()
        sot.setx(x + 50)

def cometd():
    if comet.xcor() > 900 or comet.xcor() < -900 or comet.ycor() > 450 or comet.ycor() < -450:
        comet.sety(500)
        x = random.randint(-900, 900)
        comet.setx(x)
        comet.direction = food.direction

def movecomet():
    y = comet.ycor()
    comet.sety(y - 50)

def shstard():
    if shstar.xcor() > 900 or shstar.xcor() < -900 or shstar.ycor() > 450 or shstar.ycor() < -450:
        shstar.setx(-950)
        y = random.randint(-450, 450)
        shstar.sety(y)
        shstar.direction = food.direction

def moveshstar():
    x = shstar.xcor()
    shstar.setx(x + 50)

def cmetd():
    if cmet.xcor() > 900 or cmet.xcor() < -900 or cmet.ycor() > 450 or cmet.ycor() < -450:
        cmet.sety(475)
        x = random.randint(-900, 900)
        cmet.setx(x)
        cmet.direction = food.direction

def movecmet():
    y = cmet.ycor()
    cmet.sety(y - 30)

def comtd():
    if comt.xcor() > 900 or comt.xcor() < -900 or comt.ycor() > 450 or comt.ycor() < -450:
        comt.sety(475)
        x = random.randint(-900, 900)
        comt.setx(x)
        comt.direction = food.direction

def movecomt():
    y = comt.ycor()
    comt.sety(y - 40)

def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

# Keyboard bindings
wn.listen()
wn.onkeypress(shoot, "space")
wn.onkeypress(go_up, "w")
wn.onkeypress(go_down, "s")
wn.onkeypress(go_left, "a")
wn.onkeypress(go_right, "d")
wn.onkeypress(go_up, "Up")
wn.onkeypress(go_down, "Down")
wn.onkeypress(go_left, "Left")
wn.onkeypress(go_right, "Right")

# Main game loop
while True:
    wn.update()

    # Check for a collision with the border
    if head.xcor()>900 or head.xcor()<-900 or head.ycor()>450 or head.ycor()<-450:
        time.sleep(1)
        head.goto(0,0)
        head.direction = "stop"

        # Reset the score
        score = 0

        # Reset the delay
        delay = 0.1

        pen.clear()
        pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))


    # Check for a collision with the food
    if head.distance(food) < 20 or head.distance(sot) < 40 or head.distance(comet) < 40 or cmet.distance(head) < 80 or comt.distance(head) < 70 or shstar.distance(head) < 20:
        # Move the food to a random spot
        x = random.randint(-900, 900)
        y = random.randint(-450, 450)
        food.goto(x,y)
        comet.goto(x,900)
        cmet.goto(x,900)
        comt.goto(x,900)
        shstar.goto(-450,y)
        time.sleep(.1)
        head.goto(0,0)
        head.direction = "stop"

        # Reset the score
        score = 0

        # Reset the delay
        delay = 0.1

        deaths += 1

        pen.clear()
        pen.write("Score: {}  High Score: {}  Deaths: {}".format(score, high_score, deaths), align="center", font=("Courier", 24, "normal"))

    if shot.distance(food) < 30:
        score += 10
        if score > high_score:
            high_score = score
        x = random.randint(-900, 900)
        y = random.randint(-450, 450)
        food.goto(x,y)
        pen.clear()
        pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))

    if comet.distance(food) < 20 or cmet.distance(food) < 60 or comt.distance(food) < 40 or shstar.distance(food) < 20:
        x = random.randint(-900, 900)
        y = random.randint(-450, 450)
        food.goto(x,y)

    xrel = food.xcor() - head.xcor()
    yrel = food.ycor() - head.ycor()
    if abs(xrel) > abs(yrel):
        if xrel < 0:
            food.direction = "right"
        if xrel > 0:
            food.direction = "left"
    if abs(xrel) < abs(yrel):
        if yrel < 0:
            food.direction = "up"
        if yrel > 0:
            food.direction = "down"

    if random.randint(5,5) == 5:
        sotd()

    cometd()
    movecomet()
    shstard()
    moveshstar()
    comtd()
    movecomt()
    cmetd()
    movecmet()
    movesot()
    moveshot()
    move()

    time.sleep(delay)
wn.mainloop()
