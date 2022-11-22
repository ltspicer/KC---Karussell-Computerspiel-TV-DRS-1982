#!/usr/bin/python3

################################
# KC - Karussell Computerspiel #
#    von Daniel Luginbuehl     #
#          (C) 2022            #
#  webmaster@ltspiceusers.ch   #
#                              #
#         TV DRS 1982          #
################################


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
        print()
        print("Soundtrack by Jean-Michel Jarre -- Copyright: https://www.youtube.com/watch?v=hD4KMp22jBg")
        print()
    except Exception as e:
        print("Musikdatei nicht gefunden. Spiel läuft ohne Musik!")
        pygameok = 0

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

import random, sys, click, time, os

my_os=sys.platform

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

#### Konsole löschen

def clearConsole():
    command = 'clear'
    if my_os == "win32":  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)

#### Terminal neu schreiben

def printTerminal():
    for i in range(0, len(text)):
        print(text[i])

#### Eingabe anzeigen

def print_there(y, text):
    #          my_os=
    #`win32`   for Windows(Win32)
    #'cygwin'  for Windows(cygwin)
    #'darwin'  for macOS
    #'aix'     for AIX
    if my_os == "win32":
        return
    if my_os == "linux" or my_os == "darwin":
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
                clearConsole()
                printTerminal()
            if eingabe == "q":
                print("Spiel beendet")
                time.sleep(3)
                sys.exit()
            if eingabe == '0' or eingabe == '1' or eingabe == '2' or eingabe == '3' or eingabe == '4' or eingabe == '5' or eingabe == '6' or eingabe == '7' or eingabe == '8' or eingabe == '9':
                clearConsole()
                printTerminal()
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
        clearConsole()
        printTerminal()

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

    clearConsole()
    text.append("Spiel " + str(spiel) + " = " + str(num1) + str(num2) + str(num3) + " " + antwort)
    printTerminal()
    if antwort == "As As As ":
        print("Spiel gewonnen!")
        time.sleep(5)
        sys.exit()
    spiel+=1
    if spiel == 10:
        print("Spiel verloren!")
        print("Die gesuchte Zahl wäre "+str(ziffer1)+str(ziffer2)+str(ziffer3)+" gewesen.")
        time.sleep(5)
        sys.exit()
