
def dzielenie(dzielna, dzielnik):
    iloraz = 0
    reszta = 0
    bity = dzielna.bit_length()

    for i in range(bity - 1, -1, -1):
        # 1. Shift left reszta i dołącz kolejny bit z dividend
        reszta = (reszta << 1) | ((dzielna >> i) & 1)

        # 2. Decyzja: jeśli poprzednia reszta ≥ 0, to odejmujemy; inaczej dodajemy
        if reszta >= 0:
            reszta -= dzielnik
        else:
            reszta += dzielnik

        # 3. Ustawienie bitu ilorazu: po odejmowaniu/dodawaniu patrzymy na nowy znak reszty
        if reszta >= 0:
            iloraz = (iloraz << 1) | 1
        else:
            iloraz <<= 1

    # 4. Korekta końcowej reszty jeśli jest ujemna
    if reszta < 0:
        reszta += dzielnik

 #   print(f"Dzielenie nieodtwarzające: Iloraz = {iloraz}, Reszta = {reszta}")

