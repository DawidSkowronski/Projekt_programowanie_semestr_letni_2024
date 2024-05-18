import pygame
import time

# GLOBALNE STAŁE
OKNO_SZER = 1200
OKNO_WYS = 700
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
    wys = szer * 3/4
    kolor = (255, 255, 255)
    speed = 8
    dx = 0   
    dy = 0

    def __init__(self, hp):
        Byt.__init__(self, 0, 0, hp)

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
        
        # GRACZ NIE MOŻE WYJŚĆ ZA OKIENKO
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

        if self.y <= OKNO_WYS*2//3:
            if self.dy < 0:
                self.y = OKNO_WYS*2//3
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



# KLASA PRZECIWNIK
class Przeciwnik(Byt):
    szer = OKNO_SZER//12
    wys = szer * 3/4
    kolor = (255, 255, 255)
    speed = 2
    dx = 0
    dy = 0

    def __init__(self, hp):
        Byt.__init__(self, 0, 0, hp)
    
    def rysujPrzeciwnika(self, okienko):
        self.przeciwnik = pygame.Rect(self.x, self.y, self.szer, self.wys)

        pygame.draw.rect(okienko, self.kolor, self.przeciwnik)

    def ruchPrzeciwnika(self):
        self.dy=self.speed
        przeciwnik_czekaj = 1000
        

        if self.y <= OKNO_WYS*2//3:
            if self.dy < 0:
                self.y = OKNO_WYS*2//3
            else:
                pygame.time.set_timer(zdarzenie_pozycja_przeciwnika, przeciwnik_czekaj)
                self.y += self.dy


    def ustawPrzeciwnika(self, x, y):
        """Ustawia przeciwnika na konkretne koordynaty."""
        self.x = x
        self.y = y

#DODAWANIE OBIEKTÓW

gracz = Gracz(100)
gracz.ustawGracza((OKNO_SZER - gracz.szer)//2, OKNO_WYS - gracz.wys - 50)

przeciwnik = Przeciwnik(100)
przeciwnik.ustawPrzeciwnika((OKNO_SZER - gracz.szer)//2, 0 )
zdarzenie_pozycja_przeciwnika = pygame.USEREVENT

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
        #elif zdarzenie.type == zdarzenie_pozycja_przeciwnika:
            przeciwnik.ruchPrzeciwnika(10)
    keys = pygame.key.get_pressed()

    okienko.fill(TŁO)

    # WYKONUJE SIĘ NA KAŻDY TICK
    gracz.przesuńGracza(keys)
    gracz.rysujGracza(okienko)

    przeciwnik.ruchPrzeciwnika()
    przeciwnik.rysujPrzeciwnika(okienko)

    pygame.display.update()
    zegarek.tick(FPS)

pygame.quit()