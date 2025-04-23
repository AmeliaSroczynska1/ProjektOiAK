def dzielenie(dzielna, dzielnik, podstawa=2, iteracje=10):
    """
    Poprawiona implementacja algorytmu SRT (radix-2) z polskimi nazwami zmiennych.

    Args:
        dzielna (float): Liczba dzielona.
        dzielnik (float): Liczba przez którą dzielimy.
        podstawa (int): Podstawa systemu liczbowego (domyślnie 2).
        iteracje (int): Liczba iteracji do wykonania.

    Returns:
        tuple: Iloraz i reszta po wykonaniu algorytmu.
    """
    if dzielnik == 0:
        raise ValueError("Dzielenie przez zero jest niedozwolone.")

    # Inicjalizacja zmiennych
    reszta_czesciowa = dzielna
    iloraz = 0

    for _ in range(iteracje):
        # Wybór cyfry ilorazu na podstawie reszty częściowej
        if reszta_czesciowa >= dzielnik / 2:
            cyfra_ilorazu = 1
        elif reszta_czesciowa <= -dzielnik / 2:
            cyfra_ilorazu = -1
        else:
            cyfra_ilorazu = 0

        # Aktualizacja ilorazu
        iloraz = iloraz * podstawa + cyfra_ilorazu

        # Obliczenie nowej reszty częściowej
        reszta_czesciowa = podstawa * reszta_czesciowa - cyfra_ilorazu * dzielnik

    # Normalizacja ilorazu do postaci zmiennoprzecinkowej
    iloraz_float = iloraz / (podstawa ** iteracje)
    return iloraz_float, reszta_czesciowa

