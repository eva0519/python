import pygame as pg
import random as rd

####################### 0. recommended ########################

pg.init()

SCREEN_WIDTH = 480
SCREEN_HEIGHT = 640
screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# title
pg.display.set_caption("Quiz")

# fps
clock = pg.time.Clock()

############################################################

#################### 1. user initialize process (resource) ##################

background = pg.image.load("D:/horolro/kpy/background.png")

character = pg.image.load("D:/horolro/kpy/character.png")
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (SCREEN_WIDTH / 2) - (character_width / 2)
character_y_pos = SCREEN_HEIGHT - character_height

to_x = 0
character_speed = 10

enemy = pg.image.load("D:/horolro/kpy/enemy.png")
enemy_size = enemy.get_rect().size
enemy_width = enemy_size[0]
enemy_height = enemy_size[1]
enemy_x_pos = randint(0, SCREEN_WIDTH)
enemy_y_pos = 0

enemy_speed = 10

running = True
while running:
    dt = clock.tick(30)
    # fps setting
    # print("fps : " + str(clock.get_fps()))

    # 3. event process
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

        if event.type == pg.KEYDOWN:
            if event.key == pg.K_LEFT:
                to_x -= character_speed
            elif event.key == pg.K_RIGHT:
                to_x += character_speed

        if event.type == pg.KEYUP:
            if event.key == pg.K_LEFT or event.key == pg.K_RIGHT:
                to_x = 0

    # 4. object location definition

    character_x_pos += to_x

    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > SCREEN_WIDTH - character_width:
        character_x_pos = SCREEN_WIDTH - character_width

    # 5. collision process

    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.right = character_y_pos

    # 6. draw
    screen.blit(background, (0, 0))
    screen.blit(character, (character_x_pos, character_y_pos))

    pg.display.update()

pg.quit()
