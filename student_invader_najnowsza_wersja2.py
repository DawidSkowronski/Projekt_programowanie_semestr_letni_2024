import pygame
import random
import os
import math
import unittest

pygame.init()

##
##      GLOBALNE
##

# ILOŚĆ RAKIET
pakiet_rakiet = 15

# GŁÓWNE
OKNO_SZER = 720
OKNO_WYS = 960
font = pygame.font.Font(None,34)
fps = 60
okienko = pygame.display.set_mode((OKNO_SZER, OKNO_WYS), 0, 32)

black = pygame.Surface((OKNO_SZER, OKNO_WYS))
black.set_alpha(255)
black.fill((0, 0, 0))

# SPRAJTY
statek = pygame.image.load(os.path.join("images","statek.png")).convert_alpha()
statek_lewo = pygame.image.load(os.path.join("images","statek_lewo.png")).convert_alpha()
statek_prawo = pygame.image.load(os.path.join("images","statek_prawo.png")).convert_alpha()

icon = pygame.image.load(os.path.join("images","ic_statek.png")).convert_alpha()
bariera = pygame.image.load(os.path.join("images","bariera.png")).convert_alpha()

kosmita = pygame.image.load(os.path.join("images","kosmita.png")).convert_alpha()
kosmita_1 = pygame.image.load(os.path.join("images","kosmita_dmg1.png")).convert_alpha()
kosmita_2 = pygame.image.load(os.path.join("images","kosmita_dmg2.png")).convert_alpha()

kamikaze = pygame.image.load(os.path.join("images","kamikaze.png")).convert_alpha()
kamikaze_szarza = pygame.image.load(os.path.join("images","kamikaze_szarża.png"))

krazownik = pygame.image.load(os.path.join("images","przeciwnik2.png")).convert_alpha()
krazownik_1 = pygame.image.load(os.path.join("images","przeciwnik2_dmg1.png")).convert_alpha()
krazownik_2 = pygame.image.load(os.path.join("images","przeciwnik2_dmg2.png")).convert_alpha()

szturmowiec = pygame.image.load(os.path.join("images","przeciwnik3.png")).convert_alpha()
szturmowiec_1 = pygame.image.load(os.path.join("images","przeciwnik3_dmg1.png")).convert_alpha()
szturmowiec_2 = pygame.image.load(os.path.join("images","przeciwnik3_dmg2.png")).convert_alpha()

pocisk_gracza = pygame.image.load(os.path.join("images","pocisk_gracza.png")).convert_alpha()
pocisk_gracza1 = pygame.image.load(os.path.join("images","rakieta.png")).convert_alpha()
pocisk_kosmity = pygame.image.load(os.path.join("images","pocisk_wróg1.png")).convert_alpha()
pocisk_krazownika = pygame.image.load(os.path.join("images","pocisk2.png")).convert_alpha()
pocisk_szturmowca = pygame.image.load(os.path.join("images","laser_czerwony.png")).convert_alpha()

eksplozja = pygame.image.load(os.path.join("images","eksplozja1.png")).convert_alpha()
eksplozja_1 = pygame.image.load(os.path.join("images","eksplozja2.png")).convert_alpha()
eksplozja_2 = pygame.image.load(os.path.join("images","eksplozja3.png")).convert_alpha()

bonus_klucz = pygame.image.load(os.path.join("images","bonus_klucz.png")).convert_alpha()
bonus_rakieta = pygame.image.load(os.path.join("images","rakieta_bonus.png")).convert_alpha()
bonus_przegrzanie = pygame.image.load(os.path.join("images","bonus_przegrzanie.png")).convert_alpha()
bonus_bariera = pygame.image.load(os.path.join("images","bonus_bariera.png")).convert_alpha()
klucz = pygame.image.load(os.path.join("images","klucz_naprawczy.png")).convert_alpha()
rakieta_icon = pygame.transform.scale(bonus_rakieta,(100,80))

but_start = pygame.image.load(os.path.join("images","START.png")).convert_alpha()
but_start_hover = pygame.image.load(os.path.join("images","START_aktyw.png")).convert_alpha()
but_wyjscie = pygame.image.load(os.path.join("images","EXIT.png")).convert_alpha()
but_wyjscie_hover = pygame.image.load(os.path.join("images","EXIT_aktyw.png")).convert_alpha()
but_kontynuuj = pygame.image.load(os.path.join("images","kontynuuj.jpg")).convert_alpha()
but_kontynuuj_hover = pygame.image.load(os.path.join("images","kontynuuj_aktyw.jpg")).convert_alpha()
but_powrot = pygame.image.load(os.path.join("images","powrót.jpg")).convert_alpha()
but_powrot_hover = pygame.image.load(os.path.join("images","powrót_aktyw.jpg")).convert_alpha()

but_dzwiek_enabled = pygame.image.load(os.path.join("images","włączony.jpg")).convert_alpha()
but_dzwiek_enabled_hover = pygame.image.load(os.path.join("images","włączony_aktyw.jpg")).convert_alpha()
but_dzwiek_disabled = pygame.image.load(os.path.join("images","wyłączony.jpg")).convert_alpha()
but_dzwiek_disabled_hover = pygame.image.load(os.path.join("images","wyłączony_aktyw.jpg")).convert_alpha()

but_instrukcje = pygame.image.load(os.path.join("images","instrukcja.jpg")).convert_alpha()
but_instrukcje_hover = pygame.image.load(os.path.join("images","instrukcja_aktyw.jpg")).convert_alpha()

