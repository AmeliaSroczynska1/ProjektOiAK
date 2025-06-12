def zapisz_wynik_odtwarzajace(ile_razy, czas):
    with open("wyniki.txt", "a", encoding="utf-8") as plik:
        plik.write(f"Czas dzielenia odtwarzającego (po {ile_razy} powtórzeń) = {czas:.4f} s\n")
        plik.write(f"Średni czas jednego dzielenia odtwarzającego = {czas*1000/ile_razy:.8f} ms\n\n")

def zapisz_wynik_nieodtwarzajace(ile_razy, czas):
    with open("wyniki.txt", "a", encoding="utf-8") as plik:
        plik.write(f"Czas dzielenia nieodtwarzającego (po {ile_razy} powtórzeń) = {czas:.4f} s\n")
        plik.write(f"Średni czas jednego dzielenia nieodtwarzającego = {czas*1000/ile_razy:.8f} ms\n\n")
