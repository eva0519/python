import random
import pygame as pg

#################### initialize settings ####################

pg.init()

# screen scale
SCREEN_WIDTH = 480
SCREEN_HEIGHT = 640
screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# title
pg.display.set_caption("evadeD")

# FPS
clock = pg.time.Clock()

#################### initialize settings ####################

# custom init (background, font, image, position, speed)
background = pg.image.load(
    "D:/Development/Python/pygame/ddong/img/backgroundForest.png"
)

character = pg.image.load("D:/Development/Python/pygame/ddong/img/alphaL.png")
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (SCREEN_WIDTH / 2) - (character_width / 2)
character_y_pos = SCREEN_HEIGHT - character_height

to_x = 0
character_speed = 10

enemy = pg.image.load("D:/Development/Python/pygame/ddong/img/ddong.png")
enemy_size = enemy.get_rect().size
enemy_width = enemy_size[0]
enemy_height = enemy_size[1]
enemy_x_pos = random.randint(0, (SCREEN_WIDTH - character_width))
enemy_y_pos = 0

enemy_speed = 10

evade_font = pg.font.SysFont("malgungothic", 30)

# event loop
running = True
while running:
    dt = clock.tick(30)

    # event proc
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_LEFT:
                to_x -= character_speed
                character = pg.image.load(
                    "D:/Development/Python/pygame/ddong/img/alphaL.png"
                )
            elif event.key == pg.K_RIGHT:
                to_x += character_speed
                character = pg.image.load(
                    "D:/Development/Python/pygame/ddong/img/alphaR.png"
                )

        elif event.type == pg.KEYUP:
            to_x = 0

    # exception proc
    if character_x_pos >= (SCREEN_WIDTH - character_width):
        character_x_pos = SCREEN_WIDTH - character_width

    if character_x_pos <= 0:
        character_x_pos = max(character_x_pos, 0)

    if enemy_y_pos == SCREEN_HEIGHT:
        enemy_y_pos = 0
        enemy_x_pos = random.randint(0, (SCREEN_WIDTH - character_width))

    character_x_pos += to_x
    enemy_y_pos += enemy_speed

    # object definition

    # colllision
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos

    if character_rect.colliderect(enemy_rect):
        print("Crush")
        running = False

    # draw
    screen.blit(background, (0, 0))
    screen.blit(character, (character_x_pos, character_y_pos))
    screen.blit(enemy, (enemy_x_pos, enemy_y_pos))

    evade_text = evade_font.render("alphaka", True, (255, 255, 255))
    screen.blit(evade_text, (10, 10))

    pg.display.update()

pg.quit()
