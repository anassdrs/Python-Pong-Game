import turtle

wind = turtle.Screen()
wind.title("Ping Pong By Anass")
wind.bgcolor("black")
wind.setup(width=1200, height=800)
wind.tracer(0)  # stop the window from updating automatically
# madrab1
madrab1 = turtle.Turtle()
madrab1.speed(0)
madrab1.shape("square")
madrab1.shapesize(5, 1)
madrab1.color("blue")
madrab1.penup()
madrab1.goto(-550, 0)
# madrab2
madrab2 = turtle.Turtle()
madrab2.speed(0)
madrab2.shape("square")
madrab2.shapesize(5, 1)
madrab2.color("green")
madrab2.penup()
madrab2.goto(550, 0)
# ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.5
ball.dy = 0.5
# score
score1 = 0
score2 = 0
score = turtle.Turtle()
score.speed(0)
score.shape("square")
score.color("white")
score.penup()
score.hideturtle()
score.goto(0, 360)
score.write("Player 1: 0 Player 2: 0", align="center",
            font=("Courier", 24, "normal"))

# functions


def madrab1_up():
    y = madrab1.ycor()
    y += 20
    madrab1.sety(y)


def madrab1_down():
    y = madrab1.ycor()
    y -= 20
    madrab1.sety(y)


def madrab2_up():
    y = madrab2.ycor()
    y += 20
    madrab2.sety(y)


def madrab2_down():
    y = madrab2.ycor()
    y -= 20
    madrab2.sety(y)


# keyboard bindings
wind.listen()
wind.onkeypress(madrab1_up, "8")
wind.onkeypress(madrab1_down, "5")
wind.onkeypress(madrab2_up, "Up")
wind.onkeypress(madrab2_down, "Down")
# main game loop
while True:
    wind.update()  # update the screen every time the loop runs
    # move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # border check
    if ball.ycor() > 390:
        ball.sety(390)
        ball.dy *= -1
    if ball.ycor() < - 390:
        ball.sety(-390)
        ball.dy *= -1
    if ball.xcor() < - 590:
        ball.goto(0, 0)
        ball.dx *= -1
        score2 += 1
        score.clear()
        score.write("Player 1:{} Player 2: {}".format(score1, score2),
                    align="center", font=("Courier", 24, "normal"))

    if ball.xcor() > 590:
        ball.goto(0, 0)
        ball.dx *= -1
        score1 += 1
        score.clear()
        score.write("Player 1:{} Player 2: {}".format(score1, score2),
                    align="center", font=("Courier", 24, "normal"))
    # tasadom madrab and ball

    if (ball.xcor() > 540 and ball.xcor() < 550 and ball.ycor() > madrab2.ycor()-40 and ball.ycor() < madrab2.ycor() + 40):
        ball.setx(540)
        ball.dx *= -1
    if (ball.xcor() < -540 and ball.xcor() > -550 and ball.ycor() > madrab1.ycor()-40 and ball.ycor() < madrab1.ycor() + 40):
        ball.setx(-540)
        ball.dx *= -1
