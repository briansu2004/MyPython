import pgzrun
import random

WIDTH = 600
HEIGHT = 300

x = 30
xv = 2
y = 30
yv = 2
r = 30

xrect = 270
yrect = 290
wrect = 100
hrect = 10

score = 0


def update():
    global x, xv, y, yv, xrect, yrect, wrect, hrect, score

    if x > 570:
        xv = -random.randint(0, 9)
    if y > 270:
        yv = -random.randint(0, 9)
    if x < 30:
        xv = random.randint(0, 9)
    if y < 30:
        yv = random.randint(0, 9)
    x = x + xv
    y = y + yv

    if keyboard.left:
        xrect += -10
    if keyboard.right:
        xrect += 10

    if abs(x - xrect) <= wrect and abs(y - yrect) == r:
        score += 1


def draw():
    global x, xv, y, yv, xrect, yrect, wrect, hrect, score

    # Background
    screen.fill((48, 48, 48))

    # Score
    screen.draw.text("Score: " + str(score), (0, 0), color="orange")

    # Ping pong ball
    screen.draw.filled_circle((x, y), r, (255, 255, 255))

    # Thing to stop ping pong ball from "dieing"
    screen.draw.filled_rect(Rect((xrect, yrect), (wrect, hrect)), (64, 255, 0))


pgzrun.go()
