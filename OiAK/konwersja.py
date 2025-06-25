def u2_na_dziesietny(liczba, bity=32):
    # Konwersja liczby z U2 na liczbe w systemie dziesietnym
    if liczba & (1 << (bity - 1)):
        return liczba - (1 << bity)
    else:
        return liczba


def dziesietny_na_u2(liczba, bity=32):
    # Konwersja liczby całkowitej w systemie dziesietnym na U2
    return liczba & ((1 << bity) - 1)

