import pygame as pg

pg.init()

SCREEN_WIDTH = 480
SCREEN_HEIGHT = 640
screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pg.display.set_caption("KpyG")

background = pg.image.load("D:/horolro/kpy/background.png")

# event loop
running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    # screen.fill((0,0,255))
    screen.blit(background, (0, 0))
    pg.display.update()

pg.quit()
