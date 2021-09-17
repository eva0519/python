import pygame as pg

pg.init()

SCREEN_WIDTH = 480
SCREEN_HEIGHT = 640
screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# title
pg.display.set_caption("KpyG")

# fps
clock = pg.time.Clock()

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
character_speed = 0.6

# enemy
enemy = pg.image.load("D:/horolro/kpy/enemy.png")
enemy_size = enemy.get_rect().size
enemy_width = enemy_size[0]
enemy_height = enemy_size[1]
enemy_x_pos = SCREEN_WIDTH / 2 - (enemy_width / 2)
enemy_y_pos = SCREEN_HEIGHT / 2 - (enemy_height / 2)

# event loop
running = True
while running:
    dt = clock.tick(60)  # fps setting
    # print("fps : " + str(clock.get_fps()))

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

        if event.type == pg.KEYDOWN:
            if event.key == pg.K_LEFT:
                to_x -= character_speed
            elif event.key == pg.K_RIGHT:
                to_x += character_speed
            elif event.key == pg.K_UP:
                to_y -= character_speed
            elif event.key == pg.K_DOWN:
                to_y += character_speed

        if event.type == pg.KEYUP:
            if event.key == pg.K_LEFT or event.key == pg.K_RIGHT:
                to_x = 0
            elif event.key == pg.K_UP or event.key == pg.K_DOWN:
                to_y = 0

    character_x_pos += to_x * dt
    character_y_pos += to_y * dt

    # boundary value
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > SCREEN_WIDTH - character_width:
        character_x_pos = SCREEN_WIDTH - character_width

    if character_y_pos < 0:
        character_y_pos = 0
    elif character_y_pos > SCREEN_HEIGHT - character_height:
        character_y_pos = SCREEN_HEIGHT - character_height

    # collision
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos

    if character_rect.colliderect(enemy_rect):
        print("crush")
        running = False

    # draw
    screen.blit(background, (0, 0))
    screen.blit(character, (character_x_pos, character_y_pos))
    screen.blit(enemy, (enemy_x_pos, enemy_y_pos))

    # diter
    pg.display.update()

pg.quit()
