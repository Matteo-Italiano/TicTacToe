import random
import tkinter as tk

player_1 = "X"
player_2 = "O"

a, b, c = 1, 2, 3
d, e, f = 4, 5, 6
g, h, i = 7, 8, 9

def print_area():
    print(f" >>> {a} {b} {c}\n >>> {d} {e} {f}\n >>> {g} {h} {i}")

def has_won(player):
    player_validation_string = f"{player}{player}{player}"

    if f"{a}{b}{c}" == player_validation_string:
        return True
    if f"{d}{e}{f}" == player_validation_string:
        return True
    if f"{g}{h}{i}" == player_validation_string:
        return True
    if f"{a}{d}{g}" == player_validation_string:
        return True
    if f"{b}{e}{h}" == player_validation_string:
        return True
    if f"{c}{f}{i}" == player_validation_string:
        return True
    if f"{a}{e}{i}" == player_validation_string:
        return True
    if f"{g}{e}{c}" == player_validation_string:
        return True
    
    return False

def computer():
    global a, b, c, d, e, f, g, h, i
    available_fields = []

    almost_winning_constelation = f"{player_2}{player_2}"
    almost_loosing_constelation = f"{player_1}{player_1}"

    if isinstance(a, int):
        available_fields.append("a")
    if isinstance(b, int):
        available_fields.append("b")
    if isinstance(c, int):
        available_fields.append("c")
    if isinstance(d, int):
        available_fields.append("d")
    if isinstance(e, int):
        available_fields.append("e")
    if isinstance(f, int):
        available_fields.append("f")
    if isinstance(g, int):
        available_fields.append("g")
    if isinstance(h, int):
        available_fields.append("h")
    if isinstance(i, int):
        available_fields.append("i")

    # The code below is used for Winning when theres the Opportunity Horizontal
    if f"{a}{b}" == almost_winning_constelation and "c" in available_fields:
          c = f"{player_2}"
            
    elif f"{b}{c}" == almost_winning_constelation and "a" in available_fields:
            a = f"{player_2}"
            
    elif f"{a}{c}" == almost_winning_constelation and "b" in available_fields:
            b = f"{player_2}"
            
    elif f"{d}{e}" == almost_winning_constelation and "f" in available_fields:
            f = f"{player_2}"
            
    elif f"{e}{f}" == almost_winning_constelation and "d" in available_fields:
            d = f"{player_2}"
            
    elif f"{d}{f}" == almost_winning_constelation and "e" in available_fields:
            e = f"{player_2}"
            
    elif f"{g}{h}" == almost_winning_constelation and "i" in available_fields:
            i = f"{player_2}"
            
    elif f"{h}{i}" == almost_winning_constelation and "g" in available_fields:
            g = f"{player_2}"
            
    elif f"{g}{i}" == almost_winning_constelation and "h" in available_fields:
            h = f"{player_2}"

    #The Code Below is used to win Vertical
    elif f"{a}{d}" == almost_winning_constelation and "g" in available_fields:
            g = f"{player_2}"
            
    elif f"{d}{g}" == almost_winning_constelation and "a" in available_fields:
            a = f"{player_2}"
            
    elif f"{a}{g}" == almost_winning_constelation and "d" in available_fields:
            d = f"{player_2}"
            
    elif f"{b}{e}" == almost_winning_constelation and "h" in available_fields:
            h = f"{player_2}"
            
    elif f"{e}{h}" == almost_winning_constelation and "b" in available_fields:
            b = f"{player_2}"
            
    elif f"{b}{h}" == almost_winning_constelation and "e" in available_fields:
            e = f"{player_2}"
            
    elif f"{c}{f}" == almost_winning_constelation and "i" in available_fields:
            i= f"{player_2}"
            
    elif f"{f}{i}" == almost_winning_constelation and "h" in available_fields:
            c = f"{player_2}"

    elif f"{c}{i}" == almost_winning_constelation and "f" in available_fields:
            f = f"{player_2}"

    #the code below is used for winning Diagonally
    elif f"{a}{e}" == almost_winning_constelation and "i" in available_fields:
            i = f"{player_2}"
            
    elif f"{e}{i}" == almost_winning_constelation and "a" in available_fields:
            a = f"{player_2}"
            
    elif f"{a}{i}" == almost_winning_constelation and "e" in available_fields:
            e = f"{player_2}"
            
    elif f"{c}{e}" == almost_winning_constelation and "g" in available_fields:
            g= f"{player_2}"
            
    elif f"{e}{g}" == almost_winning_constelation and "c" in available_fields:
            c = f"{player_2}"

    elif f"{g}{c}" == almost_winning_constelation and "e" in available_fields:
            e = f"{player_2}"

    #The Code Below is used for Blocking the Opponent Horizontal
    elif f"{a}{b}" == almost_loosing_constelation and "c" in available_fields:
          c = f"{player_2}"
            
    elif f"{b}{c}" == almost_loosing_constelation and "a" in available_fields:
            a = f"{player_2}"
            
    elif f"{a}{c}" == almost_loosing_constelation and "b" in available_fields:
            b = f"{player_2}"
            
    elif f"{d}{e}" == almost_loosing_constelation and "f" in available_fields:
            f = f"{player_2}"
            
    elif f"{e}{f}" == almost_loosing_constelation and "d" in available_fields:
            d = f"{player_2}"
            
    elif f"{d}{f}" == almost_loosing_constelation and "e" in available_fields:
            e = f"{player_2}"
            
    elif f"{g}{h}" == almost_loosing_constelation and "i" in available_fields:
            i = f"{player_2}"
            
    elif f"{h}{i}" == almost_loosing_constelation and "g" in available_fields:
            g = f"{player_2}"
            
    elif f"{g}{i}" == almost_loosing_constelation and "h" in available_fields:
            h = f"{player_2}"

    #the Code below is used for Blocking vertical
    elif f"{a}{d}" == almost_loosing_constelation and "g" in available_fields:
            g = f"{player_2}"
            
    elif f"{d}{g}" == almost_loosing_constelation and "a" in available_fields:
            a = f"{player_2}"
            
    elif f"{a}{g}" == almost_loosing_constelation and "d" in available_fields:
            d = f"{player_2}"
            
    elif f"{b}{e}" == almost_loosing_constelation and "h" in available_fields:
            h = f"{player_2}"
            
    elif f"{e}{h}" == almost_loosing_constelation and "b" in available_fields:
            b = f"{player_2}"
            
    elif f"{b}{h}" == almost_loosing_constelation and "e" in available_fields:
            e = f"{player_2}"
            
    elif f"{c}{f}" == almost_loosing_constelation and "i" in available_fields:
            i= f"{player_2}"
            
    elif f"{f}{i}" == almost_loosing_constelation and "h" in available_fields:
            c = f"{player_2}"

    elif f"{c}{i}" == almost_loosing_constelation and "f" in available_fields:
            f = f"{player_2}"

    #the Code below is Used for Blocking the Oponnent Diagonally
    elif f"{a}{e}" == almost_loosing_constelation and "i" in available_fields:
            i = f"{player_2}"
            
    elif f"{e}{i}" == almost_loosing_constelation and "a" in available_fields:
            a = f"{player_2}"
            
    elif f"{a}{i}" == almost_loosing_constelation and "e" in available_fields:
            e = f"{player_2}"
            
    elif f"{c}{e}" == almost_loosing_constelation and "g" in available_fields:
            g= f"{player_2}"
            
    elif f"{e}{g}" == almost_loosing_constelation and "c" in available_fields:
            c = f"{player_2}"

    elif f"{g}{c}" == almost_loosing_constelation and "e" in available_fields:
            e = f"{player_2}"

    elif available_fields:
        choice = random.choice(available_fields)
        if choice == "a":
            a = f"{player_2}"
        elif choice == "b":
            b = f"{player_2}"
        elif choice == "c":
            c = f"{player_2}"
        elif choice == "d":
            d = f"{player_2}"
        elif choice == "e":
            e = f"{player_2}"
        elif choice == "f":
            f = f"{player_2}"
        elif choice == "g":
            g = f"{player_2}"
        elif choice == "h":
            h = f"{player_2}"
        elif choice == "i":
            i = f"{player_2}"

