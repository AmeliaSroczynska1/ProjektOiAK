import time

# Parametry LCG
modulo = 2 ** 32
a = 1664525
c = 1013904223

# Inicjalizacja ziarna na podstawie czasu systemowego
ziarno = int(time.time() * 1000) & 0xFFFFFFFF

def losuj():
    global ziarno
    ziarno = (a * ziarno + c) % modulo
    # Liczba całkowita ze znakiem z przedziału -1000 do 1000
    wartosc = ziarno % 2001  # 0-2000
    return wartosc - 1000    # -1000 do 1000
