import konwersja


def dzielenie(dzielna, dzielnik, bity=32):
    dzielna_int = konwersja.u2_na_dziesietny(dzielna, bity)
    dzielnik_int = konwersja.u2_na_dziesietny(dzielnik, bity)

    dzielna_abs = abs(dzielna_int)
    dzielnik_abs = abs(dzielnik_int)

    iloraz = 0
    reszta = 0
    bity_dzielnej = dzielna_abs.bit_length()

    for i in range(bity_dzielnej - 1, -1, -1):
        # 1. Przesunięcie reszty w lewo i dołączenie kolejnego bitu dzielnej:
        #    Reszta zostaje przesunięta o jeden bit w lewo, a do najmłodszego bitu dołączany jest kolejny bit z dzielnej
        reszta = (reszta << 1) | ((dzielna_abs >> i) & 1)

        # 2. Warunkowe wykonanie operacji arytmetycznej:
        #    Jeśli poprzednia reszta była nieujemna, odejmujemy dzielnik od reszty.
        #    Jeśli poprzednia reszta była ujemna, dodajemy dzielnik do reszty.
        if reszta >= 0:
            reszta -= dzielnik_abs
            # 3. Zapisanie bitu ilorazu:
            #    Jeśli po operacji reszta jest nieujemna, do ilorazu zapisujemy 1.
            if reszta >= 0:
                iloraz = (iloraz << 1) | 1
            else:
                iloraz = (iloraz << 1) | 0
        else:
            reszta += dzielnik_abs
            # 3. Zapisanie bitu ilorazu:
            #    Jeśli po operacji reszta jest nieujemna, do ilorazu zapisujemy 1.
            if reszta >= 0:
                iloraz = (iloraz << 1) | 1
            else:
                iloraz = (iloraz << 1) | 0

        # 4. Powtórzenie procesu dla kolejnego bitu dzielnej:
        #    Proces powtarza się dla wszystkich bitów dzielnej.

    # 5. Korekta końcowej reszty (opcjonalnie):
    #    Po zakończeniu wszystkich kroków, jeśli końcowa reszta jest ujemna, należy dodać do niej dzielnik.
    if reszta < 0:
        reszta += dzielnik_abs

    # Korekta znaku wyniku
    if (dzielna_int < 0) != (dzielnik_int < 0):
        iloraz = -iloraz
    if dzielna_int < 0:
        reszta = -reszta

    # Konwersja wyniku do U2 (uzupełnień do dwóch)
    iloraz_u2 = konwersja.dziesietny_na_u2(iloraz, bity)
    reszta_u2 = konwersja.dziesietny_na_u2(reszta, bity)

    return iloraz_u2, reszta_u2

