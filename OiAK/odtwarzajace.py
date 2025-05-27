
def dzielenie(dzielna, dzielnik):
    iloraz = 0
    reszta = 0
    bity = dzielna.bit_length()

    for i in range(bity - 1, -1, -1):
        reszta = (reszta << 1) | ((dzielna >> i) & 1)
        iloraz <<= 1
        poprzednia_reszta = reszta
        reszta -= dzielnik
        if reszta >= 0:
            iloraz |= 1
        else:
            reszta = poprzednia_reszta  # Przywracamy wartość reszty

    print(f"Dzielenie odtwarzające: Iloraz = {iloraz}, Reszta = {reszta}")
