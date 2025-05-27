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
    # Liczba całkowita z przedziału 0-1000
    return int(ziarno % 1001)
