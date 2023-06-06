# -*- coding: utf-8 -*-

import random

#time funktio sleep joka hidastaa komentoja ajallisesti eli saadaan esim. printattua hitaammin
from time import sleep

#mahdollistaa os.system('cls') käytön jotta voidaan tyhjentää ruutu
import os

#ascii muotoinen logo alussa
ascii_biljon = '''
██   ██  █████  ██      ██    ██  █████  ████████ ██   ██  ██████                           
██   ██ ██   ██ ██      ██    ██ ██   ██    ██    ██  ██  ██    ██                          
███████ ███████ ██      ██    ██ ███████    ██    █████   ██    ██                          
██   ██ ██   ██ ██      ██    ██ ██   ██    ██    ██  ██  ██    ██                          
██   ██ ██   ██ ███████  ██████  ██   ██    ██    ██   ██  ██████                           
                                                                                            
                                                                                            
██████  ██ ██           ██  ██████  ███    ██  █████   █████  ██████  ██ ██   ██ ███████ ██ 
██   ██ ██ ██           ██ ██    ██ ████   ██ ██   ██ ██   ██ ██   ██ ██ ██  ██  ██      ██ 
██████  ██ ██           ██ ██    ██ ██ ██  ██ ███████ ███████ ██████  ██ █████   ███████ ██ 
██   ██ ██ ██      ██   ██ ██    ██ ██  ██ ██ ██   ██ ██   ██ ██   ██ ██ ██  ██       ██ ██ 
██████  ██ ███████  █████   ██████  ██   ████ ██   ██ ██   ██ ██   ██ ██ ██   ██ ███████ ██ 
                                                                                            
'''
#ascii muotoinen kehoitus painaa enteriä jotta peli alkaa
ascii_enter = '''
██████   █████  ██ ███    ██  █████      ███████ ███    ██ ████████ ███████ ██████  
██   ██ ██   ██ ██ ████   ██ ██   ██     ██      ████   ██    ██    ██      ██   ██ 
██████  ███████ ██ ██ ██  ██ ███████     █████   ██ ██  ██    ██    █████   ██████  
██      ██   ██ ██ ██  ██ ██ ██   ██     ██      ██  ██ ██    ██    ██      ██   ██ 
██      ██   ██ ██ ██   ████ ██   ██     ███████ ██   ████    ██    ███████ ██   ██ 
                                                                                    
                                                                                    
     ██  █████  ████████ ██   ██  █████   █████  ██   ██ ███████ ███████ ███████ ██ 
     ██ ██   ██    ██    ██  ██  ██   ██ ██   ██ ██  ██  ██      ██      ██      ██ 
     ██ ███████    ██    █████   ███████ ███████ █████   ███████ █████   ███████ ██ 
██   ██ ██   ██    ██    ██  ██  ██   ██ ██   ██ ██  ██       ██ ██           ██ ██ 
 █████  ██   ██    ██    ██   ██ ██   ██ ██   ██ ██   ██ ███████ ███████ ███████ ██                                  
'''

ascii_alkaa = '''
██████  ███████ ██      ██      █████  ██      ██   ██  █████   █████  ██ 
██   ██ ██      ██      ██     ██   ██ ██      ██  ██  ██   ██ ██   ██ ██ 
██████  █████   ██      ██     ███████ ██      █████   ███████ ███████ ██ 
██      ██      ██      ██     ██   ██ ██      ██  ██  ██   ██ ██   ██    
██      ███████ ███████ ██     ██   ██ ███████ ██   ██ ██   ██ ██   ██ ██ 
                                                                          
'''

#while silmukka joka vilkuttaa aloituslogoa neljästi,
#jonka jälkeen kehoitetaan painamaan enteriä jotta peli alkaa
biljon = 4
while True:
    biljon = biljon - 1
    sleep(0.65)
    print(ascii_biljon)
    sleep(0.65)
    os.system('cls')
    if biljon <= 0:
        sleep(0.3)
        print(ascii_enter)
        input("")
        break

#käyttäjä painaa enteriä ja peli aukeaa
#tyhjennetään ruutu
os.system('cls')

#tervetuloilmoitus
print("Tervetuloa Haluatko Biljonääriksi peliin!")



#tämä silmukka kysyy pelaajalta haluaako hän pelata vai ei
while True:
    haluatko = input("Haluatko Biljonääriksi? (Kyllä/En):  ")
    
    #jos pelaaja vastaa kyllä, tapahtuu pelin aloitus
    #silmukka päättyy
    if haluatko == "Kyllä" or haluatko == "kyllä":
        sleep(1)
        print("Aloitetaan peli!")
        sleep(1)
        break
    
    #jos vastaa että ei halua pelata, pakotetaan hänet silti pelaamaan
    #silmukka päättyy
    elif haluatko == "En" or haluatko == "en":
        print("Vai niin...")
        sleep(1)
        print("...")
        sleep(1)
        print("Sinun on pakko pelata!")
        sleep(1)
        print("Aloitetaan peli!")
        sleep(1)
        break
    
    #mikäli pelaaja ei vastaa "kyllä" tai "ei", kysytään pelaajalta uudelleen ja silmukka alkaa alusta
    else:
        sleep(1)
        print("En oikein ymmärtäny mitä tarkoitit.")

#tyhjennetään ruutu
os.system('cls')

