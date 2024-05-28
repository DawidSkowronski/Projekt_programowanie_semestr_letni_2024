import pygame
import time
import random
import os
import math

pygame.init()
##
##      GLOBALNE
##

# GŁÓWNE
OKNO_SZER = 1200
OKNO_WYS = 700
TŁO = pygame.image.load(os.path.join("images","kosmos.png"))
GAME_OVER = pygame.image.load(os.path.join("images","game_over.png"))
font = pygame.font.Font(None,32)
FPS = 60

# SPRAJTY
statek = pygame.image.load(os.path.join("images","statek.png"))
wróg = pygame.image.load(os.path.join("images","kosmita.png"))
wróg2 = pygame.image.load(os.path.join("images","przeciwnik2.png"))
pocisk_gracza = pygame.image.load(os.path.join("images","pocisk_gracza.png"))
pocisk_wroga1 = pygame.image.load(os.path.join("images","pocisk_wróg1.png"))
pocisk_wroga2 = pygame.image.load(os.path.join("images","pocisk2.png"))


# DŹWIĘKI
dźwięk_strzału = pygame.mixer.Sound(os.path.join("sounds","laser.mp3"))
dźwięk_wróg1 = pygame.mixer.Sound(os.path.join("sounds","plasma.mp3"))
dźwięk_strzału.set_volume(.1)
pygame.mixer.init()
muza = pygame.mixer.music.load(os.path.join("music","muza.mp3"))
pygame.mixer.music.set_volume(.25)
pygame.mixer.music.play(-1, 0)

##
##      KLASY
##

# KLASA BYTU
class Byt:
    """Klasa tworząca byt w grze."""
    def __init__(self, x, y):
        self.x = x
        self.y = y

