import pygame
import random
import os
import math

pygame.init()
##
##      GLOBALNE
##

# ILOŚĆ RAKIET (DO TESTÓW)
pakiet_rakiet = 20

# GŁÓWNE
OKNO_SZER = 720
OKNO_WYS = 960
font = pygame.font.Font(None,32)
fps = 60
okienko = pygame.display.set_mode((OKNO_SZER, OKNO_WYS), 0, 32)

black = pygame.Surface((OKNO_SZER, OKNO_WYS))
black.set_alpha(255)
black.fill((0, 0, 0))
# SPRAJTY
statek = pygame.image.load(os.path.join("images","statek.png")).convert_alpha()
icon = pygame.image.load(os.path.join("images","ic_statek.png")).convert_alpha()

kosmita = pygame.image.load(os.path.join("images","kosmita.png")).convert_alpha()
kosmita_1 = pygame.image.load(os.path.join("images","kosmita_dmg1.png")).convert_alpha()
kosmita_2 = pygame.image.load(os.path.join("images","kosmita_dmg2.png")).convert_alpha()

kamikaze = pygame.image.load(os.path.join("images","kamikaze.png")).convert_alpha()
kamikaze_szarza = pygame.image.load(os.path.join("images","kamikaze_szarża.png"))

krazownik = pygame.image.load(os.path.join("images","przeciwnik2.png")).convert_alpha()
krazownik_1 = pygame.image.load(os.path.join("images","przeciwnik2_dmg1.png")).convert_alpha()
krazownik_2 = pygame.image.load(os.path.join("images","przeciwnik2_dmg2.png")).convert_alpha()

pocisk_gracza = pygame.image.load(os.path.join("images","pocisk_gracza.png")).convert_alpha()
pocisk_gracza1 = pygame.image.load(os.path.join("images","rakieta.png")).convert_alpha()
pocisk_kosmity = pygame.image.load(os.path.join("images","pocisk_wróg1.png")).convert_alpha()
pocisk_krazownika = pygame.image.load(os.path.join("images","pocisk2.png")).convert_alpha()

eksplozja = pygame.image.load(os.path.join("images","eksplozja1.png")).convert_alpha()
eksplozja_1 = pygame.image.load(os.path.join("images","eksplozja2.png")).convert_alpha()
eksplozja_2 = pygame.image.load(os.path.join("images","eksplozja3.png")).convert_alpha()

bonus_klucz = pygame.image.load(os.path.join("images","klucz_naprawczy.png")).convert_alpha()

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

bg_intro1 = pygame.image.load(os.path.join("images","intro1.png")).convert()
bg_intro2 = pygame.image.load(os.path.join("images","saul_goodman.png")).convert_alpha()

logo = pygame.image.load(os.path.join("images","logo.png")).convert_alpha()

# DŹWIĘKI
pygame.mixer.init()

# SFX
sfx_pocisk = pygame.mixer.Sound(os.path.join("sounds","laser.mp3"))
sfx_pocisk_wroga = pygame.mixer.Sound(os.path.join("sounds","plasma.mp3"))
sfx_eksplozja = pygame.mixer.Sound(os.path.join("sounds", "eksplozja.ogg"))
sfx_rakieta = pygame.mixer.Sound(os.path.join("sounds", "rakieta.mp3"))
sfx_eksplozja_rakiety = pygame.mixer.Sound(os.path.join("sounds", "eksplozja_rakieta.mp3"))
sfx_alarm = pygame.mixer.Sound(os.path.join("sounds","alarm.wav"))
sfx_tsss = pygame.mixer.Sound(os.path.join("sounds","tsss.mp3"))
sfx_leczenie = pygame.mixer.Sound(os.path.join("sounds","leczenie.mp3"))
sfx_tarcza_on = pygame.mixer.Sound(os.path.join("sounds","tarcza_on.wav"))
sfx_tarcza_off = pygame.mixer.Sound(os.path.join("sounds","tarcza_off.wav"))
sfx_rakieta_bonus = pygame.mixer.Sound(os.path.join("sounds","rakieta_bonus.wav"))

sfx_pocisk.set_volume(.1)
sfx_eksplozja.set_volume(.35)
sfx_rakieta.set_volume(.15)
sfx_eksplozja_rakiety.set_volume(.1)
sfx_alarm.set_volume(.1)
sfx_tsss.set_volume(.2)
sfx_leczenie.set_volume(.5)
sfx_tarcza_on.set_volume(.5)
sfx_tarcza_off.set_volume(.5)
sfx_rakieta_bonus.set_volume(.5)

