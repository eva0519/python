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

# lotation pos
to_x = 0
to_y = 0

# event loop
running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

        if event.type == pg.KEYDOWN:
            if event.key == pg.K_LEFT:
                to_x -= 5
            elif event.key == pg.K_RIGHT:
                to_x += 5
            elif event.key == pg.K_UP:
                to_y -= 5
            elif event.key == pg.K_DOWN:
                to_y += 5

        if event.type == pg.KEYUP:
            if event.key == pg.K_LEFT or event.key == pg.K_RIGHT:
                to_x = 0
            elif event.key == pg.K_UP or event.key == pg.K_DOWN:
                to_y = 0

    character_x_pos += to_x
    character_y_pos += to_y

    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > SCREEN_WIDTH - character_width:
        character_x_pos = SCREEN_WIDTH - character_width

    if character_y_pos < 0:
        character_y_pos = 0
    elif character_y_pos > SCREEN_HEIGHT - character_height:
        character_y_pos = SCREEN_HEIGHT - character_height

    screen.blit(background, (0, 0))

    screen.blit(character, (character_x_pos, character_y_pos))

    pg.display.update()

pg.quit()