but_inkwizycja = pygame.image.load(os.path.join("images","hiszpańska_inkwizycja.png")).convert_alpha()

bg_instrukcje = pygame.image.load(os.path.join("images","jak.jpg")).convert_alpha()
bg_kosmos = pygame.image.load(os.path.join("images","kosmos.png")).convert_alpha()
bg_gameover = pygame.image.load(os.path.join("images","game_over.png")).convert_alpha()
bg_pauza = pygame.image.load(os.path.join("images","pauza.png")).convert_alpha()   #NARAZIE NIEUŻYWANE

bg_intro1 = pygame.image.load(os.path.join("images","intro1.png")).convert()
bg_intro2 = pygame.image.load(os.path.join("images","saul_goodman.png")).convert_alpha()

logo = pygame.image.load(os.path.join("images","logo.png")).convert_alpha()

# DŹWIĘKI
pygame.mixer.init()

# SFX
sfx_pocisk = pygame.mixer.Sound(os.path.join("sounds","laser.mp3"))
sfx_pocisk_wroga = pygame.mixer.Sound(os.path.join("sounds","plasma.mp3"))
sfx_eksplozja = pygame.mixer.Sound(os.path.join("sounds", "eksplozja.ogg"))
sfx_rakieta = pygame.mixer.Sound(os.path.join("sounds", "tsss.mp3"))
sfx_eksplozja_rakiety = pygame.mixer.Sound(os.path.join("sounds", "eksplozja_rakieta.mp3"))
sfx_alarm = pygame.mixer.Sound(os.path.join("sounds","alarm.wav"))
sfx_tsss = pygame.mixer.Sound(os.path.join("sounds","tsss.mp3"))
sfx_leczenie = pygame.mixer.Sound(os.path.join("sounds","leczenie.mp3"))
sfx_tarcza_on = pygame.mixer.Sound(os.path.join("sounds","tarcza_on.wav"))
sfx_tarcza_off = pygame.mixer.Sound(os.path.join("sounds","tarcza_off.wav"))
sfx_rakieta_bonus = pygame.mixer.Sound(os.path.join("sounds","rakieta_bonus.wav"))
sfx_inkwizycja = pygame.mixer.Sound(os.path.join("sounds","hiszpańska_inkwizycja.mp3"))

sfx_pocisk.set_volume(.1)
sfx_eksplozja.set_volume(.35)
sfx_rakieta.set_volume(.15)  # zmienić
sfx_eksplozja_rakiety.set_volume(.1)
sfx_alarm.set_volume(.1)
sfx_tsss.set_volume(.2)
sfx_leczenie.set_volume(.5)
sfx_tarcza_on.set_volume(.5)
sfx_tarcza_off.set_volume(.5)
sfx_rakieta_bonus.set_volume(.5)
sfx_inkwizycja.set_volume(.5)

# MUZYKA
mus_gameover = os.path.join("music","game_over.mp3")
mus_gra = os.path.join("music","muza.mp3")
mus_menu = os.path.join("music","menu.mp3")
mus_goodman = os.path.join("music","saul_goodman.mp3")

pygame.mixer.music.load(mus_goodman)
pygame.mixer.music.set_volume(.25)

##
##      KLASY
##

