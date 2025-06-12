import time

import generator_liczb
import nieodtwarzajace
import odtwarzajace
from obsluga_plikow import zapisz_wynik_odtwarzajace, zapisz_wynik_nieodtwarzajace


def generuj_pary(ile):
    dzielne, dzielniki = [], []

    for _ in range(ile):
        dzielna = generator_liczb.losuj()
        dzielnik = generator_liczb.losuj()
        while dzielnik == 0:
            dzielnik = generator_liczb.losuj()
        dzielne.append(dzielna)
        dzielniki.append(dzielnik)
    return dzielne, dzielniki

def sredni_czas():
    powtorzenia = [1, 2, 3]

    # Dla metody odtwarzającej
    for ile_razy in powtorzenia:
        dzielne, dzielniki = generuj_pary(ile_razy)


        print("\nPary liczb (dziesiętnie | binarnie):")
        for i in range(ile_razy):
            print(f"Para {i+1}:")
            print(f"Dzielna: {dzielne[i]} | {bin(dzielne[i])[2:]}")
            print(f"Dzielnik: {dzielniki[i]} | {bin(dzielniki[i])[2:]}\n")


        start = time.perf_counter()
        for i in range(ile_razy):
            odtwarzajace.dzielenie(dzielne[i], dzielniki[i])
        koniec = time.perf_counter()

        czas_odtwarzajace = koniec - start

        print(f"\nCzas dzielenia odtwarzającego (po {ile_razy} powtórzeń) = {czas_odtwarzajace:.4f} s")
        print(f"Średni czas jednego dzielenia odtwarzającego = {czas_odtwarzajace*1000/ile_razy:.8f} ms")

        zapisz_wynik_odtwarzajace(ile_razy, czas_odtwarzajace)

    # Dla metody nieodtwarzającej
    for ile_razy in powtorzenia:
        dzielne, dzielniki = generuj_pary(ile_razy)

        start = time.perf_counter()
        for i in range(ile_razy):
            nieodtwarzajace.dzielenie(dzielne[i], dzielniki[i])
        koniec = time.perf_counter()

        czas_nieodtwarzajace = koniec - start

        print(f"\nCzas dzielenia nieodtwarzającego (po {ile_razy} powtórzeń) = {czas_nieodtwarzajace:.4f} s")
        print(f"Średni czas jednego dzielenia nieodtwarzającego = {czas_nieodtwarzajace*1000/ile_razy:.8f} ms")

        zapisz_wynik_nieodtwarzajace(ile_razy, czas_nieodtwarzajace)

# Menu do wyświetlania w konsolce
def menu():
    dzielna = 0                                         # Inicjalizacja dzielnej
    dzielnik = 0                                        # Inicjalizacja dzielnika
    start = 0                                           # Zmienna do liczenia czasu

    # Wybór czy liczby pisane z klawiatury czy losowe
    print("Witaj w programie do dzielenia liczb!")
    wybor0 = input("Chcesz sam wpisać liczby, ktore program podzieli czy wygenerowac z przedzialu 0-1000 losowe liczby?\n"
                   "1 - Chce wpisac\n"
                   "2 - Losowe\n")

    if wybor0 == "1":
        while True:
            try:
                dzielna = int(input("Podaj dzielna: "))
                break
            except ValueError:
                print("Błąd: Wprowadź liczbę całkowitą!")

        while True:
            try:
                dzielnik = int(input("Podaj dzielnik: "))
                if dzielnik == 0:
                    print("Nie można dzielić przez 0")
                    continue
                break
            except ValueError:
                print("Błąd: Wprowadź liczbę całkowitą!")

    elif wybor0 == "2":
        dzielna = generator_liczb.losuj()
        dzielnik = generator_liczb.losuj()
        while dzielnik == 0:
            dzielnik = generator_liczb.losuj()
    else:
        while wybor0 not in ('1', '2'):
            print("Podałeś nieprawidłowy znak, możesz wybrać tylko 1 lub 2")
            wybor0 = input(
                "\nChcesz sam wpisać liczby, ktore program podzieli czy wygenerowac z przedzialu 0-1000 losowe liczby?\n"
                "1 - Chce wpisac\n"
                "2 - Losowe\n"
            )

    # Wybor metody dzielenia
    wybor1 = input("\nJaką metoda chcesz dzielic?\n"
                   "1 - Odtwarzajaca\n"
                   "2 - Nieodtwarzajaca\n")

    while wybor1 not in ('1', '2'):
        print("Podałeś nieprawidłowy znak, możesz wybrać tylko 1 lub 2")
        wybor1 = input("\nJaką metodą chcesz dzielić?\n"
                       "1 - Odtwarzająca\n"
                       "2 - Nieodtwarzająca\n")

    # Wybor czy liczymy czas
    wybor2 = input("\nCzy chcesz obliczyc tez czas dzielenia? T - tak\n")

    # Wybor ile razy powtarzamy dzielenie
    while True:
        try:
            wybor3 = int(input("\nIle razy chcesz powtorzyc pomiar? "))
            if wybor3 <= 0:
                print("Liczba powtórzeń musi być dodatnia!")
                continue
            break
        except ValueError:
            print("Błąd: Wprowadź liczbę całkowitą!")

    # Start liczenia czasu
    if wybor2 == 'T':
        start = time.perf_counter()

    # Dzielenie określoną liczbę razy
    for i in range(wybor3):
        if wybor1 == '1':
            odtwarzajace.dzielenie(dzielna, dzielnik)
        elif wybor1 == '2':
            nieodtwarzajace.dzielenie(dzielna, dzielnik)

    # Koniec pomiaru czasu i wyświetlenie
    if wybor2 == 'T':
        koniec = time.perf_counter()
        while True:
            try:
                precyzja = int(input("\nIle cyfr po przecinku ma mieć wynik pomiaru czasu? "))
                if precyzja < 0:
                    print("Precyzja musi być liczbą nieujemną!")
                    continue
                break
            except ValueError:
                print("Błąd: Wprowadź liczbę całkowitą!")
        print(f"\nCzas wszystkich dzielen: {(koniec - start):.{precyzja}f} s")
        print(f"Usredniony czas 1 dzielenia: {((koniec - start) / wybor3) * 1000:.{precyzja}f} ms")
