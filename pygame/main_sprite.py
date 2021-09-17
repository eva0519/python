import pygame as pg

pg.init()

SCREEN_WIDTH = 480
SCREEN_HEIGHT = 640
screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pg.display.set_caption("KpyG")

# background
background = pg.image.load("D:/horolro/kpy/background.png")

# sprite
character = pg.image.load("D:/horolro/kpy/character.png")
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = SCREEN_WIDTH / 2 - (character_width / 2)
character_y_pos = SCREEN_HEIGHT - character_height

# event loop
running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    screen.blit(background, (0, 0))

    screen.blit(character, (character_x_pos, character_y_pos))

    pg.display.update()

pg.quit()
