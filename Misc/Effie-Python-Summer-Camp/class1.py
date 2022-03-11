import pgzrun

WIDTH = 600
HEIGHT = 300


def draw():
    # Background
    screen.fill((0, 55, 255))

    # Sun
    screen.draw.filled_circle((80, 80), 50, (255, 208, 0))

    # Rocks
    screen.draw.filled_circle((320, 300), 90, (143, 143, 143))
    screen.draw.filled_circle((450, 300), 60, (143, 143, 143))

    # Cloud
    screen.draw.filled_circle((420, 100), 50, (255, 255, 255))
    screen.draw.filled_circle((450, 70), 40, (255, 255, 255))
    screen.draw.filled_circle((500, 90), 35, (255, 255, 255))
    screen.draw.filled_rect(Rect((370, 100), (470, 120)), (0, 55, 255))

    # Grass
    screen.draw.filled_rect(Rect((0, 260), (600, 300)), (94, 166, 96))


pgzrun.go()
