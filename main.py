import pygame as pg
import random as r
import time as t

pg.init()
clock = pg.time.Clock()
screen = pg.display.set_mode((960, 720))
pg.display.set_caption("Убеги от преведешка!")
pg.display.set_icon(pg.image.load("textures/ghost-a.png"))
screen.fill((114, 157, 224))


def ghost_move(keys, ghost_x, ghost_y, ghost_reload, player_speed):
    if keys[pg.K_a] and ghost_x > 0:
        ghost_x -= player_speed
        return ghost_x, ghost_y, ghost_reload
    elif keys[pg.K_d] and ghost_x < 920:
        ghost_x += player_speed
        return ghost_x, ghost_y, ghost_reload
    elif keys[pg.K_s] and ghost_y < 700:
        ghost_y += player_speed
        return ghost_x, ghost_y, ghost_reload
    elif keys[pg.K_w] and ghost_y > 0:
        ghost_y -= player_speed
        return ghost_x, ghost_y, ghost_reload
    elif keys[pg.K_q]:
        ghost_reload = 0
        ghost_x, ghost_y = r.randint(0, 920), r.randint(0, 700)
        return ghost_x, ghost_y, ghost_reload
    else:
        return ghost_x, ghost_y, ghost_reload


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
    player_speed = 4
    cat_x = 920
    cat_y = 700
    cat_reload = 0
    ghost_x = 0
    ghost_y = 0
    ghost_reload = 0
    gameplay = True
    running = True
    time = 1800

    return player_speed, cat_x, cat_y, cat_reload, ghost_x, ghost_y, ghost_reload, gameplay, running, time

player_speed, cat_x, cat_y, cat_reload, ghost_x, ghost_y, ghost_reload, gameplay, running, time = restart()

cat_wins = 0
ghost_wins = 0
go_sound = pg.mixer.Sound("sounds/goo.mp3")


myfont = pg.font.Font("font/Roboto-Italic.ttf", 25)
gameover_text = myfont.render("Для перезапуска наведите на данное сообщение", True, "Purple")
gameover_text_rect = gameover_text.get_rect(topleft=(25, 350))
win_text = myfont.render("Кися победила, для перезапуска наведите на данный текст", True, "Purple")
win_text_rect = win_text.get_rect(topleft=(25, 350))

bg = pg.image.load("textures/Woods.png").convert()
ghost = pg.transform.scale(pg.image.load("textures/ghost-a.png").convert_alpha(), (54, 102))
cat = pg.transform.scale(pg.image.load("textures/costume2.png").convert_alpha(), (85, 102))

go_sound.play()
gameplay = True
running = True
while running:

    keys = pg.key.get_pressed()

    screen.blit(bg, (0, 0))
    screen.blit(ghost, (ghost_x, ghost_y))
    screen.blit(cat, (cat_x, cat_y))

    if gameplay:

        ghost_x, ghost_y, ghost_reload = ghost_move(keys, ghost_x, ghost_y, ghost_reload, player_speed)
        cat_x, cat_y, ghost_x, ghost_y, cat_reload = cat_move(keys, cat_x, cat_y, cat_reload, ghost_x, ghost_y, player_speed)

        cat_rect = cat.get_rect(topleft=(cat_x, cat_y))
        ghost_rect = ghost.get_rect(topleft=(ghost_x, ghost_y))

        if cat_rect.colliderect(ghost_rect) or time <= 0:
            gameplay = False

        cat_reload += 1
        ghost_reload += 1
        time -= 1
    else:
        screen.fill((0, 255, 255))
        if time <= 0:
            screen.blit(win_text, win_text_rect)
            cat_wins += 1
        else:
            screen.blit(gameover_text, gameover_text_rect)
            ghost_wins += 1

        mouse = pg.mouse.get_pos()
        if gameover_text_rect.collidepoint(mouse) or win_text_rect.collidepoint(mouse) and pg.mouse.get_pressed():
            cat_x = 920
            cat_y = 700
            ghost_x = 0
            ghost_y = 0
            cat_reload = 0
            ghost_reload = 0
            time = 1800
            t.sleep(4)
            gameplay = True

    pg.display.update()

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
            print(f"кися: {cat_wins}, призря: {ghost_wins}")
            pg.quit()

    clock.tick(60)
