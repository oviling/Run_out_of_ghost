import pygame as pg
import random as r

pg.init()
clock = pg.time.Clock()
screen = pg.display.set_mode((960, 720))
pg.display.set_caption("Убеги от преведешка!")
pg.display.set_icon(pg.image.load("textures/ghost-a.png"))
screen.fill((114, 157, 224))


def ghost_move(keys, ghost_x, ghost_y, ghost_reload, player_speed):
    if keys[pg.K_a] and ghost_x > 0:
        ghost_x -= player_speed
        return ghost_x, ghost_y
    elif keys[pg.K_d] and ghost_x < 920:
        ghost_x += player_speed
        return ghost_x, ghost_y
    elif keys[pg.K_s] and ghost_y < 700:
        ghost_y += player_speed
        return ghost_x, ghost_y
    elif keys[pg.K_w] and ghost_y > 0:
        ghost_y -= player_speed
        return ghost_x, ghost_y
    else:
        return ghost_x, ghost_y


def cat_move(keys, cat_x, cat_y, cat_reload,  ghost_x, ghost_y, player_speed):
    if keys[pg.K_LEFT] and cat_x > 0:
        cat_x -= player_speed
        return cat_x, cat_y, ghost_x, ghost_y, cat_reload
    elif keys[pg.K_RIGHT] and cat_x < 920:
        cat_x += player_speed
        return cat_x, cat_y, ghost_x, ghost_y, cat_reload
    elif keys[pg.K_DOWN] and cat_y < 700:
        cat_y += player_speed
        return cat_x, cat_y, ghost_x, ghost_y, cat_reload
    elif keys[pg.K_UP] and cat_y > 0:
        cat_y -= player_speed
        return cat_x, cat_y, ghost_x, ghost_y, cat_reload
    elif keys[pg.K_SPACE] and cat_reload > 300:
        ghost_x, ghost_y = 0, 0
        cat_reload = 0
        return cat_x, cat_y, ghost_x, ghost_y, cat_reload
    else:
        return cat_x, cat_y, ghost_x, ghost_y, cat_reload


def restart():
    player_speed = 6
    cat_x = 920
    cat_y = 700
    cat_reload = 0
    ghost_x = 0
    ghost_y = 0
    ghost_reload = 0
    gameplay = True

    return player_speed, cat_x, cat_y, cat_reload, ghost_x, ghost_y, ghost_reload, gameplay

player_speed, cat_x, cat_y, cat_reload, ghost_x, ghost_y, ghost_reload, gameplay = restart()

go_sound = pg.mixer.Sound("sounds/goo.mp3")


myfont = pg.font.Font("font/Roboto-Italic.ttf", 70)
gameover_text = myfont.render("Для перезапуска нажмите r", True, "Purple")

bg = pg.image.load("textures/Woods.png").convert()
ghost = pg.transform.scale(pg.image.load("textures/ghost-a.png").convert_alpha(), (54, 102))
cat = pg.transform.scale(pg.image.load("textures/costume2.png").convert_alpha(), (85, 102))

go_sound.play()
gameplay = True
running = True
while running:

    keys = pg.key.get_pressed()

    if gameplay:

        ghost_x, ghost_y = ghost_move(keys, ghost_x, ghost_y, ghost_reload, player_speed)
        cat_x, cat_y, ghost_x, ghost_y, cat_reload = cat_move(keys, cat_x, cat_y, cat_reload, ghost_x, ghost_y, player_speed)

        screen.blit(bg, (0, 0))
        screen.blit(ghost, (ghost_x, ghost_y))
        screen.blit(cat, (cat_x, cat_y))

        cat_rect = cat.get_rect(topleft=(cat_x, cat_y))
        ghost_rect = ghost.get_rect(topleft=(ghost_x, ghost_y))

        if cat_rect.colliderect(ghost_rect):
            gameplay = False

        cat_reload += 1
        ghost_reload += 1
    else:
        screen.blit(gameover_text, (25, 350))
        if keys[pg.K_r]:
            restart()


    pg.display.update()

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
            pg.quit()

    clock.tick(60)
