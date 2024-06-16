import pygame
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
font = pygame.font.Font(None,32)
fps = 60
okienko = pygame.display.set_mode((OKNO_SZER, OKNO_WYS), 0, 32)

# SPRAJTY
statek = pygame.image.load(os.path.join("images","statek.png")).convert_alpha()
icon = pygame.image.load(os.path.join("images","ic_statek.png")).convert_alpha()

kosmita = pygame.image.load(os.path.join("images","kosmita.png")).convert_alpha()
kosmita_1 = pygame.image.load(os.path.join("images","kosmita_dmg1.png")).convert_alpha()
kosmita_2 = pygame.image.load(os.path.join("images","kosmita_dmg2.png")).convert_alpha()

krazownik = pygame.image.load(os.path.join("images","przeciwnik2.png")).convert_alpha()
krazownik_1 = pygame.image.load(os.path.join("images","przeciwnik2_dmg1.png")).convert_alpha()
krazownik_2 = pygame.image.load(os.path.join("images","przeciwnik2_dmg2.png")).convert_alpha()

pocisk_gracza = pygame.image.load(os.path.join("images","pocisk_gracza.png")).convert_alpha()
pocisk_kosmity = pygame.image.load(os.path.join("images","pocisk_wróg1.png")).convert_alpha()
pocisk_krazownika = pygame.image.load(os.path.join("images","pocisk2.png")).convert_alpha()

eksplozja = pygame.image.load(os.path.join("images","eksplozja1.png")).convert_alpha()
eksplozja_1 = pygame.image.load(os.path.join("images","eksplozja2.png")).convert_alpha()
eksplozja_2 = pygame.image.load(os.path.join("images","eksplozja3.png")).convert_alpha()

but_start = pygame.image.load(os.path.join("images","START.png")).convert_alpha()
but_start_hover = pygame.image.load(os.path.join("images","START1.png")).convert_alpha()
but_wyjscie = pygame.image.load(os.path.join("images","EXIT.png")).convert_alpha()
but_wyjscie_hover = pygame.image.load(os.path.join("images","EXIT1.png")).convert_alpha()
but_kontynuuj = pygame.image.load(os.path.join("images","kontynuuj.jpg")).convert_alpha()
but_kontynuuj_hover = pygame.image.load(os.path.join("images","kontynuuj1.jpg")).convert_alpha()

but_dzwiek_enabled = pygame.image.load(os.path.join("images","włączony.jpg")).convert_alpha()
but_dzwiek_enabled_hover = pygame.image.load(os.path.join("images","włączony1.jpg")).convert_alpha()
but_dzwiek_disabled = pygame.image.load(os.path.join("images","wyłączony.jpg")).convert_alpha()
but_dzwiek_disabled_hover = pygame.image.load(os.path.join("images","wyłączony1.jpg")).convert_alpha()

but_instrukcje = pygame.image.load(os.path.join("images","instrukcja.jpg")).convert_alpha()
but_instrukcje_hover = pygame.image.load(os.path.join("images","instrukcja1.jpg")).convert_alpha()

bg_instrukcje = pygame.image.load(os.path.join("images","jak.jpg")).convert_alpha()
bg_kosmos = pygame.image.load(os.path.join("images","kosmos.png")).convert_alpha()
bg_gameover = pygame.image.load(os.path.join("images","game_over.png")).convert_alpha()
bg_pauza = pygame.image.load(os.path.join("images","pauza.png")).convert_alpha()

# DŹWIĘKI
pygame.mixer.init()

# SFX
sfx_pocisk = pygame.mixer.Sound(os.path.join("sounds","laser.mp3"))
sfx_pocisk_wroga = pygame.mixer.Sound(os.path.join("sounds","plasma.mp3"))
sfx_eksplozja = pygame.mixer.Sound(os.path.join("sounds", "eksplozja.ogg"))
sfx_pocisk.set_volume(.1)
sfx_eksplozja.set_volume(.35)

# MUZYKA
mus_gameover = os.path.join("music","game_over.mp3")
mus_gra = os.path.join("music","muza.mp3")

