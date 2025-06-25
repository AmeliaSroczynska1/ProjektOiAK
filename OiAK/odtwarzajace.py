import konwersja


def dzielenie(dzielna, dzielnik, bity=32):
    # Konwersja argumentów z U2 na wartości całkowite ze znakiem
    dzielna_int = konwersja.u2_na_dziesietny(dzielna, bity)
    dzielnik_int = konwersja.u2_na_dziesietny(dzielnik, bity)

    dzielna_abs = abs(dzielna_int)
    dzielnik_abs = abs(dzielnik_int)

    iloraz = 0
    reszta = 0
    bity_dzielnej = dzielna_abs.bit_length()

    # Przetwarzanie bitów dzielnej od najwyższego do najniższego
    for i in range(bity_dzielnej - 1, -1, -1):
        # 1. Przesunięcie reszty w lewo i pobranie kolejnego bitu dzielnej:
        #    Reszta zostaje przesunięta o jeden bit w lewo, a do najmłodszego bitu dołączany jest kolejny bit z dzielnej.
        reszta = (reszta << 1) | ((dzielna_abs >> i) & 1)

        # 2. Próba odjęcia dzielnika od reszty:
        #    Sprawdzamy, czy reszta po przesunięciu i dodaniu nowego bitu jest większa lub równa dzielnikowi.
        #    Jeśli tak, odejmowanie będzie możliwe.
        if reszta >= dzielnik_abs:
            # 3. Aktualizacja reszty:
            #    Odejmujemy dzielnik od reszty, bo odejmowanie się udało.
            reszta -= dzielnik_abs
            # 4. Zapisanie bitu ilorazu:
            #    Skoro odejmowanie się udało, zapisujemy 1 na ostatniej pozycji ilorazu.
            iloraz = (iloraz << 1) | 1
        else:
            # 3. Aktualizacja reszty:
            #    Odejmowanie się nie udało, reszta pozostaje bez zmian.
            # 4. Zapisanie bitu ilorazu:
            #    Skoro odejmowanie się nie udało, zapisujemy 0 na ostatniej pozycji ilorazu.
            iloraz = (iloraz << 1) | 0
        # 5. Powtórzenie procesu dla kolejnego bitu dzielnej:
        #    Proces powtarza się dla każdego bitu dzielnej.

    # Korekta znaku wyniku
    if (dzielna_int < 0) != (dzielnik_int < 0):
        iloraz = -iloraz
    if dzielna_int < 0:
        reszta = -reszta

    # Konwersja wyniku do U2 (uzupełnień do dwóch)
    iloraz_u2 = konwersja.dziesietny_na_u2(iloraz, bity)
    reszta_u2 = konwersja.dziesietny_na_u2(reszta, bity)

    return iloraz_u2, reszta_u2
