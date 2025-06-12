def u2_na_wartosc(liczba, bity=32):
    # Konwersja liczby z U2 na wartość ze znakiem
    if liczba & (1 << (bity - 1)):
        return liczba - (1 << bity)
    else:
        return liczba

def wartosc_na_u2(liczba, bity=32):
    # Konwersja liczby całkowitej na U2
    return liczba & ((1 << bity) - 1)

def dzielenie(dzielna, dzielnik, bity=32):
    # Konwersja argumentów z U2 na wartości całkowite ze znakiem
    dzielna_int = u2_na_wartosc(dzielna, bity)
    dzielnik_int = u2_na_wartosc(dzielnik, bity)
    if dzielnik_int == 0:
        raise ZeroDivisionError("Dzielenie przez zero!")

    dzielna_abs = abs(dzielna_int)
    dzielnik_abs = abs(dzielnik_int)

    iloraz = 0
    reszta = 0
    bity_dzielnej = dzielna_abs.bit_length()

    # Przetwarzanie bitów dzielnej od najwyższego do najniższego
    for i in range(bity_dzielnej - 1, -1, -1):
        # 1. Przesunięcie reszty w lewo i dołączenie kolejnego bitu dzielnej:
        #    Reszta zostaje przesunięta o jeden bit w lewo, a do najmłodszego bitu dołączany jest kolejny bit z dzielnej.
        reszta = (reszta << 1) | ((dzielna_abs >> i) & 1)

        # 2. Bezwarunkowe odjęcie dzielnika:
        #    Niezależnie od wartości reszty, od reszty odejmowany jest dzielnik.
        reszta -= dzielnik_abs

        # 3. Sprawdzenie poprawności odejmowania:
        #    Jeśli wynik odejmowania jest nieujemny, operacja była poprawna i zapisujemy 1 w ilorazie.
        #    Jeśli wynik jest ujemny, przywracamy poprzednią wartość reszty przez dodanie dzielnika i zapisujemy 0.
        if reszta >= 0:
            # 4. Zapisanie bitu ilorazu:
            #    Skoro odejmowanie się udało, zapisujemy 1 na ostatniej pozycji ilorazu.
            iloraz = (iloraz << 1) | 1
        else:
            # Przywrócenie reszty i zapisanie 0 w ilorazie
            reszta += dzielnik_abs
            iloraz = (iloraz << 1) | 0

        # 5. Powtórzenie procesu dla kolejnego bitu dzielnej:
        #    Proces powtarza się dla wszystkich bitów dzielnej.

    # Korekta końcowej reszty, jeśli jest ujemna (ale nie powinna wystąpić)
    if reszta < 0:
        reszta += dzielnik_abs

    # Korekta znaku wyniku
    if (dzielna_int < 0) != (dzielnik_int < 0):
        iloraz = -iloraz
    if dzielna_int < 0:
        reszta = -reszta

    # Konwersja wyniku do U2 (uzupełnień do dwóch)
    iloraz_u2 = wartosc_na_u2(iloraz, bity)
    reszta_u2 = wartosc_na_u2(reszta, bity)

    return iloraz_u2, reszta_u2
