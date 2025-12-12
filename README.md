<div align="center">

# 🎲 Linear Congruential Generator (LCG)

### Generator pseudolosowych liczb z wizualizacją

![Python](https://img.shields.io/badge/Python-3.x-blue.svg)
![Tkinter](https://img.shields.io/badge/GUI-Tkinter-green.svg)
![License](https://img.shields.io/badge/license-MIT-orange.svg)

</div>

---

## 📋 Spis treści

- [Opis projektu](#-opis-projektu)
- [Czym jest LCG?](#-czym-jest-lcg)
- [Struktura projektu](#-struktura-projektu)
- [Jak działa algorytm?](#-jak-działa-algorytm)
- [Instalacja i uruchomienie](#-instalacja-i-uruchomienie)
- [Przykładowa wizualizacja](#-przykładowa-wizualizacja)

---

## 🎯 Opis projektu

Ten projekt demonstruje działanie **Linear Congruential Generator** (LCG) - jednego z najprostszych algorytmów do generowania pseudolosowych liczb. Projekt zawiera zarówno uproszczoną interpretację algorytmu, jak i pełną implementację z wizualizacją graficzną.

---

## 🔢 Czym jest LCG?

**Linear Congruential Generator** to algorytm generujący ciąg pseudolosowych liczb według wzoru:

```
X(n+1) = (a × X(n) + c) mod m
```

gdzie:
- **X(n)** - aktualna liczba w sekwencji
- **a** - mnożnik (multiplier)
- **c** - przyrost (increment)
- **m** - moduł (modulus)

W naszej implementacji używamy następujących parametrów:
- **a = 9301**
- **c = 49297**
- **m = 233280**

---

## 📁 Struktura projektu

```
LINEAR_CONGRUENTIAL_GENERATOR/
│
├── main.py                  # Główny program z wizualizacją
├── my_interpetation.py      # Uproszczona interpretacja algorytmu
└── README.md                # Ten plik
```

### 📄 Pliki w projekcie

#### 1️⃣ `my_interpetation.py`

<img src="public/interpretation_diagram.png" alt="Schemat działania" width="400">

**Prymitywny kod demonstrujący schemat działania LCG:**

```python
def rnd(randnum) -> int:
    randnum = (randnum * 5 + 32)
    return randnum
```

Ten plik pokazuje **podstawową ideę** algorytmu:
- ✅ Bierzemy liczbę startową (seed)
- ✅ Przekształcamy ją według wzoru
- ✅ Wynik staje się kolejną liczbą
- ✅ Proces powtarzamy wielokrotnie

**Przykład działania:**
```
Start: 3
Iteracja 1: 3 × 5 + 32 = 47
Iteracja 2: 47 × 5 + 32 = 267
Iteracja 3: 267 × 5 + 32 = 1367
```

---

#### 2️⃣ `main.py`

**Pełna implementacja z wizualizacją graficzną!**

Program:
- 🎨 Tworzy **wizualną prezentację** działania algorytmu
- 🖼️ Otwiera okno z graficzną interpretacją
- ⬛⬜ Przedstawia wygenerowane liczby jako **odcienie szarości** (czarny-biały)
- 🎲 Każda wygenerowana liczba jest przekształcana na wartość koloru od 0 (czarny) do 255 (biały)

**Kluczowe funkcje:**

```python
def rnd(s) -> int: 
    s = (s * 9301 + 49297) % 233280
    return s
```

**Wizualizacja:**
- Użytkownik wybiera ilość rzędów (3-64)
- Program generuje siatkę kolorów N×N
- Każdy kwadrat reprezentuje jedną pseudolosową liczbę
- Im wyższa wartość, tym jaśniejszy odcień szarości

---

## 🚀 Instalacja i uruchomienie

### Wymagania:
```bash
Python 3.x
tkinter (wbudowane w Python)
```

### Uruchomienie programu głównego:

```bash
python main.py
```

**Następnie:**
1. Podaj ilość rzędów (3-64)
2. Program wygeneruje sekwencję pseudolosowych liczb
3. Otworzy się okno z wizualizacją

### Uruchomienie interpretacji:

```bash
python my_interpetation.py
```

---

## 🎨 Przykładowa wizualizacja

Program tworzy siatkę, gdzie każdy kwadrat to wizualna reprezentacja wygenerowanej liczby:

<table>
<tr>
<td bgcolor="#1a1a1a">⬛</td>
<td bgcolor="#4d4d4d">◼️</td>
<td bgcolor="#808080">◾</td>
<td bgcolor="#b3b3b3">◽</td>
</tr>
<tr>
<td bgcolor="#e6e6e6">⬜</td>
<td bgcolor="#333333">⬛</td>
<td bgcolor="#999999">◾</td>
<td bgcolor="#666666">◼️</td>
</tr>
</table>

**Konwersja liczby na kolor:**
```python
intensity = int((losowa_liczba / highest) * 255)
hex_col = f"#{intensity:02x}{intensity:02x}{intensity:02x}"
```

- Liczba **0** → `#000000` (czarny)
- Liczba **116640** → `#808080` (szary)
- Liczba **233280** → `#ffffff` (biały)

---

## 🔍 Ciekawostki

- 🎲 LCG był używany w starszych wersjach generatorów liczb losowych
- ⚡ Jest bardzo szybki, ale nie nadaje się do zastosowań kryptograficznych
- 🔄 Sekwencja zawsze się powtarza po określonej liczbie iteracji (okres)
- 🌱 Ta sama liczba startowa (seed) zawsze daje tę samą sekwencję

---

## 📝 Licencja

MIT License - możesz swobodnie używać i modyfikować kod.

---

<div align="center">

**Stworzony z ❤️ do nauki algorytmów pseudolosowych**

[⬆ Powrót do góry](#-linear-congruential-generator-lcg)

</div>