def tie():   
    global a, b, c, d, e, f, g, h, i
    
    if isinstance(a, int):
        return False
    if isinstance(b, int):
       return False
    if isinstance(c, int):
       return False
    if isinstance(d, int):
        return False
    if isinstance(e, int):
        return False
    if isinstance(f, int):
        return False
    if isinstance(g, int):
        return False
    if isinstance(h, int):
        return False
    if isinstance(i, int):
        return False
    return True


number_of_players = input(f"Wie viele Spieler (1/2)?:   ")

if number_of_players == "2":
    print("Viel Spaß!")
    print_area()

    current_turn = f"{player_1}"
    while not (has_won(f"{player_1}") or has_won(f"{player_2}") or tie()):
        user_input_field = input(f"Wähle ein Feld aus ({current_turn}): ")

        if user_input_field == f"{player_1}" or user_input_field == f"{player_2}":
            print("HEY NICHT SCHUMMELN!")
            print_area()
            continue

        if user_input_field == str(a):
            a = current_turn
        elif user_input_field == str(b):
            b = current_turn
        elif user_input_field == str(c):
            c = current_turn
        elif user_input_field == str(d):
            d = current_turn
        elif user_input_field == str(e):
            e = current_turn
        elif user_input_field == str(f):
            f = current_turn
        elif user_input_field == str(g):
            g = current_turn
        elif user_input_field == str(h):
            h = current_turn
        elif user_input_field == str(i):
            i = current_turn
        else:
            print("Ungültige Auswahl. Versuche es erneut.")
            print_area()
            continue

        print_area()
        current_turn = f"{player_2}" if current_turn == f"{player_1}" else f"{player_1}"

    last_turn = f"{player_2}" if current_turn == f"{player_1}" else f"{player_1}"
    print(f"Spiel beendet!\n({last_turn}) HAT GEWONNEN!!!")

