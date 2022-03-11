import pgzrun

WIDTH = 600
HEIGHT = 300

x = 0
xv = 2
y = 50
y2 = 10


def update():
    global x, xv, y, y2
    x = x + xv
    if x > 500:
        xv = -10
    if x < 30:
        xv = 10
    if keyboard.down:
        y = 200
        y2 = 160
    else:
        y = 50
        y2 = 10


def draw():
    # Background
    screen.fill((48, 48, 48))

    # Ping pong ball
    screen.draw.filled_circle((x, y), 30, (255, 255, 255))

    # Thing to stop ping pong ball from "dieing"
    screen.draw.filled_rect(Rect((10, y2), (20, 80)), (64, 255, 0))
    screen.draw.filled_rect(Rect((540, y2), (20, 80)), (255, 0, 0))


pgzrun.go()
