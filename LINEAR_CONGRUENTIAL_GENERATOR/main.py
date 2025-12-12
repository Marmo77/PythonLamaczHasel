# STRUKTURALNE PODEJŚCIE DO LCG

import random
import tkinter as tk

def rnd(s) -> int: 
    
    s = (s * 9301 + 49297) % 233280
    
    return s
    # return s / 233280,0


lowest = 0 # as black
highest = 233280 # as white

# # random first number
first_num  = random.randint(lowest, highest)

# UŻYTKOWNIK WYBIERA ILOSC RZĘDÓW
while True:
    
    try:
        ROWS = int(input("Podaj ilość rzędów (3-64)\n:"))
        # print(ROWS)
        if 64 >= ROWS >= 3:
            break
        else:
            print("-- Nie podano liczby z zakresu --")
    except ValueError:
        print("-- Nie podano poprawnej liczby --\n")
        
squares = ROWS * ROWS

wynik = 0

board = []


for _ in range(squares):
    
    losowa_liczba = rnd(first_num)
    
    wynik = losowa_liczba
    first_num = wynik
    
    #zamiana na hex
    intensity = int((losowa_liczba / highest) * 255)
    
    hex_col = f"#{intensity:02x}{intensity:02x}{intensity:02x}"
    
    board.append(hex_col)
    

print("------------------------- TABLICA WYLOSOWANYCH KOLORÓW ------------------------")
print(board)
print("-------------- WIZUALIZACJA POWINNA OTWORZYĆ SIĘ W NOWYM OKNIE ! --------------")
# WIZUALIZACJA WYNIKÓW

root = tk.Tk()
height = 640
width = 640
screenwidth = root.winfo_width()
screenheight = root.winfo_height()
root.geometry(f"{(width+width//2)}x{(height+ height//4)}")
root.resizable(width=True, height=True)

#tekst
label = tk.Label(root, text="--- Wizualiazacja losowych liczb ---")
info = tk.Label(root, text=f"Liczba elementów: {len(board)}")
label.pack()
info.pack()

#kwadrat
# square = tk.Frame(root, width=200, height=200, bg="#d0d0d0")
# square.pack(padx=4, pady=4)
# square.pack_propagate(False)

# SIATKA dla gridów
grid_frame = tk.Frame(root)
grid_frame.pack()

for i, color in enumerate(board):
    r = i // ROWS # numer rzędu
    c = i % ROWS # numer kolumny
    
    frame = tk.Frame(grid_frame, width=(width/ROWS), height=(height/ROWS), bg=color) # tworzenie frame'a z kolorem
    frame.grid(row=r,column=c) # dodawanie frame'a do grida na odopowiednie pozycje
    frame.pack_propagate(False)
if __name__ == "__main__":
    root.mainloop()