elif number_of_players == "1":
    print("DU WIRST NIE GEWINNEN!")
    print_area()

    current_turn = f"{player_1}"
    while not (tie() or has_won(f"{player_1}") or has_won(f"{player_2}")):
        if current_turn == f"{player_1}":
            user_input_field = input(f"Wähle ein Feld aus ({current_turn}): ")

            if user_input_field == f"{player_1}" or user_input_field == f"{player_2}":
                print("HEY NICHT SCHUMMELN!")
                print_area()
                continue

            if user_input_field == str(a):
                a = current_turn
            elif user_input_field == str(b):
                b = current_turn
            elif user_input_field == str(c):
                c = current_turn
            elif user_input_field == str(d):
                d = current_turn
            elif user_input_field == str(e):
                e = current_turn
            elif user_input_field == str(f):
                f = current_turn
            elif user_input_field == str(g):
                g = current_turn
            elif user_input_field == str(h):
                h = current_turn
            elif user_input_field == str(i):
                i = current_turn
            else:
                print("Ungültige Auswahl. Versuche es erneut.")
                print_area()
                continue
        else:
            print("Der Computer macht seinen Zug...")
            computer()

        print_area()
        current_turn = f"{player_2}" if current_turn == f"{player_1}" else f"{player_1}"
        last_turn = f"{player_2}" if current_turn == f"{player_1}" else f"{player_1}"

    if tie() == True:
          print("Unentschieden!")
    else:
        print(f"Spiel beendet!\n({last_turn}) HAT GEWONNEN!!!")