#määritellään arvo funktiolle "luku"
luku = 5
sleep(1)
print("Lähtölaskenta!")

#silmukka tekee lähtölaskennan aijemmin määrittelemän luvun perustella
#joka silmukan kierroksella luku pienenee yhdellä
#kun "luku" saavuttaa arvon 0, printataan "Peli alkaa!", ja silmukka katkeaa
while True:
    sleep(0.5)
    print(luku)
    luku = luku - 1
    if luku == 0:
        sleep(1)
        print("Peli alkaa!")
        break
sleep(2)

#tyhjennetään ruutu
os.system('cls')

#printataan pelin säännöt
sleep(1)
print("Kerrataan alkuun vielä pelin säännöt.")
sleep(2)
print("Sinulta kysytään 8 kysymystä.")
sleep(3)
print("Mikäli vastaat oikein, saat kysymystä vastaavan rahasumman.")
sleep(4)
print("Mikäli vastaat väärin yhteenkin kysymykseen, menetätä kaikki voittamasi rahat.")
sleep(4)
print("Pelistä ei siis voi karata kesken pelin rahojen kanssa.")
sleep(3)
print("Nyt pelataan biljoonasta eurosta!")
sleep(3)
#silmukka joka printtaa pisteitä
luku1 = 5
while True:
    sleep(0.2)
    print("...")
    luku1 = luku1 - 1
    if luku1 == 0:
        break
print("Tässä tulee ensimmäinen testi ennen peliä")
sleep(3)

#tyhjennetään ruutu
os.system('cls')

sleep(1)

#silmukka joka kysyy muistatko säännöt
while True:
    muistatko = input("Muistatko nyt varmasti kaikki säännöt? (kirjoita kyllä/en): ")
    if muistatko == "kyllä" or muistatko == "Kyllä":
        print("Hieno juttu")
        break
    elif muistatko == "en" or muistatko == "En":
        print("Oma vika, onnea peliin silti")
        break
    else:
        print("En oikein ymmärtäny mitä tarkoitit.")

sleep(4)

alkaa = 4
while True:
    alkaa = alkaa - 1
    sleep(0.65)
    print(ascii_alkaa)
    sleep(0.65)
    os.system('cls')
    if alkaa <= 0:
        break

os.system('cls')

sleep(1)

def lue_kysymykset_tiedostosta(tiedoston_nimi):
    kysymykset = []
    with open(tiedoston_nimi, 'r') as tiedosto:
        for rivi in tiedosto:
            kysymys, vastaus, *vaihtoehdot = rivi.strip().split(',')
            vaihtoehdot.append(vastaus)
            kysymykset.append((kysymys, vastaus, vaihtoehdot))
    return kysymykset

import random
import os
from time import sleep

def lue_kysymykset_tiedostosta(tiedoston_nimi):
    # Funktio lukee kysymykset tiedostosta ja palauttaa listan kysymyksiä
    kysymykset = []
    with open(tiedoston_nimi, 'r') as tiedosto:
        for rivi in tiedosto:
            # Erotellaan rivi kysymykseksi, vastaukseksi ja vaihtoehdoiksi
            kysymys, vastaus, *vaihtoehdot = rivi.strip().split(',')
            vaihtoehdot.append(vastaus)  # Lisätään oikea vastaus vaihtoehtoihin
            kysymykset.append((kysymys, vastaus, vaihtoehdot))
    return kysymykset

def pelaa_peli():
    tiedoston_nimi = os.path.join(os.path.dirname(__file__), "kysymykset.txt")
    kysymykset = lue_kysymykset_tiedostosta(tiedoston_nimi)
    random.shuffle(kysymykset)
    kaytetyt_kysymykset = set()

    palkintosumma = 10
    
    for kysymys, vastaus, vaihtoehdot in kysymykset[:8]:
        if kysymys in kaytetyt_kysymykset:
            continue
        kaytetyt_kysymykset.add(kysymys)
        
        sleep(3)  # Odottaa 3 sekuntia ennen kysymyksen näyttämistä
        os.system('cls')  # Tyhjentää näytön
        
        print(kysymys)  # Tulostaa kysymyksen
        
        random.shuffle(vaihtoehdot)  # Sekoittaa vaihtoehdot
        for i, vaihtoehto in enumerate(vaihtoehdot):
            print(f"{chr(97 + i)}) {vaihtoehto}")  # Tulostaa vaihtoehdot
        
        oikea_vaihtoehto = chr(97 + vaihtoehdot.index(vastaus))  # Laskee oikean vaihtoehdon indeksin
        
        while True:
            arvaus = input("Valitse vaihtoehto (a, b, c tai d): ")  # Kysyy käyttäjältä vastausta
            
            if arvaus.lower() not in ['a', 'b', 'c', 'd']:
                print("Virheellinen syöte. Valitse vaihtoehto a, b, c tai d.")
            else:
                break
        
        if arvaus.lower() == oikea_vaihtoehto:
            palkintosumma = palkintosumma * 10
            print(f'Oikein! Ansaitset {palkintosumma} euroa.\n')
        else:
            print('Väärin! Peli päättyy.')
            return
    
    print(f'Onneksi olkoon! Vastasit kaikkiin kysymyksiin oikein ja voitat {palkintosumma} euroa.')

pelaa_peli()