pygame.mixer.music.load(mus_gra)
pygame.mixer.music.set_volume(.25)
#pygame.mixer.music.play(-1, 0)

##
##      KLASY
##

# KLASA BYTU
class Byt:
    """Klasa tworząca byt w grze."""
    def __init__(self, x:float, y:float, mask, obrazek:pygame.Surface = None):
        self.x = x
        self.y = y
        self.mask = mask
        self.obrazek = obrazek

# KLASA WYBUCH
class Wybuch():
    """Klasa wybuch lol lmao rofl"""
    def __init__(self, x, y):
        self.img0 = eksplozja
        self.img1 = eksplozja_1
        self.img2 = eksplozja_2
        self.x = x
        self.y = y
        self.miejsce_wybuchu = (self.x + kosmita.get_width()//2 - eksplozja.get_width()//2, self.y + kosmita.get_height()//2 - eksplozja.get_height()//2)
    
    def CzyWybuch(self, x, y, ticks_wybuchu):
        self.x = x
        self.y = y
        self.czas = ticks_wybuchu
    
    def IleOdWybuchu(self, czas_od_wybuchu):
        

        if czas_od_wybuchu - self.czas <= 225:
            if czas_od_wybuchu - self.czas <= 150:
                if czas_od_wybuchu - self.czas <= 75:
                    okienko.blit(self.img0, self.miejsce_wybuchu)
                    return
                okienko.blit(self.img1, self.miejsce_wybuchu)
                return
            okienko.blit(self.img2, self.miejsce_wybuchu)
            return
        
        else: wybuchList.remove(self)

# KLASA PRZYCISK
class Przycisk(Byt):
    """Klasa zawierająca funkcjonalność przycisków"""
    def __init__(self, x, y, but_obrazek:pygame.Surface, but_obrazek_hover:pygame.Surface = None):
        Byt.__init__(self, x, y, but_obrazek.get_rect(), but_obrazek)

        self.mask.topleft = (x, y)
        self.obrazek_hover = but_obrazek_hover

    def czyMyszka(self):
        """Sprawdza, czy myszka jest "na powierzchni" przycisku, zwraca bool."""
        myszka = pygame.mouse.get_pos()
        if self.mask.collidepoint(myszka):
            return True
        return False
    
    def rysujPrzycisk(self):
        """Wyświetla przycisk w okienku."""
        if self.czyMyszka():
            okienko.blit(self.obrazek_hover, (self.mask.x, self.mask.y))
        else:
            okienko.blit(self.obrazek, (self.mask.x, self.mask.y))

# KLASA GRACZ
class Gracz(Byt):
    """Klasa zawierająca funkcjonalność i anatomię gracza."""
    cooldown_strzalu = 125

    def __init__(self):
        mask = pygame.mask.from_surface(statek)
        Byt.__init__(self, 0, 0, mask, statek)
        self.szer = self.obrazek.get_width()
        self.wys = self.obrazek.get_height()
        self.dx = 0
        self.dy = 0
        self.predkosc = 10
        self.maks_przegrzanie = 100
        self.aktualne_przegrzanie = 0
        self.cooldown_przegrzania = 0

    def ustawGracza(self, x, y):
        """Ustawia gracza na konkretne koordynaty."""
        self.x = x
        self.y = y

    def rysujGracza(self):
        """Rysuje instancję gracza."""
        okienko.blit(self.obrazek, (self.x,self.y))

    def przesuńGracza(self):
        """Zmienia koordynaty gracza."""
        if keys[pygame.K_w]:
            self.dy = -self.predkosc
        elif keys[pygame.K_s]:
            self.dy = self.predkosc
        else:
            self.dy = 0

        if keys[pygame.K_a]:
            self.dx = -self.predkosc
        elif keys[pygame.K_d]:
            self.dx = self.predkosc
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

    def wystrzelPocisk(self):
        """Pozwala graczowi wystrzelić pocisk, zwraca prawdę jeśli go wystrzeli."""
        if czas_od_pocisku > Gracz.cooldown_strzalu + self.cooldown_przegrzania:
            if keys[pygame.K_SPACE]:
                pociskList.append(Pocisk(self.x + self.szer//2 - 10, self.y + self.wys//2, 25, "gracz"))
                pociskList.append(Pocisk(self.x + self.szer//2 + 10, self.y + self.wys//2, 25, "gracz"))
                if dźwięk:
                    sfx_pocisk.play()
                return True
        return False
    def przegranie(self):
        poziom_przegrzania = self.aktualne_przegrzanie / self.maks_przegrzanie
        if keys[pygame.K_SPACE]:
            self.aktualne_przegrzanie += 0.8
            if self.aktualne_przegrzanie > self.maks_przegrzanie:
                self.aktualne_przegrzanie = self.maks_przegrzanie
                self.cooldown_przegrzania = 10000000
        else:
            self.aktualne_przegrzanie -= 0.5
            if self.aktualne_przegrzanie < 0:
                self.aktualne_przegrzanie = 0
                self.cooldown_przegrzania = 0
        pygame.draw.rect(okienko, "gray", (self.x +125, self.y +7, 13, 120))
        pygame.draw.rect(okienko, "orange", (self.x +125, self.y +7 , 13, 120 * poziom_przegrzania))

# KLASA PUNKTY GRACZA
class Scoreboard():
    def __init__(self):
        self.wynik = 0
        try:
            os.mkdir('.\pliki')
        except:
            print("Katalog już istnieje")
        try:
            with open(os.path.join("pliki","rekord.txt"), 'r') as rekord:
                self.rekord = int(rekord.read())
        except:
            with open(os.path.join("pliki","rekord.txt"), 'w') as rekord:
                rekord.write(str(0))
                self.rekord = 0
        print(self.rekord)
    
    def dodawaniePunktów(self,wartość):
        """Dodaje punkty do wyniku."""
        self.wynik += wartość
    
    def rysujScoreboard(self):
        """Pojawia na ekranie wynik razem z rekordem."""
        okienko.blit(font.render("Wynik: " + str(self.wynik),True,(255,255,255)),(0,0))
        if self.rekord < self.wynik:
            okienko.blit(font.render("NOWY REKORD: " + str(self.wynik),True,(0, 200, 0)),(0,20))
        else:
            okienko.blit(font.render("Rekord: " + str(self.rekord),True,(255, 255, 255)),(0,20))
        if zdrowie.hp <= 0 and self.rekord < self.wynik:
            with open(os.path.join("pliki","rekord.txt"), 'w') as rekord:
                rekord.write(str(self.wynik))

# KLASA ŻYCIE GRACZA
class PasekZdrowia():
    def __init__(self, max_hp):
        self.hp = max_hp
        self.max_hp = max_hp

    def rysujPasek(self):
        """Pojawia pasek zdrowia na ekranie."""
        poziom_hp = self.hp / self.max_hp
        pygame.draw.rect(okienko, "red", (10, 660, 300, 30))
        pygame.draw.rect(okienko, "green", (10, 660, 300 * poziom_hp, 30))
        okienko.blit(font.render("HP",True,'green'),(140,630))
        
    def zmianaHp(self, wartosc:float):
        """Zmienia hp na zadaną wartość."""
        if self.hp + wartosc >=  self.max_hp:
            self.hp = self.max_hp
        elif self.hp + wartosc < 0:
            self.hp = 0
        else:
            self.hp += wartosc

# KLASA PRZECIWNIK
class Przeciwnik(Byt):
    stworzonych_przeciwnikow = 0

    dx = 0
    dy = 0

    def __init__(self, x:float = 0, y:float = 0):
        # ID PRZECIWNIKA
        self.id = Przeciwnik.stworzonych_przeciwnikow
        Przeciwnik.stworzonych_przeciwnikow += 1
        self.ruch_offset = czas_płynny_ruch_przeciwnika

        if Przeciwnik.stworzonych_przeciwnikow % 5 == 0:
            self.tag = "krążownik"
            self.obraz = krazownik
            self.obraz_1 = krazownik_1
            self.obraz_2 = krazownik_2
            self.speed = 0.5
            self.pocisk_speed = 5
            self.hp = 7
        else:
            self.tag = "kosmita"
            self.obraz = kosmita
            self.obraz_1 = kosmita_1
            self.obraz_2 = kosmita_2
            self.speed = 3
            self.pocisk_speed = 10
            self.hp = 5

        mask = pygame.mask.from_surface(self.obraz)
        Byt.__init__(self, x, y, mask, self.obraz)
        
        self.szer = self.obrazek.get_width()
        self.wys = self.obrazek.get_width()
    
    def rysujPrzeciwnika(self):
        """Rysuje instancję przeciwnika."""
        if self.hp <= 2:
            okienko.blit(self.obraz_2,(self.x,self.y))
        elif self.hp <= 4:
            okienko.blit(self.obraz_1,(self.x,self.y))
        else:
            okienko.blit(self.obraz,(self.x,self.y))
        if self.pozaOknem():
            #print("PRZECIWNIK USUNIĘTY")
            enemy_do_usunięcia.append(self)

    def ruchPrzeciwnika(self):
        """Zmienia koordynaty przeciwnika."""
        self.dy = self.speed * abs(math.sin(2*czas_płynny_ruch_przeciwnika/fps + self.ruch_offset%fps)) + .5

        self.y += self.dy

    def ustawPrzeciwnika(self, x = 0, y = 0):
        """Ustawia przeciwnika na konkretne koordynaty."""
        self.x = x
        self.y = y

    def wystrzelPocisk(self):
        """Pozwala przeciwnikowi wystrzelić pocisk"""
        pociskList.append(Pocisk(self.x + self.szer//2, self.y + self.wys//2, self.pocisk_speed, self.tag))
        #if dźwięk: dźwięk_wróg1.play()
        return True
    
    def pozaOknem(self):    # usuwamy przeciwników poza oknem, żeby nie zostawiać zbędnych obiektów
        """Sprawdza, czy przeciwnik znajduje się w obszarze okna, jeśli nie -  usuwa go."""
        if self.y > OKNO_WYS + 5:
            return True
        return False

# KLASA POCISK
class Pocisk(Byt):
    def __init__(self, x:float, y:float, predkosc:float, kto_strzelił:str):
        if kto_strzelił == "gracz":
            obrazek = pocisk_gracza
        if kto_strzelił == "kosmita":
            obrazek = pocisk_kosmity
        if kto_strzelił == "krążownik":
            obrazek = pocisk_krazownika

        mask = pygame.mask.from_surface(obrazek)  # mask tworzy dokładną siatkę pikseli wgranego obrazu

        Byt.__init__(self, x - obrazek.get_width()//2, y - obrazek.get_height()//2, mask, obrazek)
        self.predkosc = predkosc
        self.kto_strzelił = kto_strzelił
    
    def rysujPocisk(self):
        """Rysuje pocisk."""
        okienko.blit(self.obrazek, (self.x, self.y))  # rysuje obraz na wyświetlanym oknie
        if self.pozaOknem():
            pociski_do_usunięcia.append(self)
        
    def ruchPocisku(self):
        """Przemieszcza pocisk."""
        if self.kto_strzelił == "gracz":
            self.y -= self.predkosc  # pocisk porusza się pionowo do góry (gracz)
        else:
            self.y += self.predkosc # pocisk porusza się pionowo do dołu (wrog1)
    
    def pozaOknem(self):    # usuwamy pociski poza oknem, żeby nie zostawiać zbędnych obiektów
        """Sprawdza, czy pocisk znajduje się w obszarze okna."""
        czy_poza_oknem = False
        #if self.y < -pocisk_gracza.get_height() or self.y > OKNO_WYS: #Zrobiłem inaczej, potem się zmieni
        if self.y > OKNO_WYS or self.y < -30:
            czy_poza_oknem = True
        return czy_poza_oknem
        #Czy nie łatwiej usunąć zmienną czy_poza_oknem i po prostu odpowiednio zwracać True lub False?
    
    def czyKolizja(self, obiekt):
        """Sprawdza, czy następuje kolizja między pociskiem a obiektem."""
        return kolizja(self, obiekt)

# KLASA SCENA
class Scena():
    obecna_scena = None

    def __init__(self, tag:str, przyciski:list[Przycisk] = []):
        self.tag = tag
        self.przyciski = przyciski

    def rysujPrzyciski(self):
        for przycisk in self.przyciski:
            przycisk.rysujPrzycisk()

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
cykl_pojawienia_przeciwnika = 1000 #(milisekundy) <----------- TUTAJ BYM COŚ PRZEROBIŁ JAKOŚ ***************
pojaw_przeciwnika = pygame.USEREVENT
pygame.time.set_timer(pojaw_przeciwnika, cykl_pojawienia_przeciwnika)

# # przeciwnik będzie strzelał co jakiś czas (niewykorzystane)
# cykl_strzał_wróg1 = 200
# strzał_wróg1 = pygame.USEREVENT + 1
# pygame.time.set_timer(strzał_wróg1, cykl_strzał_wróg1)

##*************************##
##           GRA           ##
##*************************##

pygame.display.set_icon(icon)
#okienko = pygame.display.set_mode((OKNO_SZER, OKNO_WYS), 0, 32)
podział_okienka = range(0, OKNO_SZER - kosmita.get_width(), kosmita.get_width())
pygame.display.set_caption("Student Invaders")
zegarek = pygame.time.Clock()

# LISTY
enemyList = list[Przeciwnik]()          # lista przeciwników
pociskList = list[Pocisk]()             # lista pocisków
wybuchList = list[Wybuch]()             # lista wybuchów

czas_od_pocisku = 0
czas_płynny_ruch_przeciwnika = 0

# funkcja sprawdzająca kolizję obiektów
def kolizja(obiekt1, obiekt2):
    """Sprawdza kolizję między dwoma obiektami, zwraca prawdę lub fałsz."""
    ramka_x = obiekt2.x - obiekt1.x
    ramka_y = obiekt2.y - obiekt1.y
    return obiekt1.mask.overlap(obiekt2.mask, (ramka_x, ramka_y)) != None


# PRZYCISKI
WZNÓW = Przycisk(0, 200, but_kontynuuj, but_kontynuuj_hover)
WYJDŹ = Przycisk(200, 200, but_wyjscie, but_wyjscie_hover)
START = Przycisk(0, 0, but_start, but_start_hover)
EXIT = Przycisk(450, 0, but_wyjscie, but_wyjscie_hover)
INSTRUKCJA = Przycisk(0, 500, but_instrukcje, but_instrukcje_hover)
DŹWIĘK_ON = Przycisk(450, 500, but_dzwiek_enabled, but_dzwiek_enabled_hover)
DŹWIĘK_OFF = Przycisk(450, 500, but_dzwiek_disabled, but_dzwiek_disabled_hover)
DŹWIĘKI=[DŹWIĘK_ON, DŹWIĘK_OFF]
DŹWIĘK = DŹWIĘK_ON
dźwięk = True

MENU_PONOWNIE = Przycisk(0, 0, but_dzwiek_enabled, but_dzwiek_enabled_hover)
WYJDŹ_PONOWNIE = Przycisk(0, 400, but_wyjscie, but_wyjscie_hover)
GRAJ_PONOWNIE = Przycisk(400, 0, but_start, but_start_hover)

# SCENY
SCENA_MENU = Scena("MENU", [START, INSTRUKCJA, EXIT])
SCENA_GRA = Scena("GRA")
SCENA_INSTRUKCJE = Scena("INSTRUKCJE", [INSTRUKCJA])
SCENA_PAUZA = Scena("PAUZA", [WZNÓW, WYJDŹ])
SCENA_ŚMIERĆ = Scena("ŚMIERĆ", [MENU_PONOWNIE, WYJDŹ_PONOWNIE, GRAJ_PONOWNIE])

Scena.obecna_scena = SCENA_MENU

# GRA
scena : Scena = Scena.obecna_scena
graj = True
while graj:
    scena = Scena.obecna_scena
    dt = zegarek.tick(fps)
    keys = pygame.key.get_pressed()
    pygame.display.update()

    zdarzenia = pygame.event.get()  #to chyba najwazniejsza linijka programu

    for zdarzenie in zdarzenia:
        if zdarzenie.type == pygame.QUIT:
            graj = False
    
    if scena == SCENA_MENU:
        okienko.fill('black')

        scena.rysujPrzyciski()
        DŹWIĘK.rysujPrzycisk()
        
        if keys[pygame.K_LSHIFT]:
            Scena.obecna_scena = SCENA_GRA
        if keys[pygame.K_ESCAPE]:
            graj = False

        for zdarzenie in zdarzenia:
            if zdarzenie.type == pygame.MOUSEBUTTONUP:
                if START.czyMyszka():
                    if dźwięk:
                        pygame.mixer.music.play(-1, 0)
                    Scena.obecna_scena = SCENA_GRA
                if EXIT.czyMyszka():
                    graj = False
                if DŹWIĘK.czyMyszka():
                    dźwięk = not dźwięk
                    if dźwięk:
                        DŹWIĘK = DŹWIĘK_ON
                    else:
                        DŹWIĘK = DŹWIĘK_OFF
                if INSTRUKCJA.czyMyszka():
                    Scena.obecna_scena = SCENA_INSTRUKCJE
    elif scena == SCENA_INSTRUKCJE:
        okienko.blit(bg_instrukcje, (0, 0))
        scena.rysujPrzyciski()
        for zdarzenie in zdarzenia:
            if zdarzenie.type == pygame.KEYDOWN:
                zdarzenie.key == pygame.K_ESCAPE
                Scena.obecna_scena = SCENA_MENU
            if zdarzenie.type == pygame.MOUSEBUTTONUP and INSTRUKCJA.czyMyszka():
                Scena.obecna_scena = SCENA_MENU
    elif scena == SCENA_GRA:
        for zdarzenie in zdarzenia:
            if zdarzenie.type == pygame.QUIT:
                graj = False
            if zdarzenie.type == pojaw_przeciwnika: #pauza is False po to, aby przeciwnicy nie generowali się w trakcie pauzy
                przeciwnik = Przeciwnik()
                gdzie_przeciwnik = random.choice(podział_okienka)
                przeciwnik.ustawPrzeciwnika(gdzie_przeciwnik, - przeciwnik.wys - 2)
                enemyList.append(przeciwnik)
            if zdarzenie.type == pygame.KEYDOWN:
                if zdarzenie.key == pygame.K_ESCAPE:
                    Scena.obecna_scena = SCENA_PAUZA
                    pygame.mixer.music.set_volume(.03)
                elif zdarzenie.key == pygame.K_c:
                    print(pygame.time.get_ticks())


            # if zdarzenie.type == strzał_wróg1:
            #     if enemyList != []:
            #         random.choice(enemyList).wystrzelPocisk1()

        # WYKONUJE SIĘ NA KAŻDY TICK
        okienko.blit(bg_kosmos, (0,0))
        czas_od_pocisku += dt
        czas_płynny_ruch_przeciwnika += dt/17
        #print(czas_płynny_ruch_przeciwnika)

        if gracz.wystrzelPocisk():
            czas_od_pocisku = 0
        
        if czas_od_pocisku > 2000:
            czas_od_pocisku = Gracz.cooldown_strzalu
        
        enemy_do_usunięcia = []
        strzelający_przeciwnik = random.randint(0, 300)
        for enemy in enemyList:
            if enemy.id == strzelający_przeciwnik:
                enemy.wystrzelPocisk()
            if kolizja(enemy, gracz):
                enemy_do_usunięcia.append(enemy)
                punkty.dodawaniePunktów(-100)
                zdrowie.zmianaHp(-20)
            enemy.ruchPrzeciwnika()
            enemy.rysujPrzeciwnika()
        
        pociski_do_usunięcia = []
        for pocisk in pociskList:
            pocisk.ruchPocisku()
            pocisk.rysujPocisk()
            if pocisk.kto_strzelił == "gracz":
                for enemy in enemyList:
                    if pocisk.czyKolizja(enemy):
                        pociski_do_usunięcia.append(pocisk)
                        enemy.hp += -1
                        if enemy.hp == 0:
                            punkty.dodawaniePunktów(200)
                            enemy_do_usunięcia.append(enemy)
            if pocisk.kto_strzelił in ("kosmita", "krążownik"):
                if pocisk.czyKolizja(gracz):
                    pociski_do_usunięcia.append(pocisk)
                    punkty.dodawaniePunktów(-100)
                    strata = -20 if pocisk.kto_strzelił == "kosmita" else -40
                    zdrowie.zmianaHp(strata)
                    #^^^^^^^^^^^^^^^^^^
                    #tutaj zrobimy stratę hp zależną od typu przeciwnika (to jak zrobimy klasę typów przeciwnika albo wczytywanie pliku)
        
        czas = pygame.time.get_ticks()
        
        for enemy in enemy_do_usunięcia:
            wybuch = Wybuch(enemy.x, enemy.y)
            wybuch.CzyWybuch(enemy.x, enemy.y, czas)
            wybuchList.append(wybuch)
            if dźwięk:
                sfx_eksplozja.play()
            try:
                enemyList.remove(enemy)
            except:
                print("Błąd usunięcia przeciwnika.")
        for pocisk in pociski_do_usunięcia:
            try:
                pociskList.remove(pocisk)
            except:
                print("Błąd usunięcia pocisku.")
        gracz.przesuńGracza()
        gracz.rysujGracza()
        gracz.przegranie()
        punkty.rysujScoreboard()
        zdrowie.rysujPasek()

        for wybuch in wybuchList:
            wybuch.IleOdWybuchu(czas)
        
        if zdrowie.hp <= 0:
            
            Scena.obecna_scena = SCENA_ŚMIERĆ
            pygame.mixer.music.load(mus_gameover)
            pygame.mixer.music.play()

            punkty.wynik = 0
            zdrowie.hp = zdrowie.max_hp
            #gracz = Gracz()
            gracz.ustawGracza((OKNO_SZER - gracz.szer)//2, OKNO_WYS - gracz.wys - 50)
            Przeciwnik.stworzonych_przeciwnikow = 0

            enemyList = []
            pociskList = []
            wybuchList = []          #Czyścimy listy, aby przeciwnicy, wybuchy oraz pociski z poprzedniej rundy nie pojawiali się w nowej
    elif scena == SCENA_PAUZA:
        okienko.blit(bg_pauza, (0, 0))
        scena.rysujPrzyciski()
        pygame.display.update() # to ważne, nie usuwać
        for zdarzenie in zdarzenia:
            if zdarzenie.type == pygame.QUIT:
                graj = False
            if zdarzenie.type == pygame.KEYDOWN:
                if zdarzenie.key == pygame.K_LSHIFT: # chciałem enter ale nie działa
                    pygame.mixer.music.set_volume(.25)
                    Scena.obecna_scena = SCENA_GRA
                elif zdarzenie.key == pygame.K_ESCAPE:
                    graj = False
            elif zdarzenie.type == pygame.MOUSEBUTTONDOWN:
                if WZNÓW.czyMyszka():
                    pygame.mixer.music.set_volume(.25)
                    Scena.obecna_scena = SCENA_GRA
                elif WYJDŹ.czyMyszka():
                    graj = False
                    pauza = False
    elif scena == SCENA_ŚMIERĆ:
        okienko.blit(bg_gameover, (0,0))

        scena.rysujPrzyciski()

        for zdarzenie in zdarzenia:
            if zdarzenie.type == pygame.QUIT:
                pygame.mixer.stop()
            if zdarzenie.type == pygame.MOUSEBUTTONUP:
                if WYJDŹ_PONOWNIE.czyMyszka():
                    pygame.mixer.stop()
                    graj = False
                elif MENU_PONOWNIE.czyMyszka():
                    Scena.obecna_scena = SCENA_MENU
                    pygame.mixer.stop()
                    pygame.mixer.music.load(mus_gra)
                elif GRAJ_PONOWNIE.czyMyszka():
                    Scena.obecna_scena = SCENA_GRA
                    
                    pygame.mixer.music.stop()
                    pygame.mixer.music.load(mus_gra)
                    pygame.mixer.music.play()

pygame.quit()