import pygame

# GLOBALNE STAŁE
OKNO_SZER = 1200
OKNO_WYS = 900
FPS = 60
TŁO = (0, 25, 15)

# KLASA BYTU
class Byt:
    """Klasa tworząca byt w grze."""
    def __init__(self, x, y, hp):
        self.x = x
        self.y = y
        self.hp = hp

# KLASA GRACZ
class Gracz(Byt):
    """Klasa zawierająca funkcjonalność i anatomię gracza."""
    szer = OKNO_SZER//12
    wys = szer
    kolor = (255, 255, 255)
    speed = 15
    dx = 0
    dy = 0

    def __init__(self, x, y, hp):
        Byt.__init__(self, x, y, hp)

    def rysujGracza(self, okienko):
        """Rysuje instancję gracza."""
        
        self.gracz = pygame.Rect(self.x, self.y, self.szer, self.wys)

        pygame.draw.rect(okienko, self.kolor, self.gracz)

    def przesuńGracza(self, keys):
        """Zmienia koordynaty gracza."""
        if keys[pygame.K_w]:
            self.dy = -self.speed
        elif keys[pygame.K_s]:
            self.dy = self.speed
        else:
            self.dy = 0

        if keys[pygame.K_a]:
            self.dx = -self.speed
        elif keys[pygame.K_d]:
            self.dx = self.speed
        else:
            self.dx = 0
        
        if self.x <= 0:
            if self.dx < 0:
                self.x = 0
            else:
                self.x += self.dx
        elif self.x >= OKNO_SZER - self.szer:
            if self.dx > 0:
                self.x = OKNO_SZER - self.szer
            else:
                self.x += self.dx
        else:
            self.x += self.dx

        if self.y <= 0:
            if self.dy < 0:
                self.y = 0
            else:
                self.y += self.dy
        elif self.y >= OKNO_WYS - self.wys:
            if self.dy > 0:
                self.y = OKNO_WYS - self.wys
            else:
                self.y += self.dy
        else:
            self.y += self.dy

    def ustawGracza(self, x, y):
        """Ustawia gracza na konkretne koordynaty."""
        self.x = x
        self.y = y

gracz = Gracz(100, 500, 100)

# KLASA PRZECIWNIK
class Przeciwnik(Byt):
    pass

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
    keys = pygame.key.get_pressed()

    okienko.fill(TŁO)

    # WYKONUJE SIĘ NA KAŻDY TICK
    gracz.przesuńGracza(keys)
    gracz.rysujGracza(okienko)
    
    pygame.display.update()
    zegarek.tick(FPS)

pygame.quit()