# MUZYKA
mus_gameover = os.path.join("music","game_over.mp3")
mus_gra = os.path.join("music","muza.mp3")
mus_menu = os.path.join("music","menu.mp3")
mus_goodman = os.path.join("music","saul_goodman.mp3")

pygame.mixer.music.load(mus_goodman)
pygame.mixer.music.set_volume(.25)
#pygame.mixer.music.play(-1, 0)

##
##      KLASY
##

class Tło:
    def __init__(self, y):
        self.y = y
        self.img = bg_kosmos

    def ruchTła(self):
        self.y += .33
        if self.y >= OKNO_WYS:
            self.y = -OKNO_WYS

    def rysujTło(self):
        self.ruchTła()
        okienko.blit(self.img, (0, self.y))

TŁO1 = Tło(-OKNO_WYS)
TŁO2 = Tło(0)

# KLASA BYTU
class Byt:
    """Klasa tworząca byt w grze."""
    def __init__(self, x:float, y:float, mask, obrazek:pygame.Surface = None):
        self.x = x
        self.y = y
        self.mask = mask
        self.obrazek = obrazek

# KLASA WYBUCH
class Wybuch:
    """Klasa wybuch lol lmao rofl"""
    def __init__(self, x, y):
        self.img0 = eksplozja
        self.img1 = eksplozja_1
        self.img2 = eksplozja_2
        self.x = x
        self.y = y
        self.miejsce_wybuchu = (self.x + kosmita.get_width()//2 - eksplozja.get_width()//2, self.y + kosmita.get_height()//2 - eksplozja.get_height()//2)
        self.miejsce_wybuchu1 = (self.x + pocisk_gracza1.get_width()//2 - (eksplozja.get_width()//2)*2, self.y + pocisk_gracza1.get_height()//2 - (eksplozja.get_height()//2)*2)
    
    def CzyWybuch(self, x, y, ticks_wybuchu, T_F):
        self.x = x
        self.y = y
        self.czas = ticks_wybuchu
        self.rakieta = T_F
    
    def IleOdWybuchu(self, czas_od_wybuchu):
        if czas_od_wybuchu - self.czas <= 225:
            if czas_od_wybuchu - self.czas <= 150:
                if czas_od_wybuchu - self.czas <= 75:
                    if self.rakieta:
                        okienko.blit(pygame.transform.smoothscale(self.img0, [self.img0.get_width()*2, self.img0.get_height()*2]), self.miejsce_wybuchu1)
                    else:
                        okienko.blit(self.img0, self.miejsce_wybuchu)
                    return
                if self.rakieta:
                    okienko.blit(pygame.transform.smoothscale(self.img0, [self.img0.get_width()*2, self.img0.get_height()*2]), self.miejsce_wybuchu1)
                else:
                    okienko.blit(self.img1, self.miejsce_wybuchu)
                return
            if self.rakieta:
                okienko.blit(pygame.transform.smoothscale(self.img0, [self.img0.get_width()*2, self.img0.get_height()*2]), self.miejsce_wybuchu1)
            else:
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
    
    def ustawPrzycisk(self, x : float, y : float):
        """Ustawia przycisk na zadane koordynaty."""
        self.x = x
        self.y = y
        self.mask.topleft = (x, y)
    
    def rysujPrzycisk(self):
        """Wyświetla przycisk w okienku."""
        if self.czyMyszka():
            okienko.blit(self.obrazek_hover, (self.mask.x, self.mask.y))
        else:
            okienko.blit(self.obrazek, (self.mask.x, self.mask.y))

# KLASA BONUSY
class Bonusy(Byt):
    stworzone_bonusy = 0

    dx = 0
    dy = 0
    poprzedni_pwr_up = 0
    
    def __init__(self, x:float = 0, y:float = 0):
        self.x = x
        self.y = y
        self.speed = 2.5
        self.nietrafiony = True
        self.z_prawej_do_lewej = random.choice([True, False])
        print(self.z_prawej_do_lewej)
        if zdrowie.hp >= zdrowie.max_hp:
            self.pwr_up = random.choice([i for i in range(1, 4) if i != Bonusy.poprzedni_pwr_up])
            Bonusy.poprzedni_pwr_up = self.pwr_up
        elif zdrowie.hp >= zdrowie.max_hp * 0.3:
            self.pwr_up = random.choice([i for i in range(1, 5) if i != Bonusy.poprzedni_pwr_up])
            Bonusy.poprzedni_pwr_up = self.pwr_up
        else:
            self.pwr_up = 4
            Bonusy.poprzedni_pwr_up = self.pwr_up
        #print(Bonusy.poprzedni_pwr_up)
        if self.pwr_up == 1:
            self.obraz = pocisk_kosmity
        elif self.pwr_up == 2:
            self.obraz = pocisk_gracza1
        elif self.pwr_up == 3:
            self.obraz = pocisk_krazownika
        elif self.pwr_up == 4:
            self.obraz = bonus_klucz
        
        mask = pygame.mask.from_surface(self.obraz)
        Byt.__init__(self, x, y, mask, self.obraz)
        self.szer = self.obrazek.get_width()
        self.wys = self.obrazek.get_width()

    def rysujBonus(self):
        okienko.blit(self.obraz,(self.x,self.y))
        if self.z_prawej_do_lewej and self.x <= 0 - self.obraz.get_width() - 5:
            print("BONUS USUNIĘTY")
            bonusList.remove(self)
            del self
        elif self.x >= OKNO_SZER + self.obraz.get_width() + 5:
            print("BONUS USUNIĘTY")
            bonusList.remove(self)
            del self

    def ruchBonusu(self):
        self.dx = self.speed
        if self.z_prawej_do_lewej:
            self.x -= self.dx
        else:
            self.x += self.dx
        self.dy = (self.speed*math.sin(czas_ruch_bonusu/10))
        self.y -= self.dy
    
    def ustawBonus(self):
        if self.z_prawej_do_lewej:
            self.x = OKNO_SZER
        else:
            self.x = 0 - self.obraz.get_width()
        self.y = OKNO_WYS//3*2 + 50 - random.random() * (OKNO_WYS//3 - 50)
        #Zakres "spawnu": (OKNO_WYS//3 ; OKNO_WYS//3*2 + 50], można zmienić, bo funkcja malejąca, a random.random() zwraca wartości w zakresie [0.0, 1.0)

# KLASA GRACZ
class Gracz(Byt):
    """Klasa zawierająca funkcjonalność i anatomię gracza."""
    cooldown_strzalu = 125
    cooldown_rakiety = 500
    ilość_rakiet = pakiet_rakiet
    niezniszczalność_bonus = False
    przegrzanie_bonus = False
    
    def __init__(self):
        mask = pygame.mask.from_surface(statek)
        Byt.__init__(self, 0, 0, mask, statek)
        self.szer = self.obrazek.get_width()
        self.wys = self.obrazek.get_height()
        self.obrazek1 = but_start
        self.dx = 0
        self.dy = 0
        self.predkosc = 10
        self.maks_przegrzanie = 100
        self.aktualne_przegrzanie = self.maks_przegrzanie
        self.cooldown_przegrzania = 0

    def ustawGracza(self, x, y):
        """Ustawia gracza na konkretne koordynaty."""
        self.x = x
        self.y = y

    def rysujGracza(self):
        """Rysuje instancję gracza."""
        if Gracz.niezniszczalność_bonus:
            okienko.blit(self.obrazek1, (self.x,self.y))
            return
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
    
    def wystrzelRakiete(self):
        """Pozwala graczowi wystrzelić rakietę, zwraca prawdę jeśli ją wystrzeli."""
        if czas_od_rakiety > Gracz.cooldown_rakiety:
            if keys[pygame.K_LSHIFT] and Gracz.ilość_rakiet > 0:
                pociskList.append(Pocisk(self.x + self.szer//2, self.y + self.wys//2, 15, "rakieta"))
                Gracz.ilość_rakiet += -1
                if dźwięk:
                    sfx_rakieta.play()
                return True
        return False
    
    def przegrzanie(self):
        self.poziom_przegrzania = self.aktualne_przegrzanie / self.maks_przegrzanie
        if Gracz.przegrzanie_bonus is False:
            if keys[pygame.K_SPACE]:
                if self.cooldown_przegrzania == 0:
                    self.aktualne_przegrzanie -= .5
                elif self.aktualne_przegrzanie > self.maks_przegrzanie:
                        self.aktualne_przegrzanie = self.maks_przegrzanie
                        self.cooldown_przegrzania = 0
                else:
                    self.aktualne_przegrzanie += 1
                if self.aktualne_przegrzanie < 0:
                    self.aktualne_przegrzanie = 0
                    self.cooldown_przegrzania = 1000000
                    sfx_alarm.stop()
                    #sfx_tsss.play()
                if self.aktualne_przegrzanie == 30.5:
                    sfx_alarm.play()
            else:
                if self.aktualne_przegrzanie > 30.5:
                    sfx_alarm.stop()
                self.aktualne_przegrzanie += 2
                if self.aktualne_przegrzanie > self.maks_przegrzanie:
                    self.aktualne_przegrzanie = self.maks_przegrzanie
                    self.cooldown_przegrzania = 0
        if Gracz.przegrzanie_bonus is True:
            sfx_alarm.stop()
        pygame.draw.rect(okienko, "orange", (self.x +125, self.y +7, 13, 120))
        pygame.draw.rect(okienko, "gray", (self.x +125, self.y +7 , 13, 120 * self.poziom_przegrzania))

# KLASA PUNKTY GRACZA
class Scoreboard:
    def __init__(self):
        self.wynik = 0
        try:
            os.mkdir('.\pliki')
        except:
            pass
        try:
            with open(os.path.join("pliki","rekord.txt"), 'r') as rekord:
                self.rekord = int(rekord.read())
        except:
            with open(os.path.join("pliki","rekord.txt"), 'w') as rekord:
                rekord.write(str(0))
                self.rekord = 0
        #print(self.rekord)

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
        okienko.blit(font.render("Ilość rakiet: " + str(Gracz.ilość_rakiet),True,(255,255,255)),(0,40))
    
    def resetRekordu(self):
        """Zeruje najlepszy wynik gracza"""
        print(self.rekord)
        with open(os.path.join("pliki","rekord.txt"), 'w') as rekord:
            rekord.write(str(0))
            self.rekord = 0
        
# KLASA ŻYCIE GRACZA
class PasekZdrowia:
    def __init__(self, max_hp):
        self.hp = max_hp
        self.max_hp = max_hp

    def rysujPasek(self):
        """Pojawia pasek zdrowia na ekranie."""
        poziom_hp = self.hp / self.max_hp
        pygame.draw.rect(okienko, "red", (10, OKNO_WYS - 40, 300, 30))
        pygame.draw.rect(okienko, "green", (10, OKNO_WYS - 40, 300 * poziom_hp, 30))
        okienko.blit(font.render("HP",True,'green'),(140,OKNO_WYS - font.get_height() - 40))
        
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

    def __init__(self, x:float = 0, y:float = 0, typ:str = "kosmita", czas_powstania:float = 0):
        # ID PRZECIWNIKA
        self.id = Przeciwnik.stworzonych_przeciwnikow
        self.tag = typ
        Przeciwnik.stworzonych_przeciwnikow += 1
        self.ruch_offset = czas_płynny_ruch_przeciwnika

        if self.tag == "krążownik":
            self.obraz = krazownik
            self.obraz_1 = krazownik_1
            self.obraz_2 = krazownik_2
            self.speed = 1
            self.pocisk_speed = 10
            self.hp = 15
        elif self.tag == "kosmita":
            self.obraz = kosmita
            self.obraz_1 = kosmita_1
            self.obraz_2 = kosmita_2
            self.speed = 3
            self.pocisk_speed = 15
            self.hp = 5
        elif self.tag == "kamikaze":
            self.obraz = kamikaze
            self.obraz_1 = kamikaze
            self.obraz_2 = kamikaze_szarza
            self.speed = 3
            self.pocisk_speed = 0
            self.hp = 4

        self.czas_powstania = czas_powstania
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
        if self.tag == "kamikaze":
            czas_zachowania = czas - self.czas_powstania
            print(czas_zachowania)
            if czas_zachowania < 500:
                self.dy = self.speed * 4*math.cos(math.radians(czas_zachowania//5.5))
            elif czas_zachowania < 800:
                self.dy = self.speed/2 * math.cos(math.radians(czas_zachowania//5.5))
            else:
                self.hp = 2
                self.dy += self.speed/10
        elif self.tag == "krążownik":
            self.dy = self.speed
        elif self.tag == "kosmita":
            self.dy = self.speed * abs(math.sin(2*czas_płynny_ruch_przeciwnika/fps + self.ruch_offset%fps)) + .5

        self.y += self.dy

    def ustawPrzeciwnika(self, x = 0, y = 0):
        """Ustawia przeciwnika na konkretne koordynaty."""
        self.x = x
        self.y = y

    def wystrzelPocisk(self):
        """Pozwala przeciwnikowi wystrzelić pocisk"""
        if self.tag == "kamikaze":
            return False
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
        elif kto_strzelił == "kosmita":
            obrazek = pocisk_kosmity
        elif kto_strzelił == "krążownik":
            obrazek = pocisk_krazownika
        elif kto_strzelił == "rakieta":
            obrazek = pocisk_gracza1

        mask = pygame.mask.from_surface(obrazek)  # mask tworzy dokładną siatkę pikseli wgranego obrazu

        Byt.__init__(self, x - obrazek.get_width()//2, y - obrazek.get_height()//2, mask, obrazek)
        self.predkosc = predkosc
        self.kto_strzelił = kto_strzelił
        self.czas_płynny_ruch_rakiety = 0
    
    def rysujPocisk(self):
        """Rysuje pocisk."""
        okienko.blit(self.obrazek, (self.x, self.y))  # rysuje obraz na wyświetlanym oknie
        if self.pozaOknem():
            pociski_do_usunięcia.append(self)
        
    def ruchPocisku(self):
        """Przemieszcza pocisk."""
        if self.kto_strzelił == "gracz":
            self.y -= self.predkosc  # pocisk porusza się pionowo do góry (gracz)
        elif self.kto_strzelił == "rakieta":
            self.czas_płynny_ruch_rakiety += dt/17
            self.y -= self.predkosc * self.czas_płynny_ruch_rakiety / fps *.5
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

# KLASA FAZA
class Faza:
    wszystkie_fazy = 0

    def __init__(self, przeciwnicy:list[str], czestotliwosci:list[tuple], cykl_pojawiania:float):
        self.przeciwnicy = przeciwnicy
        self.czestotliwosci = czestotliwosci
        self.pojaw_przeciwnika = pygame.USEREVENT + 100 + Faza.wszystkie_fazy
        pygame.time.set_timer(self.pojaw_przeciwnika, cykl_pojawiania)

        Faza.wszystkie_fazy += 1

    def pojawPrzeciwnika(self):
        for zdarzenie in zdarzenia:
            if zdarzenie.type == self.pojaw_przeciwnika:
                rint = random.randint(1,100)
                i = 0
                typ_wybrany = self.przeciwnicy[0]
                print(rint)
                for typ in self.przeciwnicy:
                    if rint in range(self.czestotliwosci[i][0], self.czestotliwosci[i][1]):
                        typ_wybrany = typ
                    i += 1
                gdzie_przeciwnik = random.choice(podział_okienka)
                przeciwnik = Przeciwnik(typ=typ_wybrany, czas_powstania=czas)
                przeciwnik.ustawPrzeciwnika(gdzie_przeciwnik, - przeciwnik.wys - 2)
                enemyList.append(przeciwnik)

FAZA0 = Faza(["kosmita", "krążownik"], [(1, 80), (81, 100)], 1500)
FAZA1 = Faza(["kamikaze"], [(1, 100)], 1000)
FAZA2 = Faza(["kosmita", "kamikaze"], [(1,80), (81, 100)], 1250)
FAZA3 = Faza(["krążownik", "kamikaze"], [(1, 60), (61, 100)], 1000)
FAZA4 = Faza(["kosmita"], [(1, 100)], 500)
FAZA5 = Faza(["kosmita", "krążownik", "kamikaze"], [(1,50),(51,75),(76,100)], 1000)
FAZA6 = Faza(["kosmita", "kamikaze"], [(1, 10), (11, 90)], 500)

# KLASA SCENA
class Scena:
    obecna_scena = None
    faza:Faza = FAZA0

    def __init__(self, tag:str, przyciski:list[Przycisk] = []):
        self.tag = tag
        self.przyciski = przyciski
        if self.tag == "MENU":
            self.przyciski[0].ustawPrzycisk(OKNO_SZER//2 - self.przyciski[0].obrazek.get_width()//2, OKNO_WYS//2 - przyciski[0].obrazek.get_height() - 50)
            self.przyciski[1].ustawPrzycisk(OKNO_SZER//2 - self.przyciski[1].obrazek.get_width()//2, OKNO_WYS//2 + przyciski[1].obrazek.get_height() - 50)
            self.przyciski[2].ustawPrzycisk(OKNO_SZER//2 - self.przyciski[2].obrazek.get_width()//2, OKNO_WYS//2 + 2* przyciski[2].obrazek.get_height() - 20)

    def rysujPrzyciski(self):
        for przycisk in self.przyciski:
            przycisk.rysujPrzycisk()

    @staticmethod
    def fazaGry():
        if Scena.obecna_scena == SCENA_GRA:
            Scena.faza.pojawPrzeciwnika()
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

cykl_pojawienia_pwr_up = 15

##*************************##
##           GRA           ##
##*************************##

pygame.display.set_icon(icon)
podział_okienka = range(0, OKNO_SZER - kosmita.get_width(), kosmita.get_width())
podział_okienka_bonus = range(OKNO_WYS//2, OKNO_SZER - bonus_klucz.get_width(), bonus_klucz.get_width())
pygame.display.set_caption("STUDENT INVADERS")
zegarek = pygame.time.Clock()

# LISTY
enemyList = list[Przeciwnik]()          # lista przeciwników
pociskList = list[Pocisk]()             # lista pocisków
wybuchList = list[Wybuch]()             # lista wybuchów
bonusList = list[Bonusy]()              # lista bonusów

czas_od_pocisku = 0
czas_od_rakiety = 0
czas_płynny_ruch_przeciwnika = 0
czas_ruch_bonusu = 0
czas_intro = 0
czas_goodman = 0
czas_niezniszczalności_bonus = 0
czas_przegrzanie_bonus = 0

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
DŹWIĘK_ON = Przycisk(OKNO_SZER - but_dzwiek_enabled.get_width() - 10, OKNO_WYS - but_dzwiek_enabled.get_height() - 10, but_dzwiek_enabled, but_dzwiek_enabled_hover)
DŹWIĘK_OFF = Przycisk(OKNO_SZER - but_dzwiek_disabled.get_width() - 10, OKNO_WYS - but_dzwiek_disabled.get_height() - 10, but_dzwiek_disabled, but_dzwiek_disabled_hover)
DŹWIĘKI=[DŹWIĘK_ON, DŹWIĘK_OFF]
DŹWIĘK = DŹWIĘK_ON
dźwięk = True
puszczono = True

MENU_PONOWNIE = Przycisk(0, 0, but_dzwiek_enabled, but_dzwiek_enabled_hover)
WYJDŹ_PONOWNIE = Przycisk(0, 400, but_wyjscie, but_wyjscie_hover)
GRAJ_PONOWNIE = Przycisk(400, 0, but_start, but_start_hover)

# SCENY
SCENA_INTRO = Scena("INTRO")
SCENA_MENU = Scena("MENU", [START, INSTRUKCJA, EXIT])
SCENA_GRA = Scena("GRA")
SCENA_INSTRUKCJE = Scena("INSTRUKCJE", [INSTRUKCJA])
SCENA_PAUZA = Scena("PAUZA", [WZNÓW, WYJDŹ])
SCENA_ŚMIERĆ = Scena("ŚMIERĆ", [MENU_PONOWNIE, WYJDŹ_PONOWNIE, GRAJ_PONOWNIE])

Scena.obecna_scena = SCENA_INTRO

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

    if scena == SCENA_INTRO:
        okienko.blit(bg_intro1, (0, 0))
        czas_intro += 1
        if czas_intro > 399:
            pygame.mixer.music.stop()
            pygame.mixer.music.load(mus_menu)
            pygame.mixer.music.play()
            Scena.obecna_scena = SCENA_MENU
            czas_intro = 0
        if czas_intro > 370:
            okienko.blit(bg_intro2, (0, 0))
            if puszczono:
                pygame.mixer.music.play()
                puszczono = False
        black.set_alpha(255 * (1 - abs(math.sin(czas_intro/117))))
        print(black.get_alpha())
        okienko.blit(black, (0, 0))
    elif scena == SCENA_MENU:
        TŁO1.rysujTło()
        TŁO2.rysujTło()

        okienko.blit(logo, (OKNO_SZER//2 - logo.get_width()//2, 10))
        scena.rysujPrzyciski()
        DŹWIĘK.rysujPrzycisk()

        if czas_intro < 120:
            czas_intro += 1
            black.set_alpha(255 * (1 - 5*abs(math.sin(czas_intro/116))))
            okienko.blit(black, (0, 0))

        if keys[pygame.K_LSHIFT]:
            Scena.obecna_scena = SCENA_GRA
        if keys[pygame.K_ESCAPE]:
            graj = False
        if keys[pygame.K_r]:
            punkty.resetRekordu()

        for zdarzenie in zdarzenia:
            if zdarzenie.type == pygame.MOUSEBUTTONUP:
                if START.czyMyszka():
                    if dźwięk:
                        pygame.mixer.music.load(mus_gra)
                        pygame.mixer.music.play()
                    czas_intro = 0
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
        TŁO1.rysujTło()
        TŁO2.rysujTło()
        scena.rysujPrzyciski()
        for zdarzenie in zdarzenia:
            if zdarzenie.type == pygame.KEYDOWN:
                zdarzenie.key == pygame.K_ESCAPE
                Scena.obecna_scena = SCENA_MENU
            if zdarzenie.type == pygame.MOUSEBUTTONUP and INSTRUKCJA.czyMyszka():
                Scena.obecna_scena = SCENA_MENU
    elif scena == SCENA_GRA:
        Scena.fazaGry()
        if punkty.wynik < 30000:
            if punkty.wynik in (5000, 5500):
                Scena.faza = FAZA1
            if punkty.wynik in (10000, 10500):
                Scena.faza = FAZA2
            if punkty.wynik in (15000, 15500):
                Scena.faza = FAZA3
            if punkty.wynik in (20000, 20500):
                Scena.faza = FAZA4
            if punkty.wynik in (25000, 25500):
                Scena.faza = FAZA5
        else:
            if punkty.wynik % 10000 in range(0, 399):
                random_faza = random.choice([FAZA4, FAZA5, FAZA6])
                Scena.faza = random_faza
        for zdarzenie in zdarzenia:
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
        TŁO1.rysujTło()
        TŁO2.rysujTło()
        czas_od_pocisku += dt
        czas_od_rakiety += dt
        czas_ruch_bonusu += dt/20
        czas_płynny_ruch_przeciwnika += dt/17
        #print(czas_płynny_ruch_przeciwnika)

        if gracz.wystrzelPocisk():
            czas_od_pocisku = 0
        
        if czas_od_pocisku > 2000:
            czas_od_pocisku = Gracz.cooldown_strzalu

        if gracz.wystrzelRakiete():
            czas_od_rakiety = 0
        
        if czas_od_rakiety > 5000:
            czas_od_rakiety = Gracz.cooldown_rakiety
        
        enemy_do_usunięcia = []
        strzelający_przeciwnik = random.randint(0, 300)
        for enemy in enemyList:
            if enemy.id == strzelający_przeciwnik:
                enemy.wystrzelPocisk()
            if kolizja(enemy, gracz):
                enemy_do_usunięcia.append(enemy)
                if Gracz.niezniszczalność_bonus is False:
                    punkty.dodawaniePunktów(-100)
                    zdrowie.zmianaHp(-20)
            enemy.ruchPrzeciwnika()
            enemy.rysujPrzeciwnika()
        
        czas = pygame.time.get_ticks()
        czy_rakieta_wybucha = False
        
        if Przeciwnik.stworzonych_przeciwnikow == cykl_pojawienia_pwr_up:
            bonus = Bonusy()
            bonus.ustawBonus()
            bonusList.append(bonus)
            cykl_pojawienia_pwr_up += random.randint(17, 27)

        for bonus in bonusList:
            bonus.ruchBonusu()
            bonus.rysujBonus()
        
        bonusy_do_usunięcia = []
        
        pociski_do_usunięcia = []
        for pocisk in pociskList:
            pocisk.ruchPocisku()
            pocisk.rysujPocisk()
            if pocisk.kto_strzelił == "gracz" or pocisk.kto_strzelił == "rakieta":
                for enemy in enemyList:
                    if pocisk.czyKolizja(enemy):
                        pociski_do_usunięcia.append(pocisk)
                        if pocisk.kto_strzelił == "gracz":
                            enemy.hp += -1
                        if pocisk.kto_strzelił == "rakieta":
                            czy_rakieta_wybucha = True
                            wybuch = Wybuch(pocisk.x, pocisk.y)
                            wybuch.CzyWybuch(pocisk.x, pocisk.y, czas, True)
                            wybuchList.append(wybuch)
                            (x0, y0) = (pocisk.x + pocisk_gracza1.get_width()//2, pocisk.y + pocisk_gracza1.get_height()//2)
                            if dźwięk:
                                sfx_eksplozja_rakiety.play()
            if pocisk.kto_strzelił in ("kosmita", "krążownik"):
                if pocisk.czyKolizja(gracz) and Gracz.niezniszczalność_bonus is False:
                    pociski_do_usunięcia.append(pocisk)
                    punkty.dodawaniePunktów(-100)
                    strata = -20 if pocisk.kto_strzelił == "kosmita" else -40
                    zdrowie.zmianaHp(strata)
                    #^^^^^^^^^^^^^^^^^^
                    #tutaj zrobimy stratę hp zależną od typu przeciwnika (to jak zrobimy klasę typów przeciwnika albo wczytywanie pliku)
            for bonus in bonusList:
                if pocisk.czyKolizja(bonus) and (pocisk.kto_strzelił == "gracz" or pocisk.kto_strzelił == "rakieta") and bonus.nietrafiony:
                    if bonus.pwr_up == 1: #ODPORNOŚĆ
                        Gracz.niezniszczalność_bonus = True
                        czas_niezniszczalności_bonus = czas
                        sfx_tarcza_on.play()
                    elif bonus.pwr_up == 2: #RAKIETA
                        Gracz.ilość_rakiet += 1
                        sfx_rakieta_bonus.play()
                    elif bonus.pwr_up == 3: #PRZEGRZANIE
                        Gracz.przegrzanie_bonus = True
                        gracz.aktualne_przegrzanie = gracz.maks_przegrzanie
                        czas_przegrzanie_bonus = czas
                        sfx_tarcza_on.play()
                    elif bonus.pwr_up == 4: #HP
                        zdrowie.zmianaHp(20)
                        sfx_leczenie.play()
                    bonus.nietrafiony = False
                    bonusy_do_usunięcia.append(bonus)
        
        for bonus in bonusy_do_usunięcia:
            try:
                bonusList.remove(bonus)
            except:
                print("BŁĄD USUNIĘCIA BONUSU")
        
        if czy_rakieta_wybucha:
            for enemy in enemyList:
                if ((enemy.x + enemy.obraz.get_width()//2) - x0)**2 + ((enemy.y + enemy.obraz.get_height()//2) - y0)**2 <= (eksplozja.get_height())**2:
                    enemy.hp += -14
                if enemy.hp <= 0:
                    punkty.dodawaniePunktów(200)
                    enemy_do_usunięcia.append(enemy)
        else:
            for enemy in enemyList:
                if enemy.hp <= 0:
                    punkty.dodawaniePunktów(200)
                    enemy_do_usunięcia.append(enemy)
        
        for enemy in enemy_do_usunięcia:
            wybuch = Wybuch(enemy.x, enemy.y)
            wybuch.CzyWybuch(enemy.x, enemy.y, czas, False)
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
        gracz.przegrzanie()
        punkty.rysujScoreboard()
        zdrowie.rysujPasek()
        
        for wybuch in wybuchList:
            wybuch.IleOdWybuchu(czas)
        
        if czas - czas_niezniszczalności_bonus > 10000 and Gracz.niezniszczalność_bonus:
            Gracz.niezniszczalność_bonus = False
            sfx_tarcza_off.play()
        
        if czas - czas_przegrzanie_bonus > 10000 and Gracz.przegrzanie_bonus:
            Gracz.przegrzanie_bonus = False
            sfx_tarcza_off.play()
        
        if zdrowie.hp <= 0:
            
            if punkty.rekord < punkty.wynik:
                with open(os.path.join("pliki","rekord.txt"), 'w') as rekord:
                    rekord.write(str(punkty.wynik))
                    punkty.rekord = punkty.wynik
            
            Scena.obecna_scena = SCENA_ŚMIERĆ
            pygame.mixer.music.load(mus_gameover)
            pygame.mixer.music.play()

            punkty.wynik = 0
            zdrowie.hp = zdrowie.max_hp
            #gracz = Gracz()
            Gracz.ilość_rakiet = pakiet_rakiet
            gracz.aktualne_przegrzanie = gracz.maks_przegrzanie
            gracz.ustawGracza((OKNO_SZER - gracz.szer)//2, OKNO_WYS - gracz.wys - 50)

            Przeciwnik.stworzonych_przeciwnikow = 0
            
            cykl_pojawienia_pwr_up = 15

            enemyList.clear()
            pociskList.clear()
            bonusList.clear()
            wybuchList.clear()  #Czyścimy listy, aby przeciwnicy, wybuchy oraz pociski z poprzedniej rundy nie pojawiali się w nowej

        if czas_intro < 170:
            czas_intro += 1
            black.set_alpha(255 * (1 - 2*abs(math.sin(czas_intro/116))))
            okienko.blit(black, (0, 0))
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

        czas_intro = 0

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
                    pygame.mixer.music.load(mus_menu)
                    pygame.mixer.music.play()
                elif GRAJ_PONOWNIE.czyMyszka():
                    Scena.obecna_scena = SCENA_GRA
                    pygame.mixer.music.stop()
                    pygame.mixer.music.load(mus_gra)
                    pygame.mixer.music.play()

pygame.quit()