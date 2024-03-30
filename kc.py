#!/usr/bin/python3

################################
# KC - Karussell Computerspiel #
#    von Daniel Luginbuehl     #
#          (C) 2022            #
#  webmaster@ltspiceusers.ch   #
#                              #
#         TV DRS 1982          #
################################

import os
import sys
import time
import random
import click

if os.path.exists("Oxygen2.mp3"):
    PYGAME_OK = 1
    try:
        from pygame import mixer
    except ImportError:
        print("Kein pygame installiert. Spiel läuft ohne Musik!")
        PYGAME_OK = 0

    if PYGAME_OK == 1:
        mixer.init()
        mixer.music.set_volume(0.3)
        mixer.music.load("Oxygen2.mp3")
        mixer.music.play(-1)
        print()
        print("Soundtrack by Jean-Michel Jarre -- Copyright:\
            https://www.youtube.com/watch?v=hD4KMp22jBg")
        print()
else:
    print("Musikdatei nicht gefunden. Spiel läuft ohne Musik!")

text = ["################################",
"# KC - Karussell Computerspiel #",
"#         TV DRS 1982          #",
"################################",
" ",
" ",
"Finde die 3-stellige Zahl.",
"Du hast 9 Spielzüge. Viel Glück.",
"c = aktuelle Eingabe löschen",
"q = Spiel abbrechen",
" ",
" "]

print()
print(text[0])
print(text[1])
print(text[2])
print(text[3])
print(text[4])
print(text[5])
print(text[6])
print(text[7])
print(text[8])
print(text[9])
print(text[10])
print("Gib jetzt die ersten 3 Zahlen ein.")
print("Eingabe:")
print()
print('\033[?25l', end="")

MY_OS=sys.platform

#### Zahlen generieren

ziffer1 = random.randint(0, 9)
while True:
    ziffer2 = random.randint(0, 9)
    if ziffer2 != ziffer1:
        break
while True:
    ziffer3 = random.randint(0, 9)
    if ziffer3 != ziffer1 and ziffer3 != ziffer2:
        break

#print(ziffer1, ziffer2, ziffer3)

SPIEL = 1

#### Konsole löschen

def clear_console():
    command = 'clear'
    if MY_OS == "win32":  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)

#### Konsole neu schreiben

def print_terminal():
    for z in enumerate(text):
        print(z)

#### Hauptschleife

while True:
    while True:
        i = 0
        while i < 3:
            eingabe = click.getchar()   # Gets a single character
            if eingabe == "c":
                i = 0
                clear_console()
                print_terminal()
            if eingabe == "q":
                print("Spiel beendet")
                print('\033[?25h', end="")
                time.sleep(3)
                sys.exit()
            if eingabe == '0' or eingabe == '1' or eingabe == '2' or eingabe == '3' or\
               eingabe == '4' or eingabe == '5' or eingabe == '6' or eingabe == '7' or\
               eingabe == '8' or eingabe == '9':
                clear_console()
                print_terminal()
                if i == 0:
                    num1 = int(eingabe)
                    print(str(num1))
                if i == 1:
                    num2 = int(eingabe)
                    print(str(num1)+str(num2))
                if i == 2:
                    num3 = int(eingabe)
                    print(str(num1)+str(num2)+str(num3))
                i+=1

        if num1 != num2 and num1 != num3 and num2 != num3:
            break
        clear_console()
        print_terminal()

    ANTWORT = ""
    if ziffer1 == num1:
        ANTWORT+="As "
    if ziffer2 == num2:
        ANTWORT+="As "
    if ziffer3 == num3:
        ANTWORT+="As "
    if ziffer1 == num2:
        ANTWORT+="Gut "
    if ziffer1 == num3:
        ANTWORT+="Gut "
    if ziffer2 == num1:
        ANTWORT+="Gut "
    if ziffer2 == num3:
        ANTWORT+="Gut "
    if ziffer3 == num1:
        ANTWORT+="Gut "
    if ziffer3 == num2:
        ANTWORT+="Gut "

    clear_console()
    text.append("Spiel " + str(SPIEL) + " = " + str(num1) + str(num2) + str(num3) + " " + ANTWORT)
    print_terminal()
    if ANTWORT == "As As As ":
        print("Spiel gewonnen!")
        time.sleep(5)
        sys.exit()
    SPIEL+=1
    if SPIEL == 10:
        print("Spiel verloren!")
        print("Die gesuchte Zahl wäre "+str(ziffer1)+str(ziffer2)+str(ziffer3)+" gewesen.")
        time.sleep(5)
        sys.exit()
