import pygame as pg

####################### 0. recommended ########################

pg.init()

SCREEN_WIDTH = 480
SCREEN_HEIGHT = 640
screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# title
pg.display.set_caption("title")

# fps
clock = pg.time.Clock()

############################################################

#################### 1. user init process (resource) ##################

running = True
while running:
    dt = clock.tick(60)
    # fps setting
    # print("fps : " + str(clock.get_fps()))

    # 3. event process (keyboard, mouse)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    # 4. object location definition

    # 5. collision process

    # 6. draw
    pg.display.update()

pg.quit()