# KLASA TŁA
class Tło:
    """Klasa tworząca ruchome tło."""
    def __init__(self, y):
        self.y = y
        self.img = bg_kosmos

    def ruchTła(self):
        """Porusza tłem."""
        self.y += .33
        if self.y >= OKNO_WYS:
            self.y = -OKNO_WYS

    def rysujTło(self):
        """Rysuje tło."""
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
    """Klasa tworząca animacje wybuchów."""   # DO POPRAWY WYBUCHY
    def __init__(self, x, y):
        self.img0 = eksplozja
        self.img1 = eksplozja_1
        self.img2 = eksplozja_2
        self.x = x
        self.y = y
        self.miejsce_wybuchu_kosmita = (self.x + kosmita.get_width()//2 - eksplozja.get_width()//2, self.y + kosmita.get_height()//2 - eksplozja.get_height()//2)
        self.miejsce_wybuchu_krazownik = (self.x + krazownik.get_width()//2 - (eksplozja.get_width()//2)*1.3, self.y + krazownik.get_height()//2 - (eksplozja.get_height()//2)*1.3)
        self.miejsce_wybuchu_rakieta = (self.x + pocisk_gracza1.get_width()//2 - (eksplozja.get_width()//2)*2, self.y + pocisk_gracza1.get_height()//2 - (eksplozja.get_height()//2)*2)
    
    def CzyWybuch(self, x, y, ticks_wybuchu, czy_krazownik, czy_rakieta):
        """Ustawia koordynaty wybuchu i sprawdza, czy jest to wybuch rakiety."""
        self.x = x
        self.y = y
        self.czas = ticks_wybuchu
        self.czy_krazownik = czy_krazownik
        self.czy_rakieta = czy_rakieta

    
    def IleOdWybuchu(self, czas_od_wybuchu):
        """Wykonuje odpowiednią animację dla danego typu wybuchu."""
        if self.czy_rakieta:
            if czas_od_wybuchu - self.czas <= 225:
                okienko.blit(pygame.transform.smoothscale(self.img0, [self.img0.get_width()*2, self.img0.get_height()*2]), self.miejsce_wybuchu_rakieta)
            else:
                wybuchList.remove(self)
        else:
            if czas_od_wybuchu - self.czas <= 225:
                if czas_od_wybuchu - self.czas <= 150:
                    if czas_od_wybuchu - self.czas <= 75:
                        if self.czy_krazownik:
                            okienko.blit(pygame.transform.smoothscale(self.img0, [self.img0.get_width()*1.3, self.img0.get_height()*1.3]), self.miejsce_wybuchu_krazownik)
                        else:
                            okienko.blit(self.img0, self.miejsce_wybuchu_kosmita)
                        return
                    if self.czy_krazownik:
                        okienko.blit(pygame.transform.smoothscale(self.img1, [self.img0.get_width()*1.3, self.img0.get_height()*1.3]), self.miejsce_wybuchu_krazownik)
                    else:
                        okienko.blit(self.img1, self.miejsce_wybuchu_kosmita)
                    return
                if self.czy_krazownik:
                    okienko.blit(pygame.transform.smoothscale(self.img2, [self.img0.get_width()*1.3, self.img0.get_height()*1.3]), self.miejsce_wybuchu_krazownik)
                else:
                    okienko.blit(self.img2, self.miejsce_wybuchu_kosmita)
                return
            else:
                wybuchList.remove(self)

# KLASA PRZYCISK
class Przycisk():
    """Klasa zawierająca funkcjonalność przycisków"""
    def __init__(self, but_obrazek, but_obrazek_hover:pygame.Surface = None):
        
        self.mask = but_obrazek.get_rect()

        self.obrazek = but_obrazek
        self.obrazek_hover = but_obrazek_hover

    def czyMyszka(self):
        """Sprawdza, czy myszka jest "na powierzchni" przycisku, zwraca bool."""
        myszka = pygame.mouse.get_pos()
        if self.mask.collidepoint(myszka):
            return True
        return False
    
    def ustawPrzycisk(self, x : float, y : float):
        """Ustawia przycisk na zadane koordynaty."""
        self.mask.x = x
        self.mask.y = y
    
    def rysujPrzycisk(self):
        """Wyświetla przycisk w okienku."""
        if self.czyMyszka():
            okienko.blit(self.obrazek_hover, (self.mask.x, self.mask.y))
        else:
            okienko.blit(self.obrazek, (self.mask.x, self.mask.y))

# KLASA BONUSY
class Bonusy(Byt):
    """Klasa tworząca bonusy."""
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
        if zdrowie.hp >= zdrowie.max_hp:
            self.pwr_up = random.choice([i for i in range(1, 4) if i != Bonusy.poprzedni_pwr_up])
            Bonusy.poprzedni_pwr_up = self.pwr_up
        elif zdrowie.hp >= zdrowie.max_hp * 0.3:
            self.pwr_up = random.choice([i for i in range(1, 5) if i != Bonusy.poprzedni_pwr_up])
            Bonusy.poprzedni_pwr_up = self.pwr_up
        else:
            self.pwr_up = 4
            Bonusy.poprzedni_pwr_up = 4     #zamiast self.pwr_up, bo w tej pętli jest zawsze równe 4
        if self.pwr_up == 1:
            self.obraz = bonus_bariera
        elif self.pwr_up == 2:
            self.obraz = bonus_rakieta
        elif self.pwr_up == 3:
            self.obraz = bonus_przegrzanie
        elif self.pwr_up == 4:
            self.obraz = bonus_klucz
        mask = pygame.mask.from_surface(self.obraz)
        Byt.__init__(self, x, y, mask, self.obraz)
        self.szer = self.obrazek.get_width()
        self.wys = self.obrazek.get_width()

    def rysujBonus(self):
        """Rysuje bonus i usuwa go, jeżeli znajdzie się za granicą mapy."""
        okienko.blit(self.obraz,(self.x,self.y))
        if self.z_prawej_do_lewej and self.x <= 0 - self.obraz.get_width() - 5:
            bonusList.remove(self)
            del self
        elif self.x >= OKNO_SZER + self.obraz.get_width() + 5:
            bonusList.remove(self)
            del self

    def ruchBonusu(self):
        """Określa ruch bonusu po sinusoidzie."""
        self.dx = self.speed
        if self.z_prawej_do_lewej:
            self.x -= self.dx
        else:
            self.x += self.dx
        self.dy = (self.speed*math.sin(czas_ruch_bonusu/10))
        self.y -= self.dy
    
    def ustawBonus(self):
        """Ustawia bonus odpwiednio z lewej lub prawej strony i na losowej wysokości."""
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
        maska_bariery = pygame.mask.from_surface(bariera)
        self.bariera = Byt(1200, 1200, maska_bariery, bariera)
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
        okienko.blit(self.obrazek, (self.x,self.y))
        if Gracz.niezniszczalność_bonus:
            self.bariera.x = self.x - 38
            self.bariera.y = self.y - 33
            okienko.blit(self.bariera.obrazek, (self.bariera.x, self.bariera.y))
        else:
            self.bariera.x = 1200
            self.bariera.y = 1200
        

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
            self.obrazek = statek_lewo

        elif keys[pygame.K_d]:
            self.dx = self.predkosc
            self.obrazek = statek_prawo
        else:
            self.dx = 0
            self.obrazek = statek
        
        # GRACZ NIE MOŻE WYJŚĆ ZA OKIENKO
        # NIE MOŻE WYJŚĆ Z LEWEJ ANI Z PRAWEJ
        if self.x <= 10:
            if self.dx < 0:
                self.x = 10
                self.obrazek = statek
            else:
                self.x += self.dx
        elif self.x >= OKNO_SZER - self.szer-25:
            if self.dx > 0:
                self.x = OKNO_SZER - self.szer-25
                self.obrazek = statek
            else:
                self.x += self.dx
        else:
            self.x += self.dx

        # NIE MOŻE WYJŚĆ Z GÓRY ANI Z DOŁU
        if self.y <= OKNO_WYS*3//5:
            if self.dy < 0:
                self.y = OKNO_WYS*3//5
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
                sfx_pocisk.play()
                return True
        return False
    
    def wystrzelRakiete(self):
        """Pozwala graczowi wystrzelić rakietę, zwraca prawdę jeśli ją wystrzeli."""
        if czas_od_rakiety > Gracz.cooldown_rakiety:
            if keys[pygame.K_LSHIFT] and Gracz.ilość_rakiet > 0:
                pociskList.append(Pocisk(self.x + self.szer//2, self.y + self.wys//2, 15, "rakieta"))
                Gracz.ilość_rakiet += -1
                sfx_rakieta.play()
                return True
        return False
    
    def przegrzanie(self):
        """Nie pozwala graczowi strzelać, jeżeli 'przegrzał broń'."""
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

        pygame.draw.rect(okienko, "orangered", (self.x +125, self.y +7, 13, 120))
        pygame.draw.rect(okienko, "gray", (self.x +125, self.y +7 , 13, 120 * self.poziom_przegrzania))

        if Gracz.przegrzanie_bonus:
            sfx_alarm.stop()
            pygame.draw.rect(okienko, "gold", (self.x +125, self.y +7, 13, 120))
# KLASA PUNKTY GRACZA
class Scoreboard:
    """Klasa tworząca wynik gracza."""
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

    def dodawaniePunktów(self,wartość):
        """Dodaje punkty do wyniku."""
        self.wynik += wartość
    
    def rysujScoreboard(self):
        """Pojawia na ekranie wynik razem z rekordem."""
        if scena == SCENA_GRA:
            okienko.blit(font.render("Wynik: " + str(self.wynik),True,(255,255,255)),(0,0))
            if self.rekord < self.wynik:
                okienko.blit(font.render("NOWY REKORD: " + str(self.wynik),True,(0, 200, 0)),(0,20))
            else:
                okienko.blit(font.render("Rekord: " + str(self.rekord),True,(255, 255, 255)),(0,20))
            okienko.blit(rakieta_icon, (-30,40))
            okienko.blit(font.render("x " + str(Gracz.ilość_rakiet),True,(255,255,255)),(40,60))
        elif scena == SCENA_ŚMIERĆ:
            okienko.blit(font.render("Wynik: " + str(self.wynik),True,(255,255,255)),(280,170))
            if self.rekord < self.wynik:
                okienko.blit(font.render("NOWY REKORD: " + str(self.wynik),True,(0, 200, 0)),(280,193))
            else:
                okienko.blit(font.render("Rekord: " + str(self.rekord),True,(255, 255, 255)),(280,193))

    
    def resetRekordu(self):
        """Zeruje najlepszy wynik gracza."""
        with open(os.path.join("pliki","rekord.txt"), 'w') as rekord:
            rekord.write(str(0))
            self.rekord = 0
        
# KLASA ŻYCIE GRACZA
class PasekZdrowia:
    """Klasa tworząca pasek zdrowia."""
    def __init__(self, max_hp):
        self.hp = max_hp
        self.max_hp = max_hp

    def rysujPasek(self):
        """Pojawia pasek zdrowia na ekranie."""
        poziom_hp = self.hp / self.max_hp
        pygame.draw.rect(okienko, "red", (10, OKNO_WYS - 40, 260, 25))
        pygame.draw.rect(okienko, "green", (10, OKNO_WYS - 40, 260 * poziom_hp, 25))
        okienko.blit(font.render("HP",True,'green'),(140,OKNO_WYS - font.get_height() - 40))
        okienko.blit(klucz, (247,OKNO_WYS-50))
        
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
    """Klasa tworząca instancje przeciwników."""
    stworzonych_przeciwnikow = 0
    pokonanych_przeciwnikow = 0

    dx = 0
    dy = 0

    def __init__(self, x:float = 0, y:float = 0, typ:str = "kosmita", czas_powstania:float = 0):
        """Przeciwnik otrzymuje ogólne zmienne oraz konkretne, zależące od jego rodzaju."""
        # ID PRZECIWNIKA
        if Przeciwnik.stworzonych_przeciwnikow > 299:
            Przeciwnik.stworzonych_przeciwnikow = 0
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
        elif self.tag == "szturmowiec":
            self.obraz = szturmowiec
            self.obraz_1 = szturmowiec_1
            self.obraz_2 = szturmowiec_2
            self.speed = 2
            self.pocisk_speed = 10
            self.hp = 6

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
            enemy_do_usunięcia.append(self)

    def ruchPrzeciwnika(self):
        """Zmienia koordynaty przeciwnika."""
        if self.tag == "kamikaze":
            czas_zachowania = czas - self.czas_powstania
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
        elif self.tag == "szturmowiec":
            self.dx = self.speed *math.sin(2*czas_płynny_ruch_przeciwnika/fps + self.ruch_offset%fps)
            self.dy = self.speed

        self.y += self.dy
        self.x += self.dx

    def ustawPrzeciwnika(self, x = 0, y = 0):
        """Ustawia przeciwnika na konkretne koordynaty."""
        self.x = x
        self.y = y

    def wystrzelPocisk(self):
        """Pozwala przeciwnikowi wystrzelić pocisk"""
        if self.tag == "kamikaze":
            return False
        if self.tag == "szturmowiec":
            pociskList.append(Pocisk(self.x + self.szer//2 - 30, self.y + self.wys//2, self.pocisk_speed, self.tag))
            pociskList.append(Pocisk(self.x + self.szer//2 + 30, self.y + self.wys//2, self.pocisk_speed, self.tag))
        else:
            pociskList.append(Pocisk(self.x + self.szer//2, self.y + self.wys//2, self.pocisk_speed, self.tag))
            return True
    
    def pozaOknem(self):    # usuwamy przeciwników poza oknem, żeby nie zostawiać zbędnych obiektów
        """Sprawdza, czy przeciwnik znajduje się w obszarze okna, jeśli nie -  usuwa go."""
        if self.y > OKNO_WYS + 5:
            return True
        return False

# KLASA POCISK
class Pocisk(Byt):
    """Klasa tworząca pociski gracza i przeciwników."""
    def __init__(self, x:float, y:float, predkosc:float, kto_strzelił:str):
        if kto_strzelił == "gracz":
            obrazek = pocisk_gracza
        elif kto_strzelił == "kosmita":
            obrazek = pocisk_kosmity
        elif kto_strzelił == "krążownik":
            obrazek = pocisk_krazownika
        elif kto_strzelił == "rakieta":
            obrazek = pocisk_gracza1
        elif kto_strzelił == "szturmowiec":
            obrazek = pocisk_szturmowca

        mask = pygame.mask.from_surface(obrazek)  # mask tworzy dokładną siatkę pikseli wgranego obrazu

        Byt.__init__(self, x - obrazek.get_width()//2, y - obrazek.get_height()//2, mask, obrazek)
        self.predkosc = predkosc
        self.kto_strzelił = kto_strzelił
        self.czas_płynny_ruch_rakiety = 0
    
    def rysujPocisk(self):
        """Rysuje pocisk."""
        okienko.blit(self.obrazek, (self.x, self.y))  # rysuje obraz na wyświetlanym oknie
        
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
    """Klasa tworząca fazy gry."""
    wszystkie_fazy = 0

    def __init__(self, przeciwnicy:list[str], czestotliwosci:list[tuple], cykl_pojawiania:float):
        self.przeciwnicy = przeciwnicy
        self.czestotliwosci = czestotliwosci
        self.pojaw_przeciwnika = pygame.USEREVENT + 100 + Faza.wszystkie_fazy
        pygame.time.set_timer(self.pojaw_przeciwnika, cykl_pojawiania)

        Faza.wszystkie_fazy += 1

    def pojawPrzeciwnika(self):
        """LOL NIE WIEM"""
        for zdarzenie in zdarzenia:
            if zdarzenie.type == self.pojaw_przeciwnika:
                rint = random.randint(1,100)
                i = 0
                typ_wybrany = self.przeciwnicy[0]
                for typ in self.przeciwnicy:
                    if rint in range(self.czestotliwosci[i][0], self.czestotliwosci[i][1]):
                        typ_wybrany = typ
                    i += 1
                if typ_wybrany == "szturmowiec":
                    gdzie_przeciwnik = random.choice(range(200, OKNO_SZER - 200, kosmita.get_width()))
                else:
                    gdzie_przeciwnik = random.choice(podział_okienka)
                przeciwnik = Przeciwnik(typ=typ_wybrany, czas_powstania=czas)
                przeciwnik.ustawPrzeciwnika(gdzie_przeciwnik, - przeciwnik.wys - 2)
                enemyList.append(przeciwnik)

FAZA0 = Faza(["kosmita", "szturmowiec"], [(1, 80), (81, 100)], 1500)
FAZA1 = Faza(["kamikaze"], [(1, 100)], 1000)
FAZA2 = Faza(["kosmita", "kamikaze"], [(1,80), (81, 100)], 1250)
FAZA3 = Faza(["krążownik", "kamikaze"], [(1, 60), (61, 100)], 1000)
FAZA4 = Faza(["kosmita"], [(1, 100)], 500)
FAZA5 = Faza(["kosmita", "krążownik", "kamikaze"], [(1,50),(51,75),(76,100)], 1000)
FAZA6 = Faza(["kosmita", "kamikaze"], [(1, 10), (11, 90)], 500)

# KLASA SCENA
class Scena:
    """Klasa tworząca sceny gry."""
    obecna_scena = None
    faza:Faza = FAZA0

    def __init__(self, tag:str, przyciski:list[Przycisk] = []):
        self.tag = tag
        self.przyciski = przyciski

    def ustawPrzyciski(self):
        """Ustawia przyciski w zależności od sceny."""
        if self.tag == "MENU":
            self.przyciski[0].ustawPrzycisk(OKNO_SZER//2 - self.przyciski[0].obrazek.get_width()//2, OKNO_WYS//2 - self.przyciski[0].obrazek.get_height() - 50)
            self.przyciski[1].ustawPrzycisk(OKNO_SZER//2 - self.przyciski[1].obrazek.get_width()//2, OKNO_WYS//2 + self.przyciski[1].obrazek.get_height() - 50)
            self.przyciski[2].ustawPrzycisk(OKNO_SZER//2 - self.przyciski[2].obrazek.get_width()//2, OKNO_WYS//2 + 2* self.przyciski[2].obrazek.get_height() - 20)
        elif self.tag == "INSTRUKCJE":
            self.przyciski[0].ustawPrzycisk(20, OKNO_WYS - self.przyciski[0].obrazek.get_height() - 20)
        elif self.tag == "PAUZA":
            self.przyciski[0].ustawPrzycisk(OKNO_SZER//2 - self.przyciski[0].obrazek.get_width()//2, OKNO_WYS//2 - self.przyciski[0].obrazek.get_height() - 50)
            self.przyciski[1].ustawPrzycisk(OKNO_SZER//2 - self.przyciski[1].obrazek.get_width()//2, OKNO_WYS//2 + self.przyciski[1].obrazek.get_height() - 50)
            self.przyciski[2].ustawPrzycisk(0, OKNO_WYS - self.przyciski[2].obrazek.get_height())
            self.przyciski[3].ustawPrzycisk(OKNO_SZER - self.przyciski[3].obrazek.get_width(), OKNO_WYS - self.przyciski[3].obrazek.get_height())
        elif self.tag == "ŚMIERĆ":
            self.przyciski[0].ustawPrzycisk(OKNO_SZER//2 - self.przyciski[0].obrazek.get_width()//2, OKNO_WYS//2 - self.przyciski[0].obrazek.get_height() - 50)
            self.przyciski[1].ustawPrzycisk(OKNO_SZER//2 - self.przyciski[1].obrazek.get_width()//2, OKNO_WYS//2 + self.przyciski[1].obrazek.get_height() - 50)
            self.przyciski[2].ustawPrzycisk(OKNO_SZER//2 - self.przyciski[2].obrazek.get_width()//2, OKNO_WYS//2 + 2* self.przyciski[2].obrazek.get_height() - 20)

    def rysujPrzyciski(self):
        """Rysuje przyciski obecne w danej scenie."""
        for przycisk in self.przyciski:
            przycisk.rysujPrzycisk()

    @staticmethod
    def fazaGry():
        """Tworzy przeciwników, jeżeli obecna scena to gra."""
        if scena == SCENA_GRA:
            Scena.faza.pojawPrzeciwnika()

# KLASA TESTY
class Testy(unittest.TestCase):

    def test_czy_gracz_strzelil(self):
        
        czy_strzal = Gracz.wystrzelPocisk(self)
        self.assertEqual(czy_strzal,True,"Nie zanotowano wystrzału.")

    def test_pocisk_kolizja(self):
        pass
        #self.assertTrue(self.sprawdzenie_kolizji,True, "Brak kolizji.")
    
    def test_usuwanie_przeciwnika(self):
        pass

if __name__ == '__main__':
     unittest.main()

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

cykl_pojawienia_pwr_up = 2

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
czas = 0

easter_egg = random.choice([True, False])

# funkcja sprawdzająca kolizję obiektów
def kolizja(obiekt1, obiekt2):
    """Sprawdza kolizję między dwoma obiektami, zwraca prawdę lub fałsz."""
    ramka_x = obiekt2.x - obiekt1.x
    ramka_y = obiekt2.y - obiekt1.y
    return obiekt1.mask.overlap(obiekt2.mask, (ramka_x, ramka_y)) != None

# funkcja restartująca wszystkie assety przed ponownym rozpoczęciem gry
def restart():
    zdrowie.hp = zdrowie.max_hp
    Gracz.ilość_rakiet = pakiet_rakiet
    gracz.aktualne_przegrzanie = gracz.maks_przegrzanie
    gracz.ustawGracza((OKNO_SZER - gracz.szer)//2, OKNO_WYS - gracz.wys - 50)

    Przeciwnik.stworzonych_przeciwnikow = 0
    Przeciwnik.pokonanych_przeciwnikow = 0
    cykl_pojawienia_pwr_up = 2
    Scena.faza = FAZA0
    
    enemyList.clear()
    pociskList.clear()
    bonusList.clear()
    wybuchList.clear()

# PRZYCISKI
WZNÓW = Przycisk(but_kontynuuj, but_kontynuuj_hover)
WYJDŹ = Przycisk(but_wyjscie, but_wyjscie_hover)
START = Przycisk(but_start, but_start_hover)
INSTRUKCJA = Przycisk(but_instrukcje, but_instrukcje_hover)
MENU = Przycisk(but_powrot, but_powrot_hover)
MUZYKA_ON = Przycisk(but_dzwiek_enabled, but_dzwiek_enabled_hover)
MUZYKA_OFF = Przycisk(but_dzwiek_disabled, but_dzwiek_disabled_hover)
INKWIZYCJA = Przycisk(but_inkwizycja, but_inkwizycja)

MUZYKA_ON.ustawPrzycisk(OKNO_SZER - MUZYKA_ON.obrazek.get_width(), OKNO_WYS - MUZYKA_ON.obrazek.get_height())
MUZYKA_OFF.ustawPrzycisk(OKNO_SZER - MUZYKA_OFF.obrazek.get_width(), OKNO_WYS - MUZYKA_OFF.obrazek.get_height())
MUZYKA = MUZYKA_ON
muzyka = True
puszczono = True

# SCENY
SCENA_INTRO = Scena("INTRO")
SCENA_MENU = Scena("MENU", [START, INSTRUKCJA, WYJDŹ])
SCENA_GRA = Scena("GRA")
SCENA_INSTRUKCJE = Scena("INSTRUKCJE", [INSTRUKCJA])
SCENA_PAUZA = Scena("PAUZA", [WZNÓW, WYJDŹ, MENU, INKWIZYCJA])
SCENA_ŚMIERĆ = Scena("ŚMIERĆ", [MENU, START, WYJDŹ])

scena = SCENA_INTRO

# GRA
graj = True
while graj:
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
            pygame.mixer.music.play(-1)
            scena = SCENA_MENU
            scena.ustawPrzyciski()
            czas_intro = 0
            puszczono = True
        if czas_intro > 370:
            if easter_egg:
                okienko.blit(bg_intro2, (0, 0))
                if puszczono:
                    pygame.mixer.music.play()
                    puszczono = False
            else:
                pygame.mixer.music.stop()
                pygame.mixer.music.load(mus_menu)
                pygame.mixer.music.play(-1)
                scena = SCENA_MENU
                scena.ustawPrzyciski()
                czas_intro = 0
                puszczono = True
        black.set_alpha(255 * (1 - abs(math.sin(czas_intro/117))))
        okienko.blit(black, (0, 0))
    elif scena == SCENA_MENU:
        TŁO1.rysujTło()
        TŁO2.rysujTło()
        scena.rysujPrzyciski()

        okienko.blit(logo, (OKNO_SZER//2 - logo.get_width()//2, 10))
        MUZYKA.rysujPrzycisk()

        if puszczono is False and muzyka:
            pygame.mixer.music.load(mus_menu)
            pygame.mixer.music.play(-1)
            puszczono = True

        if czas_intro < 120:
            czas_intro += 1
            black.set_alpha(255 * (1 - 5*abs(math.sin(czas_intro/116))))
            okienko.blit(black, (0, 0))

        if keys[pygame.K_ESCAPE]:
            graj = False
        if keys[pygame.K_r]:
            punkty.resetRekordu()

        for zdarzenie in zdarzenia:
            if zdarzenie.type == pygame.MOUSEBUTTONUP:
                if START.czyMyszka():
                    pygame.mixer.music.stop()
                    if muzyka:
                        pygame.mixer.music.load(mus_gra)
                        pygame.mixer.music.play(-1)
                    czas_intro = 0
                    scena = SCENA_GRA
                if WYJDŹ.czyMyszka():
                    graj = False
                if MUZYKA.czyMyszka():
                    muzyka = not muzyka
                    if muzyka:
                        MUZYKA = MUZYKA_ON
                        puszczono = False
                    else:
                        MUZYKA = MUZYKA_OFF
                        pygame.mixer.music.stop()
                if INSTRUKCJA.czyMyszka():
                    scena = SCENA_INSTRUKCJE
                    scena.ustawPrzyciski()
    elif scena == SCENA_INSTRUKCJE:
        TŁO1.rysujTło()
        TŁO2.rysujTło()
        scena.rysujPrzyciski()
        for zdarzenie in zdarzenia:
            if zdarzenie.type == pygame.MOUSEBUTTONUP and INSTRUKCJA.czyMyszka():
                scena = SCENA_MENU
                scena.ustawPrzyciski()
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
                    scena = SCENA_PAUZA
                    scena.ustawPrzyciski()
                    if muzyka:
                        pygame.mixer.music.set_volume(.03)

        # WYKONUJE SIĘ NA KAŻDY TICK
        TŁO1.rysujTło()
        TŁO2.rysujTło()
        czas_od_pocisku += dt
        czas_od_rakiety += dt
        czas_ruch_bonusu += dt/20
        czas_płynny_ruch_przeciwnika += dt/17

        if gracz.wystrzelPocisk():
            czas_od_pocisku = 0
        
        if czas_od_pocisku > 2000:
            czas_od_pocisku = Gracz.cooldown_strzalu

        if gracz.wystrzelRakiete():
            czas_od_rakiety = 0
        
        if czas_od_rakiety > 5000:
            czas_od_rakiety = Gracz.cooldown_rakiety
        
        enemy_do_usunięcia = []
        strzelający_przeciwnik = random.randint(0, 250)
        for enemy in enemyList:
            if enemy.id == strzelający_przeciwnik:
                enemy.wystrzelPocisk()
            if kolizja(enemy, gracz):
                enemy_do_usunięcia.append(enemy)
                punkty.dodawaniePunktów(-100)
                zdrowie.zmianaHp(-20)
            if kolizja(enemy, gracz.bariera):
                enemy_do_usunięcia.append(enemy)
            enemy.ruchPrzeciwnika()
            enemy.rysujPrzeciwnika()
        
        czas = pygame.time.get_ticks()
        czy_rakieta_wybucha = False
        
        if Przeciwnik.pokonanych_przeciwnikow == cykl_pojawienia_pwr_up:
            bonus = Bonusy()
            bonus.ustawBonus()
            bonusList.append(bonus)
            cykl_pojawienia_pwr_up += random.randint(10, 15)

        for bonus in bonusList:
            bonus.ruchBonusu()
            bonus.rysujBonus()
        
        bonusy_do_usunięcia = []
        
        pociski_do_usunięcia = []
        for pocisk in pociskList:
            pocisk.ruchPocisku()
            pocisk.rysujPocisk()
            if pocisk.kto_strzelił in ("gracz", "rakieta"):
                for enemy in enemyList:
                    if pocisk.czyKolizja(enemy):
                        pociski_do_usunięcia.append(pocisk)
                        if pocisk.kto_strzelił == "gracz":
                            enemy.hp += -1
                        if pocisk.kto_strzelił == "rakieta":
                            czy_rakieta_wybucha = True
                            wybuch = Wybuch(pocisk.x, pocisk.y)
                            wybuch.CzyWybuch(pocisk.x, pocisk.y, czas, False, True)
                            wybuchList.append(wybuch)
                            (x0, y0) = (pocisk.x + pocisk_gracza1.get_width()//2, pocisk.y + pocisk_gracza1.get_height()//2)
                            sfx_eksplozja_rakiety.play()
            if pocisk.kto_strzelił in ("kosmita", "krążownik", "kamikaze", "szturmowiec"):
                if pocisk.czyKolizja(gracz):
                    pociski_do_usunięcia.append(pocisk)
                    punkty.dodawaniePunktów(-100)
                    if pocisk.kto_strzelił == "kosmita":
                        strata = -20
                    elif pocisk.kto_strzelił == "szturmowiec":
                        strata = -10
                    else:
                        strata = -40
                    zdrowie.zmianaHp(strata)
                if pocisk.czyKolizja(gracz.bariera):
                    pociski_do_usunięcia.append(pocisk)
                    sfx_leczenie.play()
            if pocisk.pozaOknem() and pocisk not in pociski_do_usunięcia:
                pociski_do_usunięcia.append(pocisk)

            for bonus in bonusList:
                if pocisk.czyKolizja(bonus) and pocisk.kto_strzelił in ("gracz", "rakieta") and bonus.nietrafiony:
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
        
        if czy_rakieta_wybucha:
            for enemy in enemyList:
                if ((enemy.x + enemy.obraz.get_width()//2) - x0)**2 + ((enemy.y + enemy.obraz.get_height()//2) - y0)**2 <= (eksplozja.get_height())**2:
                    enemy.hp += -14
                if enemy.hp <= 0:
                    punkty.dodawaniePunktów(200)
                    Przeciwnik.pokonanych_przeciwnikow += 1
                    enemy_do_usunięcia.append(enemy)
        else:
            for enemy in enemyList:
                if enemy.hp <= 0:
                    punkty.dodawaniePunktów(200)
                    Przeciwnik.pokonanych_przeciwnikow += 1
                    enemy_do_usunięcia.append(enemy)
        
        for enemy in enemy_do_usunięcia:
            wybuch = Wybuch(enemy.x, enemy.y)
            if enemy.tag == "krążownik":
                wybuch.CzyWybuch(enemy.x, enemy.y, czas, True, False)
            else:
                wybuch.CzyWybuch(enemy.x, enemy.y, czas, False, False)
            wybuchList.append(wybuch)
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
        
        for bonus in bonusy_do_usunięcia:
            try:
                bonusList.remove(bonus)
            except:
                print("Błąd usunięcia bonusu.")
        
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
            
            scena = SCENA_ŚMIERĆ
            scena.ustawPrzyciski()
            if muzyka:
                pygame.mixer.music.load(mus_gameover)
                pygame.mixer.music.play()
            
            restart()
        
        if czas_intro < 170:
            czas_intro += 1
            black.set_alpha(255 * (1 - 2*abs(math.sin(czas_intro/116))))
            okienko.blit(black, (0, 0))
    elif scena == SCENA_PAUZA:
        okienko.blit(bg_pauza, (0, 0))
        scena.rysujPrzyciski()
        pygame.display.update() # to ważne, nie usuwać
        for zdarzenie in zdarzenia:
            if zdarzenie.type == pygame.KEYDOWN:
                if zdarzenie.key == pygame.K_ESCAPE:
                    if muzyka:
                        pygame.mixer.music.set_volume(.25)
                    scena = SCENA_GRA
            elif zdarzenie.type == pygame.MOUSEBUTTONDOWN:
                if WZNÓW.czyMyszka():
                    if muzyka:
                        pygame.mixer.music.set_volume(.25)
                    scena = SCENA_GRA
                elif MENU.czyMyszka():
                    if muzyka:
                        pygame.mixer.music.set_volume(.25)
                    scena = SCENA_MENU
                    scena.ustawPrzyciski()
                    czas_intro = 0
                    if muzyka:
                        pygame.mixer.music.load(mus_menu)
                        pygame.mixer.music.play()
                    restart()
                    punkty.wynik = 0
                elif WYJDŹ.czyMyszka():
                    graj = False
                elif INKWIZYCJA.czyMyszka():
                    sfx_inkwizycja.play()
    elif scena == SCENA_ŚMIERĆ:
        okienko.blit(bg_gameover, (0,0))
        scena.rysujPrzyciski()
        punkty.rysujScoreboard()

        czas_intro = 0

        for zdarzenie in zdarzenia:
            if zdarzenie.type == pygame.MOUSEBUTTONUP:
                if WYJDŹ.czyMyszka():
                    graj = False
                elif MENU.czyMyszka():
                    punkty.wynik = 0
                    scena = SCENA_MENU
                    scena.ustawPrzyciski()
                    pygame.mixer.stop()
                    if muzyka:
                        pygame.mixer.music.load(mus_menu)
                        pygame.mixer.music.play(-1)
                elif START.czyMyszka():
                    punkty.wynik = 0
                    czas_intro = 0
                    scena = SCENA_GRA
                    scena.ustawPrzyciski()
                    if muzyka:
                        pygame.mixer.music.stop()
                        pygame.mixer.music.load(mus_gra)
                        pygame.mixer.music.play(-1)

pygame.quit()

