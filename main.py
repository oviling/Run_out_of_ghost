import pygame as pg

pg.init()
screen = pg.display.set_mode((480, 360))
pg.display.set_caption("Убеги от преведешка!")
pg.display.set_icon(pg.image.load("textures/ghost-a.png"))
screen.fill((114, 157, 224))

square = pg.Surface((50, 170))
square.fill("Red")

myfont = pg.font.Font("fonts/Roboto-Italic.ttf", 40)
text_surface = myfont.render("Привет!", True, "Purple")

ghost = pg.image.load("textures/ghost-a.png", )

running = True
while running:

    screen.blit(square, (10, 10))
    screen.blit(text_surface, (200, 10))
    pg.draw.circle(screen, "Blue", (100, 100), 30)
    screen.blit(ghost, (200, 80))

    pg.display.update()

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
            pg.quit()
       #elif event.type == pg.KEYDOWN:
       #    if event.key == pg.K_a:
       #        screen.fill((70, 44, 133))
