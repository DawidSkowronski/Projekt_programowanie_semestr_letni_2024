import pygame

# GLOBALNE STAŁE
OKNO_SZER = 800
OKNO_WYS = 600
FPS = 60
TŁO = (0, 25, 15)

# KLASA BYTU
class Byt:
    """Zawiera """
    def __init__(self, x, y, hp):
        self.x = x
        self.y = y
        self.hp = hp

# KLASA GRACZ
class Gracz(Byt):
    pass

# KLASA PRZECIWNIK
class Przeciwnik(Byt):
    pass

gracz = Gracz(1, 2, 10)
print(gracz.x)

# GRA
pygame.init()

okienko = pygame.display.set_mode((OKNO_SZER, OKNO_WYS), 0, 32)
pygame.display.set_caption("Student Invaders")
zegarek = pygame.time.Clock()

graj = True
while graj:
    for zdarzenie in pygame.event.get():
        if zdarzenie.type == pygame.QUIT:
            graj = False

    okienko.fill(TŁO)
    
    pygame.display.update()
    zegarek.tick(FPS)

pygame.quit()