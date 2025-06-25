def zapisz_czas_odtwarzajace(ile_razy, czas, precyzja):
    with open("czasy_wykonywania.txt", "a", encoding="utf-8") as plik:
        plik.write(f"Czas dzielenia odtwarzającego (po {ile_razy} powtórzeń) = {czas*1000:.{precyzja}f} ms\n")
        plik.write(f"Średni czas jednego dzielenia odtwarzającego = {czas*1000000/ile_razy:.{precyzja}f} micro s\n\n")


def zapisz_czas_nieodtwarzajace(ile_razy, czas, precyzja):
    with open("czasy_wykonywania.txt", "a", encoding="utf-8") as plik:
        plik.write(f"Czas dzielenia nieodtwarzającego (po {ile_razy} powtórzeń) = {czas*1000:.{precyzja}f} ms\n")
        plik.write(f"Średni czas jednego dzielenia nieodtwarzającego = {czas*1000000/ile_razy:.{precyzja}f} micro s\n\n")


def zapisz_wynik(dzielna, dzielnik, iloraz, reszta, bity=32):
    with open("wyniki_dzielenia.txt", "a", encoding="utf-8") as plik:
        plik.write(
            f"Dzielna: {dzielna} | U2: {bin(dzielna & ((1 << bity) - 1))[2:].zfill(bity)}; \n"
            f"Dzielnik: {dzielnik} | U2: {bin(dzielnik & ((1 << bity) - 1))[2:].zfill(bity)}; \n"
            f"Iloraz: {iloraz} | U2: {bin(iloraz & ((1 << bity) - 1))[2:].zfill(bity)}; \n"
            f"Reszta: {reszta} | U2: {bin(reszta & ((1 << bity) - 1))[2:].zfill(bity)}\n\n"
        )
