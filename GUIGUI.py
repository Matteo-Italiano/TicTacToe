import tkinter as tk


a, b, c,= 1, 2, 3,
d, e, f,= 4, 5, 6,
g, h, i = 7, 8, 9

current_turn = "X"  

player_1 = "X"
player_2 = "O"

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


def disable_all_buttons():
    for button in buttons:
        button.config(state="disabled")

def button_input_changer(button, field_var_name):
    global current_turn, label, window
    

    if isinstance(globals()[field_var_name], int):
        globals()[field_var_name] = current_turn  
        button.config(text=current_turn) 
        
        if has_won(current_turn):
            label.config(text=f"Spiel beendet! {current_turn} hat gewonnen!")
            disable_all_buttons()
        elif tie():
            label.config(text="Unentschieden! Kein freies Feld mehr.")
            disable_all_buttons()
        else:
            current_turn = "O" if current_turn == "X" else "X"
            label.config(text=f"Wähle ein Feld aus ({current_turn}):")
  

def play_and_grid():
    global label, buttons, window

    window = tk.Tk()
    window.title("Tic-Tac-Toe")

    label = tk.Label(window, text=f"Wähle ein Feld aus ({current_turn}):", font=("Arial", 16))
    label.grid(row=0, column=0, columnspan=3, pady=10)

    
    buttons = []
    
    button_a = tk.Button(window, text=f"{a}", width=10, height=5, command=lambda: button_input_changer(button_a, 'a'), bg="white", fg="black")
    button_a.grid(row=1, column=0, padx=5, pady=5)
    buttons.append(button_a)
    
    button_b = tk.Button(window, text=f"{b}", width=10, height=5, command=lambda: button_input_changer(button_b, 'b'), bg="white", fg="black")
    button_b.grid(row=1, column=1, padx=5, pady=5)
    buttons.append(button_b)
    
    button_c = tk.Button(window, text=f"{c}", width=10, height=5, command=lambda: button_input_changer(button_c, 'c'), bg="white", fg="black")
    button_c.grid(row=1, column=2, padx=5, pady=5)
    buttons.append(button_c)
    
    button_d = tk.Button(window, text=f"{d}", width=10, height=5, command=lambda: button_input_changer(button_d, 'd'), bg="white", fg="black")
    button_d.grid(row=2, column=0, padx=5, pady=5)
    buttons.append(button_d)
    
    button_e = tk.Button(window, text=f"{e}", width=10, height=5, command=lambda: button_input_changer(button_e, 'e'), bg="white", fg="black")
    button_e.grid(row=2, column=1, padx=5, pady=5)
    buttons.append(button_e)
    
    button_f = tk.Button(window, text=f"{f}", width=10, height=5, command=lambda: button_input_changer(button_f, 'f'), bg="white", fg="black")
    button_f.grid(row=2, column=2, padx=5, pady=5)
    buttons.append(button_f)
    
    button_g = tk.Button(window, text=f"{g}", width=10, height=5, command=lambda: button_input_changer(button_g, 'g'), bg="white", fg="black")
    button_g.grid(row=3, column=0, padx=5, pady=5)
    buttons.append(button_g)
    
    button_h = tk.Button(window, text=f"{h}", width=10, height=5, command=lambda: button_input_changer(button_h, 'h'), bg="white", fg="black")
    button_h.grid(row=3, column=1, padx=5, pady=5)
    buttons.append(button_h)
    
    button_i = tk.Button(window, text=f"{i}", width=10, height=5, command=lambda: button_input_changer(button_i, 'i'), bg="white", fg="black")
    button_i.grid(row=3, column=2, padx=5, pady=5)
    buttons.append(button_i)

    label = tk.Label(window, text="Willst du nochmal Spielen",  font=("Arial", 16))
    label.grid(row=4, column=0, padx=5, pady=5)
    
    window.mainloop()

play_and_grid()

 
