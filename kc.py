#!/usr/bin/python3

################################
# KC - Karussell Computerspiel #
#    von Daniel Luginbuehl     #
#          (C) 2022            #
#  webmaster@ltspiceusers.ch   #
#                              #
#         TV DRS 1982          #
################################

# Soundtrack by Jean-Michel Jarre -- Copyright: https://www.youtube.com/watch?v=hD4KMp22jBg

pygameok = 1
try:
    from pygame import mixer
except ImportError as e:
    print("Kein pygame installiert. Spiel läuft ohne Musik!")
    pygameok = 0

if pygameok == 1:
    mixer.init()
    mixer.music.set_volume(0.3)
    try:
        mixer.music.load("Oxygen2.mp3")
        mixer.music.play(-1)
    except Exception as e:
        print("Musikdatei nicht gefunden. Spiel läuft ohne Musik!")
        pygameok = 0


print()
print()
print("################################")
print("# KC - Karussell Computerspiel #")
print("#         TV DRS 1982          #")
print("################################")
print()
print()
print("Finde die 3-stellige Zahl.")
print("Du hast 9 Spielzüge. Viel Glück.")
print("c = neue Eingabe")
print("q = Spiel abbrechen")
print()
print("                                       Eingabe")
print()


import random, sys, click


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

spiel = 1


#### Eingabe anzeigen

def print_there(y, text):
     sys.stdout.write("\x1b7\x1b[%d;%df%s\x1b8" % (40, y, text))
     sys.stdout.flush()

#### Spielschlaufe

while True:
    while True:
        i = 0
        while i < 3:
            eingabe = click.getchar()   # Gets a single character
            if eingabe == "c":
                i = 0
                print_there(40, "   ")
            if eingabe == "q":
                exit()
            if eingabe == '0' or eingabe == '1' or eingabe == '2' or eingabe == '3' or eingabe == '4' or eingabe == '5' or eingabe == '6' or eingabe == '7' or eingabe == '8' or eingabe == '9':
                if i == 0:
                    num1 = int(eingabe)
                    print_there(40, str(num1))
                if i == 1:
                    num2 = int(eingabe)
                    print_there(41, str(num2))
                if i == 2:
                    num3 = int(eingabe)
                    print_there(42, str(num3))
                i+=1

        if num1 != num2 and num1 != num3 and num2 != num3:
            break
        print_there(40, "   ")

    antwort = ""
    if ziffer1 == num1:
        antwort+="As "
    if ziffer2 == num2:
        antwort+="As "
    if ziffer3 == num3:
        antwort+="As "
    if ziffer1 == num2:
        antwort+="Gut "
    if ziffer1 == num3:
        antwort+="Gut "
    if ziffer2 == num1:
        antwort+="Gut "
    if ziffer2 == num3:
        antwort+="Gut "
    if ziffer3 == num1:
        antwort+="Gut "
    if ziffer3 == num2:
        antwort+="Gut "

    print_there(40, "   ")
    print("Spiel", spiel, "=", str(num1) + str(num2) + str(num3), antwort)
    if antwort == "As As As ":
        print("Spiel gewonnen!")
        exit()
    spiel+=1
    if spiel == 10:
        print("Spiel verloren!")
        exit()