# KLASA GRACZ
class Gracz(Byt):
    """Klasa zawierająca funkcjonalność i anatomię gracza."""
    cooldown = 125
    szer = statek.get_width()
    wys = statek.get_height()
    speed = 10
    dx = 0   
    dy = 0

    def __init__(self):
        Byt.__init__(self, 0, 0)
        self.ship_img = statek
        self.mask = pygame.mask.from_surface(self.ship_img)

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
        """Pozwala graczowi wystrzelić pocisk, zwraca prawdę jeśli go wystrzeli."""
        if czas_od_pocisku > Gracz.cooldown:
            if keys[pygame.K_SPACE]:
                pociskList.append(Pocisk(self.x + self.szer//2 - 10, self.y + self.wys//2, 25, "gracz"))
                pociskList.append(Pocisk(self.x + self.szer//2 + 10, self.y + self.wys//2, 25, "gracz"))
                dźwięk_strzału.play()
                return True
        return False

    # def czy_trafił(self, obiekt):
    #     """Sprawdza, czy wystrzelony pocisk trafił w coś."""
    #     for pocisk in pociskList:
    #         if pocisk.czy_kolizja(obiekt):
    #             pociskList.remove(pocisk)

# KLASA PUNKTY GRACZA
class Scoreboard():
    def __init__(self):
        self.czy_nowy_rekord = 0
        self.score = 0
        try: 
            with open(os.path.join("pliki","rekord.txt"), 'r') as rekord:
                self.highscore = int(rekord.read())
        except:
            with open(os.path.join("pliki","rekord.txt"), 'w') as rekord:
                rekord.write(str(0))
                self.highscore = 0
        print(self.highscore)
    
    def dodawanie_punktów(self,wartość):
        self.score += wartość
        if self.highscore < self.score:
            self.czy_nowy_rekord = 1
            self.highscore = self.score
            with open(os.path.join("pliki","rekord.txt"), 'w') as rekord:
                rekord.write(str(self.score))
    
    def rysuj_scoreboard(self,surface):
        okienko.blit(font.render("Score: " + str(self.score),True,(255,255,255)),(0,0))
        if self.czy_nowy_rekord == 1:
                okienko.blit(font.render("NEW HIGHSCORE: " + str(self.highscore),True,(0, 200, 0)),(0,20))
        else:
            okienko.blit(font.render("Highscore: " + str(self.highscore),True,(255, 255, 255)),(0,20))

# KLASA ŻYCIE GRACZA
class PasekZdrowia():
    def __init__(self, max_hp):
        self.hp = max_hp
        self.max_hp = max_hp

    def rysuj_pasek(self, surface):
        poziom_hp = self.hp / self.max_hp
        pygame.draw.rect(surface, "red", (10, 660, 300, 30))
        pygame.draw.rect(surface, "green", (10, 660, 300 * poziom_hp, 30))
        okienko.blit(font.render("HP",True,'green'),(140,630))
        
    def zmiana_hp(self, wartość):
        if self.hp + wartość >=  self.max_hp:
            self.hp = self.max_hp
        elif self.hp + wartość < 0:
            self.hp = 0
        else:
            self.hp += wartość

# KLASA PRZECIWNIK
class Przeciwnik(Byt):
    stworzonychPrzeciwników = 0

    dx = 0
    dy = 0

    def __init__(self):
        Byt.__init__(self, 0, 0)

        # ID PRZECIWNIKA
        self.id = Przeciwnik.stworzonychPrzeciwników
        Przeciwnik.stworzonychPrzeciwników += 1
        self.offset = czas_płynny_ruch_przeciwnika

        if Przeciwnik.stworzonychPrzeciwników % 10 == 0:
            self.tag = "wróg2"
            self.ship_img = wróg2
            self.speed = 1
            self.pocisk_speed = 5
            self.hp = 5
        else:
            self.tag = "wróg1"
            self.ship_img = wróg
            self.speed = 3
            self.pocisk_speed = 10
            self.hp = 3

        self.szer = self.ship_img.get_width()
        self.wys = self.ship_img.get_width()
        self.mask = pygame.mask.from_surface(self.ship_img)
    
    def rysujPrzeciwnika(self):
        """Rysuje instancję przeciwnika."""
        okienko.blit(self.ship_img,(self.x,self.y))
        if self.pozaOknem1():
            print("PRZECIWNIK USUNIĘTY")
            enemyDoUsunięcia.append(self)

    def ruchPrzeciwnika(self):
        """Zmienia koordynaty przeciwnika."""
        self.dy = self.speed * abs(math.sin(2*czas_płynny_ruch_przeciwnika/FPS + self.offset%FPS)) + .5

        self.y += self.dy

    def ustawPrzeciwnika(self, x = 0, y = 0):
        """Ustawia przeciwnika na konkretne koordynaty."""
        self.x = x
        self.y = y

    def wystrzelPocisk1(self):
        """Pozwala przeciwnikowi wystrzelić pocisk"""
        pociskList.append(Pocisk(self.x + self.szer//2, self.y + self.wys//2, self.pocisk_speed, self.tag))
        #dźwięk_wróg1.play()
        return True
    
    def pozaOknem1(self):    # usuwamy przeciwników poza oknem, żeby nie zostawiać zbędnych obiektów
        """Sprawdza, czy przeciwnik znajduje się w obszarze okna, jeśli nie -  usuwa go."""
        if self.y > OKNO_WYS + 5:
            return True
        return False

# KLASA POCISK
class Pocisk(Byt):
    def __init__(self, x, y, speed, ktoStrzelił):
        if ktoStrzelił == "gracz":
            self.img = pocisk_gracza
        if ktoStrzelił == "wróg1":
            self.img = pocisk_wroga1
        if ktoStrzelił == "wróg2":
            self.img = pocisk_wroga2

        self.mask = pygame.mask.from_surface(self.img)  # mask tworzy dokładną siatkę pikseli wgranego obrazu

        Byt.__init__(self, x - self.img.get_width()//2, y - self.img.get_height()//2)
        self.speed = speed
        self.ktoStrzelił = ktoStrzelił
    
    def rysujPocisk(self):
        """Rysuje pocisk."""
        okienko.blit(self.img, (self.x, self.y))  # rysuje obraz na wyświetlanym oknie
        if self.pozaOknem():
            pociskiDoUsunięcia.append(self)
        
    def ruchPocisku(self):
        """Przemieszcza pocisk."""
        if self.ktoStrzelił == "gracz":
            self.y -= self.speed  # pocisk porusza się pionowo do góry (gracz)
        else:
            self.y += self.speed # pocisk porusza się pionowo do dołu (wrogowie)
    
    def pozaOknem(self):    # usuwamy pociski poza oknem, żeby nie zostawiać zbędnych obiektów
        """Sprawdza, czy pocisk znajduje się w obszarze okna."""
        czy_poza_oknem = False
        #if self.y < -pocisk_gracza.get_height() or self.y > OKNO_WYS: #Zrobiłem inaczej, potem się zmieni
        if self.y > OKNO_WYS or self.y < -30:
            czy_poza_oknem = True
        return czy_poza_oknem
        #Czy nie łatwiej usunąć zmienną czy_poza_oknem i po prostu odpowiednio zwracać True lub False?
    
    def czy_kolizja(self, obiekt):
        """Sprawdza, czy następuje kolizja między pociskiem a obiektem."""
        return kolizja(self, obiekt)

##
##      OBIEKTY
##

punkty = Scoreboard()
zdrowie = PasekZdrowia(100)

gracz = Gracz()
gracz.ustawGracza((OKNO_SZER - gracz.szer)//2, OKNO_WYS - gracz.wys - 50)

##
##  ZDARZENIA
## 

# pojawia przeciwnika co jakiś czas
cykl_pojawienia_przeciwnika = 1000 #(milisekundy)
pojaw_przeciwnika = pygame.USEREVENT
pygame.time.set_timer(pojaw_przeciwnika, cykl_pojawienia_przeciwnika)

# przeciwnik będzie strzelał co jakiś czas (niewykorzystane)
cykl_strzał_wróg1 = 200
strzał_wróg1 = pygame.USEREVENT + 1
pygame.time.set_timer(strzał_wróg1, cykl_strzał_wróg1)

##*************************##
##           GRA           ##
##*************************##
okienko = pygame.display.set_mode((OKNO_SZER, OKNO_WYS), 0, 32)
podział_okienka = range(0, OKNO_SZER - wróg.get_width(), wróg.get_width())
pygame.display.set_caption("Student Invaders")
pygame.display.set_icon(statek)
zegarek = pygame.time.Clock()

#   LISTY
enemyList = list[Przeciwnik]()          # lista przeciwników
pociskList = list[Pocisk]()             # lista pocisków

czas_od_pocisku = 0
czas_płynny_ruch_przeciwnika = 0

# funkcja sprawdzająca kolizję obiektów
def kolizja(obiekt1, obiekt2):
    """Sprawdza kolizję między dwoma obiektami, zwraca prawdę lub fałsz."""
    ramka_x = obiekt2.x - obiekt1.x
    ramka_y = obiekt2.y - obiekt1.y
    return obiekt1.mask.overlap(obiekt2.mask, (ramka_x, ramka_y)) != None 

graj = True
while graj:
    for zdarzenie in pygame.event.get():
        if zdarzenie.type == pygame.QUIT:
            graj = False
        if zdarzenie.type == pojaw_przeciwnika:
            przeciwnik = Przeciwnik()
            gdzie_przeciwnik = random.choice(podział_okienka)
            przeciwnik.ustawPrzeciwnika(gdzie_przeciwnik, - przeciwnik.wys - 2)
            enemyList.append(przeciwnik)
        # if zdarzenie.type == strzał_wróg1:
        #     if enemyList != []:
        #         random.choice(enemyList).wystrzelPocisk1()
            
    keys = pygame.key.get_pressed()

    okienko.blit(TŁO,(0,0))

    # WYKONUJE SIĘ NA KAŻDY TICK
    dt = zegarek.tick(FPS)
    czas_od_pocisku += dt
    czas_płynny_ruch_przeciwnika += dt/17
    print(czas_płynny_ruch_przeciwnika)

    if gracz.wystrzelPocisk(keys):
        czas_od_pocisku = 0
    
    if czas_od_pocisku > 2000:
        czas_od_pocisku = Gracz.cooldown
    

    enemyDoUsunięcia = []
    strzelający_przeciwnik = random.randint(0, 300)
    for enemy in enemyList:
        if enemy.id == strzelający_przeciwnik:
            enemy.wystrzelPocisk1()
        if kolizja(enemy, gracz):
            enemyDoUsunięcia.append(enemy)
            punkty.dodawanie_punktów(-100)
            zdrowie.zmiana_hp(-20)
        enemy.ruchPrzeciwnika()
        enemy.rysujPrzeciwnika()

    pociskiDoUsunięcia = []
    for pocisk in pociskList:
        pocisk.ruchPocisku()
        pocisk.rysujPocisk()
        if pocisk.ktoStrzelił == "gracz":
            for enemy in enemyList:
                if pocisk.czy_kolizja(enemy):
                    pociskiDoUsunięcia.append(pocisk)
                    enemy.hp += -1
                    if enemy.hp == 0:
                        punkty.dodawanie_punktów(200)
                        enemyDoUsunięcia.append(enemy)
        if pocisk.ktoStrzelił in ("wróg1", "wróg2"):
            if pocisk.czy_kolizja(gracz):
                pociskiDoUsunięcia.append(pocisk)
                punkty.dodawanie_punktów(-100)
                strata = -20 if pocisk.ktoStrzelił == "wróg1" else -40
                zdrowie.zmiana_hp(strata)
                #^^^^^^^^^^^^^^^^^^
                #tutaj zrobimy stratę hp zależną od typu przeciwnika (to jak zrobimy klasę typów przeciwnika albo wczytywanie pliku)

    for enemy in enemyDoUsunięcia:
        try:
            enemyList.remove(enemy)
        except:
            print("Błąd usunięcia przeciwnika.")
    for pocisk in pociskiDoUsunięcia:
        try:
            pociskList.remove(pocisk)
        except:
            print("Błąd usunięcia pocisku.")

    gracz.przesuńGracza(keys)
    gracz.rysujGracza(okienko)
    punkty.rysuj_scoreboard(okienko)
    zdrowie.rysuj_pasek(okienko)

    pygame.display.update()
    
    if zdrowie.hp <= 0 :
        pygame.mixer.stop()
        okienko.blit(GAME_OVER,(0,0))
        pygame.display.update()
        dźwięk = pygame.mixer.Sound('./music/game_over.mp3')
        muza = pygame.mixer.music.load(os.path.join("music","game_over.mp3"))
        pygame.mixer.music.play(-1, 0)
        pygame.time.wait(int(dźwięk.get_length()) * 1000)
        graj = False

pygame.quit()