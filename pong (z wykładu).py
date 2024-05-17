import pygame

from math import sin, cos, pi
from random import choice, uniform

OKNO_SZER = 800
OKNO_WYS = 600
FPS = 60

# PALETKA
PALETKA_WYS = 80
PALETKA_SZER = 20
PALETKA = (255, 255, 255)

# PIŁKA
PIŁKA = (255, 255, 255)
PIŁKA_R = 10
piłka_x = OKNO_SZER//2
piłka_y = OKNO_SZER//2

piłka_dx = 0
piłka_dy = 0

# TŁO
TŁO = (0, 30, 0)

# GRACZE
gracz1 = pygame.Rect(0, OKNO_WYS//2 - PALETKA_SZER//2, PALETKA_SZER, PALETKA_WYS)
gracz2 = pygame.Rect(OKNO_SZER - PALETKA_SZER, OKNO_WYS//2 - PALETKA_SZER//2, PALETKA_SZER, PALETKA_WYS)

SPEED = 5
gracz1_speed = 0
gracz2_speed = 0

# WYNIKI
STOP_PLAY = 5
TEKST = (127, 127, 127)
WINNER = (127, 255, 127)
LOOSER = (255, 127, 127)


pygame.init()

font = pygame.font.SysFont('Arial', 64)
okienko = pygame.display.set_mode((OKNO_SZER, OKNO_WYS), 0, 32)
pygame.display.set_caption("student invaders")
zegarek = pygame.time.Clock()

# NOWA PIŁKA
def nowa_piłka():
    """Tworzy piłkę i nadaje jej trajektorię."""
    global piłka_x, piłka_y, piłka_dx, piłka_dy
    phi = uniform(-pi/3, pi/3)
    piłka_x = OKNO_SZER//2
    piłka_y = OKNO_WYS//2
    piłka_dx = SPEED * choice([-1, 1]) * cos(phi)
    piłka_dy = SPEED * sin(phi)

nowa_piłka()

gracz1_wynik = 0
gracz2_wynik = 0
gracz1_text = font.render("0", True, TEKST)
gracz2_text = font.render("0", True, TEKST)


graj = True
while graj:
    for zdarzenie in pygame.event.get():
        if zdarzenie.type == pygame.QUIT:
            graj = False
        elif zdarzenie.type == pygame.KEYDOWN:
            if zdarzenie.key == pygame.K_w:
                gracz1_speed -= SPEED   
            elif zdarzenie.key == pygame.K_s:
                gracz1_speed += SPEED
            elif zdarzenie.key == pygame.K_UP:
                gracz2_speed -= SPEED
            elif zdarzenie.key == pygame.K_DOWN:
                gracz2_speed += SPEED
        elif zdarzenie.type == pygame.KEYUP:
            if zdarzenie.key == pygame.K_w:
                gracz1_speed += SPEED
            elif zdarzenie.key == pygame.K_s:
                gracz1_speed -= SPEED
            elif zdarzenie.key == pygame.K_UP:
                gracz2_speed += SPEED
            elif zdarzenie.key == pygame.K_DOWN:
                gracz2_speed -= SPEED

    

    # WYPEŁNIENIE TŁA
    okienko.fill(TŁO)
    okienko.blit(gracz1_text, (40, 40))
    okienko.blit(gracz2_text, (OKNO_SZER-40-gracz2_text.get_rect().width, 40))

    # RYSOWANIE OBIEKTÓW
    pygame.draw.rect(okienko, PALETKA, gracz1)
    pygame.draw.rect(okienko, PALETKA, gracz2)

    piłka_x += piłka_dx
    piłka_y += piłka_dy
    pygame.draw.circle(okienko, PIŁKA, (piłka_x, piłka_y), PIŁKA_R)

    gracz1.y += gracz1_speed
    if gracz1.y < 0:
        gracz1.y = 0
    elif gracz1.y > OKNO_WYS - PALETKA_WYS:
        gracz1.y = OKNO_WYS - PALETKA_WYS

    gracz2.y += gracz2_speed
    if gracz2.y < 0:
        gracz2.y = 0
    elif gracz2.y > OKNO_WYS - PALETKA_WYS:
        gracz2.y = OKNO_WYS - PALETKA_WYS

    if piłka_y < PIŁKA_R:
        wystaje = PIŁKA_R-piłka_y
        piłka_y = PIŁKA_R+wystaje
        piłka_dy *= -1
    elif piłka_y > OKNO_WYS-PIŁKA_R:
        wystaje = piłka_y - (OKNO_WYS-PIŁKA_R)
        piłka_y = OKNO_WYS-PIŁKA_R-wystaje
        piłka_dy *= -1

    if piłka_x < PIŁKA_R+PALETKA_SZER:
        if gracz1.y <= piłka_y <= gracz1.y+PALETKA_WYS:
            wystaje = PIŁKA_R+PALETKA_SZER - piłka_x
            piłka_x = PIŁKA_R+PALETKA_SZER+wystaje
            piłka_dx *= -1
        else:
            gracz2_wynik += 1
            if gracz2_wynik >= STOP_PLAY:
                gracz1_text = font.render(str(gracz1_wynik), True, LOOSER)
                gracz2_text = font.render(str(gracz2_wynik), True, WINNER)
                SPEED = 0
                gracz1_speed = 0
                gracz2_speed = 0
            else:
                gracz2_text = font.render(str(gracz2_wynik), True, TEKST)
            nowa_piłka()
    elif piłka_x > OKNO_SZER-PALETKA_SZER-PIŁKA_R:
        if gracz2.y <= piłka_y <= gracz2.y+PALETKA_WYS:
            wystaje = piłka_x - (OKNO_SZER-PALETKA_SZER-PIŁKA_R)
            piłka_x = OKNO_SZER-PALETKA_SZER-PIŁKA_R - wystaje
            piłka_dx *= -1
        else:
            gracz1_wynik += 1
            if gracz1_wynik >= STOP_PLAY:
                gracz1_text = font.render(str(gracz1_wynik), True, WINNER)
                gracz2_text = font.render(str(gracz2_wynik), True, LOOSER)
                SPEED = 0
                gracz1_speed = 0
                gracz2_speed = 0
            else:
                gracz1_text = font.render(str(gracz1_wynik), True, TEKST)
            nowa_piłka()

            

    pygame.display.update()
    zegarek.tick(FPS)

pygame.quit()
