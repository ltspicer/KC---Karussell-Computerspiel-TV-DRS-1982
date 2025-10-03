#!/bin/bash

################################
# KC - Karussell Computerspiel #
#    von Daniel Luginbuehl     #
#          (C) 2025            #
#  webmaster@ltspiceusers.ch   #
#                              #
#         TV DRS 1982          #
################################


# Konsole löschen
clear_console() {
    clear
}

# Konsole neu schreiben
print_terminal() {
    for line in "${text[@]}"; do
        echo "$line"
    done
}

text=(
    "################################"
    "# KC - Karussell Computerspiel #"
    "#         TV DRS 1982          #"
    "################################"
    " "
    " "
    "Finde die 3-stellige Zahl."
    "Du hast 9 Spielzüge. Viel Glück."
    "c = aktuelle Eingabe löschen"
    "q = Spiel abbrechen"
    " "
    " "
)

clear_console

for line in "${text[@]}"; do
    echo "$line"
done
echo "Gib jetzt die ersten 3 Zahlen ein."
echo "Eingabe:"
echo ""
stty -echo
trap "stty echo" EXIT

# Zahlen generieren
ziffer1=$(( RANDOM % 10 ))
while true; do
    ziffer2=$(( RANDOM % 10 ))
    if [ $ziffer2 -ne $ziffer1 ]; then
        break
    fi
done
while true; do
    ziffer3=$(( RANDOM % 10 ))
    if [ $ziffer3 -ne $ziffer1 ] && [ $ziffer3 -ne $ziffer2 ]; then
        break
    fi
done

SPIEL=1

# Hauptschleife
while true; do
    while true; do
        i=0
        while [ $i -lt 3 ]; do
            read -n 1 eingabe
            if [ "$eingabe" == "c" ]; then
                i=0
                clear_console
                print_terminal
            fi
            if [ "$eingabe" == "q" ]; then
                echo "Spiel beendet"
                stty echo
                sleep 3
                exit
            fi
            if [[ "$eingabe" =~ ^[0-9]$ ]]; then
                clear_console
                print_terminal
                if [ $i -eq 0 ]; then
                    num1=$(( eingabe ))
                    echo "$num1"
                fi
                if [ $i -eq 1 ]; then
                    num2=$(( eingabe ))
                    echo "$num1$num2"
                fi
                if [ $i -eq 2 ]; then
                    num3=$(( eingabe ))
                    echo "$num1$num2$num3"
                fi
                ((i++))
            fi
        done

        if [ $num1 -ne $num2 ] && [ $num1 -ne $num3 ] && [ $num2 -ne $num3 ]; then
            break
        fi
        clear_console
        print_terminal
    done

    ANTWORT=""
    if [ $ziffer1 -eq $num1 ]; then
        ANTWORT+="As "
    fi
    if [ $ziffer2 -eq $num2 ]; then
        ANTWORT+="As "
    fi
    if [ $ziffer3 -eq $num3 ]; then
        ANTWORT+="As "
    fi
    if [ $ziffer1 -eq $num2 ] || [ $ziffer1 -eq $num3 ]; then
        ANTWORT+="Gut "
    fi
    if [ $ziffer2 -eq $num1 ] || [ $ziffer2 -eq $num3 ]; then
        ANTWORT+="Gut "
    fi
    if [ $ziffer3 -eq $num1 ] || [ $ziffer3 -eq $num2 ]; then
        ANTWORT+="Gut "
    fi

    clear_console
    text+=("Spiel $SPIEL = $num1$num2$num3 $ANTWORT")
    print_terminal
    if [ "$ANTWORT" == "As As As " ]; then
        echo "Spiel gewonnen!"
        read -p "ENTER zum beenden/Press ENTER to exit"
        echo
        exit
    fi
    ((SPIEL++))
    if [ $SPIEL -eq 10 ]; then
        echo "Spiel verloren!"
        echo "Die gesuchte Zahl wäre $ziffer1$ziffer2$ziffer3 gewesen."
        read -p "ENTER zum beenden/Press ENTER to exit"
        echo
        exit
    fi
done
