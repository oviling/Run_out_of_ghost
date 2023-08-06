import pygame as pg

pg.init()
screen = pg.display.set_mode((960, 720))
pg.display.set_caption("Убеги от преведешка!")
pg.display.set_icon(pg.image.load("textures/ghost-a.png"))
screen.fill((114, 157, 224))


bg = pg.image.load("textures/Woods.png")
ghost = pg.transform.scale(pg.image.load("textures/ghost-a.png"), (54, 102)) #2.7
cat = pg.transform.scale(pg.image.load("textures/costume2.png"), (85, 102))

running = True
while running:

    screen.blit(bg, (0, 0))
    screen.blit(ghost, (0, 0))
    screen.blit(cat, (100, 100))

    pg.display.update()

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
            pg.quit()
       #elif event.type == pg.KEYDOWN:
       #    if event.key == pg.K_a:
       #        screen.fill((70, 44, 133))
