# OBIETKOWE PODEJŚCIE DO LCG

import tkinter as tk

class LCG:
    
    
    lowest = 0 # black
    highest = 233280 # white
    board = []  # tablica z wynikami
    
    def generator(self, s) -> int:
        
        s = (s * 9301 + 49297) % 233280
        
        return s
    
    
    def tablica_wynikow(self, ROWS, start_num):
        
        for _ in range(ROWS * ROWS): #aby wyszedł kwadrat w wizualizacji
            
            losowa_liczba = self.generator(start_num)
            
            wynik = losowa_liczba
            start_num = wynik
            
            self.board.append(losowa_liczba)
            
        return self.board
    
    def tablica_na_hexy(self, tablica) -> list:
        tablica_hexow = []
        
        for element in tablica:
            intensity = int((element / self.highest) * 255)
            
            hex_color = f"#{intensity:02x}{intensity:02x}{intensity:02x}" # zamiana liczby na odcien szarości
            
            tablica_hexow.append(hex_color)
            
        return tablica_hexow
        
class App:
    def __init__(self, height: int, width):
        self.height = height
        self.width = width
        
        
        #teksty
        
    def pokaz_wizualizacje(self, tablica_hexow):
        
        root = tk.Tk()
        root.geometry(f"{(self.width+self.width//2)}x{(self.height+ self.height//4)}")
        root.resizable(width=True, height=True)
        
        #tekst
        label = tk.Label(root, text="--- Wizualiazacja losowych liczb ---")
        info = tk.Label(root, text=f"Liczba elementów: {len(tablica_hexow)}")
        label.pack()
        info.pack()
        
        #siatka do gridów
        grid_frame = tk.Frame(root)
        grid_frame.pack()
        
        #dodawanie hexów do tablicy
        
        for i, color in enumerate(tablica_hexow):
            r = i // ROWS # numer rzędu
            c = i % ROWS # numer kolumny
            
            frame = tk.Frame(grid_frame, width=(self.width/ROWS), height=(self.height/ROWS), bg=color) # tworzenie frame'a z kolorem
            frame.grid(row=r,column=c) # dodawanie frame'a do grida na odopowiednie pozycje
            frame.pack_propagate(False)
        
        # uruchomienie aplikacji
        root.mainloop()
        
if __name__ == "__main__":
    
    lcg = LCG() 
    
    while True:
        try:
            ROWS = int(input("Podaj ilość rzędów (3-64)\n:"))
            if 64 >= ROWS >= 3:
                while True:
                    try:
                        start_num = int(input(f"Podaj Liczbę rozpoczęcia ({lcg.lowest}-{lcg.highest})\n: "))
                        if lcg.highest >= start_num >= lcg.lowest:
                            break
                        print("--Podano liczbe z poza zakresu--")
                    except ValueError:
                        print("--- Podano błędną wartośc ---")
                break
            else:
                print("-- Nie podano liczby z zakresu --")
        except ValueError:
            print("-- Nie podano poprawnej liczby --\n")
            
    tablica_wynikow = lcg.tablica_wynikow(ROWS, start_num)
    
    hexy = lcg.tablica_na_hexy(tablica_wynikow)
    print("---------------------------------- TABLICA HEXÓW ----------------------------------")
    print(hexy)
    print("-----------------------------------------------------------------------------------")
    
    app = App(640,640)
    
    print("-------------- ! WIZUALIZACJA POWINNA OTWORZYĆ SIE W NOWYM OKNIE !-----------------")
    app.pokaz_wizualizacje(hexy)
    