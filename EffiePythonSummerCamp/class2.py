import pgzrun

WIDTH = 600
HEIGHT = 300

xsun = 80
xline = 500
xcar = 25
xwheel1 = 120
xwheel2 = 50


def update():
    global xsun, xline, xcar, xwheel1, xwheel2
    c = 0.5
    xsun += 0.1
    xcar = xcar + c
    xline -= 1
    xwheel1 = xwheel1 + c
    xwheel2 = xwheel2 + c


def draw():
    global xsun

    # Background
    screen.fill((0, 55, 255))

    # Sun
    screen.draw.filled_circle((xsun, 50), 20, (255, 208, 0))

    # Road
    screen.draw.filled_rect(Rect((0, 230), (600, 300)), (89, 89, 89))

    # Car
    screen.draw.filled_circle((xwheel2, 210), 20, (69, 69, 69))
    screen.draw.filled_circle((xwheel1, 210), 20, (69, 69, 69))
    screen.draw.filled_rect(Rect((xcar, 170), (120, 30)), (0, 255, 183))
    screen.draw.filled_rect(Rect((xcar, 140), (80, 30)), (0, 255, 183))

    # line in road
    #screen.draw.line((xline, 260), (xline + 50, 260), (255, 255, 255))


pgzrun.go()
