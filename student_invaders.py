import pygame
import time
import random
import os

pygame.init()

# GLOBALNE STAŁE
OKNO_SZER = 1200
OKNO_WYS = 700
FPS = 60
TŁO = pygame.image.load(os.path.join("images","kosmos.png"))
statek = pygame.image.load(os.path.join("images","statek.png"))
wróg = pygame.image.load(os.path.join("images","kosmita.png"))
pocisk_gracza = pygame.image.load(os.path.join("images","pocisk_gracza.png"))

# KLASA BYTU
class Byt:
    """Klasa tworząca byt w grze."""
    def __init__(self, x, y):
        self.x = x
        self.y = y

# KLASA GRACZ
class Gracz(Byt):
    """Klasa zawierająca funkcjonalność i anatomię gracza."""
    szer = 115
    wys = 132
    speed = 8
    dx = 0   
    dy = 0

    def __init__(self):
        Byt.__init__(self, 0, 0)
        


    def ustawGracza(self, x, y):
        """Ustawia gracza na konkretne koordynaty."""
        self.x = x
        self.y = y

    def rysujGracza(self, okienko):
        """Rysuje instancję gracza."""
        okienko.blit(statek,(self.x,self.y))
        

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
        # NIE MOŻE WYJŚĆ Z LEWEJ ANI Z PRAWEJ
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

        # NIE MOŻE WYJŚĆ Z GÓRY ANI Z DOŁU
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

    def wystrzelPocisk(self, keys):
        """Przypisanie wystrzału do klawisza."""
        if keys[pygame.K_SPACE]:
            pocisk = Pocisk(x,y)



# KLASA PRZECIWNIK
class Przeciwnik(Byt):
    stworzonychPrzeciwników = 0

    szer = 128
    wys = 123
    dx = 0
    dy = 0

    def __init__(self):
        Byt.__init__(self, 0, 0)

        self.speed = 1

        self.id = Przeciwnik.stworzonychPrzeciwników
        Przeciwnik.stworzonychPrzeciwników += 1
    
    def rysujPrzeciwnika(self, okienko):
        """Rysuje instancję przeciwnika."""
        okienko.blit(wróg,(self.x,self.y))

    def ruchPrzeciwnika(self):
        """Zmienia koordynaty przeciwnika."""
        self.dy = self.speed

        self.y += self.dy

    def ustawPrzeciwnika(self, x = 0, y = 0):
        """Ustawia przeciwnika na konkretne koordynaty."""
        self.x = x
        self.y = y

# KLASA POCISK
class Pocisk():
    def __init__(self, x, y, img):
        self.x = x
        self.y = y

        self.img = img
        self.mask = pygame.mask.from_surface(self.img)  # mask tworzy dokładną siatkę pikseli wgranego obrazu 
        
        self.speed = 3
    
    def rysujPocisk(self, okienko):
        """Rysuje pocisk."""
        okienko.blit(self.img, (self.x, self.y) )  # rysuje obraz na wyświetlanym oknie
        
        
    def ruchPocisku(self, speed):
            self.y -= speed  # pocisk jest porusza się w górę
            

    def poza_oknem(self, wys ):    # usuwamy pociski poza oknem , żeby zostawiać zbędnych obiektów
        """Sprawdza czy pocisk znajduje się w obszarze okna, jeśli nie usuwa go."""
        return self.y >= wys + 10 and self.y <= -10

    #trzeba zdefiniować kolizję


        

# DODAWANIE OBIEKTÓW
# ustawiamy gracza na środku ekranu przy dole
gracz = Gracz()
gracz.ustawGracza((OKNO_SZER - gracz.szer)//2, OKNO_WYS - gracz.wys - 50)

# TIMER
# pojawia przeciwnika co jakiś czas
cykl_pojawienia_przeciwnika = 3000      # ms
pojaw_przeciwnika = pygame.USEREVENT
pygame.time.set_timer(pojaw_przeciwnika, cykl_pojawienia_przeciwnika)

#
#    GRA
#

okienko = pygame.display.set_mode((OKNO_SZER, OKNO_WYS), 0, 32)
pygame.display.set_caption("Student Invaders")
zegarek = pygame.time.Clock()

# lista przeciwników
enemyList = list[Przeciwnik]()

graj = True
while graj:
    for zdarzenie in pygame.event.get():
        if zdarzenie.type == pygame.QUIT:
            graj = False
        if zdarzenie.type == pojaw_przeciwnika:
            przeciwnik = Przeciwnik()
            przeciwnik.ustawPrzeciwnika(random.randint(0, OKNO_SZER - przeciwnik.szer), - przeciwnik.wys - 2)
            enemyList.append(przeciwnik)

    keys = pygame.key.get_pressed()

    okienko.blit(TŁO,(0,0))

    # WYKONUJE SIĘ NA KAŻDY TICK
    gracz.przesuńGracza(keys)
    gracz.rysujGracza(okienko)

    for enemy in enemyList:
        enemy.rysujPrzeciwnika(okienko)
        enemy.ruchPrzeciwnika()

    pygame.display.update()
    zegarek.tick(FPS)

pygame.quit()