#------------------------------------
# MOJA INTERPETACJA  (prymitywny kod aby wytłumaczyć schemat działania)
def rnd(randnum) -> int:
    
    randnum = (randnum * 5 + 32) # losowy inny schemat losowanych liczb
    
    return randnum

# liczba powtorzen
t = 3

#pierwsza liczba od ktorej sie zaczyna
start = 3

wynik = start

for i in range(t):
    # 1 wejscie - wynik = 3
    # 2 wejscie wynik - 47
    losowa_piewrsza = rnd(wynik)
    wynik = losowa_piewrsza
    print(wynik)
    
    
# MOJA INTERPETACJA    
#------------------------------------