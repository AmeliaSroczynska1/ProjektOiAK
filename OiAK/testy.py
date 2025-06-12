import time

import generator_liczb
import nieodtwarzajace
import odtwarzajace
from obsluga_plikow import (
    zapisz_wynik_odtwarzajace,
    zapisz_wynik_nieodtwarzajace,
    zapisz_dzielenie
)

def generuj_pary(ile, bity=32):
    dzielne, dzielniki = [], []
    for _ in range(ile):
        dzielna = generator_liczb.losuj()
        dzielnik = generator_liczb.losuj()
        while dzielnik == 0:
            dzielnik = generator_liczb.losuj()
        dzielne.append(dzielna & ((1 << bity) - 1))
        dzielniki.append(dzielnik & ((1 << bity) - 1))
    return dzielne, dzielniki

def sredni_czas():
    powtorzenia = [1, 2, 3]  # Przykładowe wartości do testów
    bity = 32

    for ile_razy in powtorzenia:
        dzielne, dzielniki = generuj_pary(ile_razy, bity)

        print("\nPary liczb (dziesiętnie | system U2):")
        for i in range(ile_razy):
            print(f"Para {i+1}:")
            print(f"Dzielna: {odtwarzajace.u2_na_wartosc(dzielne[i], bity)} | {bin(dzielne[i])[2:].zfill(bity)}")
            print(f"Dzielnik: {odtwarzajace.u2_na_wartosc(dzielniki[i], bity)} | {bin(dzielniki[i])[2:].zfill(bity)}\n")

        # Dla metody odtwarzającej
        start = time.perf_counter()
        for i in range(ile_razy):
            iloraz_u2, reszta_u2 = odtwarzajace.dzielenie(dzielne[i], dzielniki[i], bity)
            # Zapis każdej operacji dzielenia do pliku
            zapisz_dzielenie(
                odtwarzajace.u2_na_wartosc(dzielne[i], bity),
                odtwarzajace.u2_na_wartosc(dzielniki[i], bity),
                odtwarzajace.u2_na_wartosc(iloraz_u2, bity),
                odtwarzajace.u2_na_wartosc(reszta_u2, bity),
                bity
            )
        koniec = time.perf_counter()

        czas_odtwarzajace = koniec - start

        print(f"Czas dzielenia odtwarzającego (po {ile_razy} powtórzeń) = {czas_odtwarzajace:.4f} s")
        print(f"Średni czas jednego dzielenia odtwarzającego = {czas_odtwarzajace*1000/ile_razy:.8f} ms\n")

        zapisz_wynik_odtwarzajace(ile_razy, czas_odtwarzajace)

        # Dla metody nieodtwarzającej
        start = time.perf_counter()
        for i in range(ile_razy):
            iloraz_u2, reszta_u2 = nieodtwarzajace.dzielenie(dzielne[i], dzielniki[i], bity)
            zapisz_dzielenie(
                nieodtwarzajace.u2_na_wartosc(dzielne[i], bity),
                nieodtwarzajace.u2_na_wartosc(dzielniki[i], bity),
                nieodtwarzajace.u2_na_wartosc(iloraz_u2, bity),
                nieodtwarzajace.u2_na_wartosc(reszta_u2, bity),
                bity
            )
        koniec = time.perf_counter()

        czas_nieodtwarzajace = koniec - start

        print(f"Czas dzielenia nieodtwarzającego (po {ile_razy} powtórzeń) = {czas_nieodtwarzajace:.4f} s")
        print(f"Średni czas jednego dzielenia nieodtwarzającego = {czas_nieodtwarzajace*1000/ile_razy:.8f} ms\n")

        zapisz_wynik_nieodtwarzajace(ile_razy, czas_nieodtwarzajace)

def menu():
    bity = 32

    print("Witaj w programie do dzielenia liczb w systemie U2!")
    wybor0 = input("Chcesz sam wpisać liczby, czy wygenerować losowe?\n"
                   "1 - Chcę wpisać\n"
                   "2 - Losowe\n")

    if wybor0 == "1":
        while True:
            try:
                dzielna = int(input("Podaj dzielną (może być ujemna): "))
                break
            except ValueError:
                print("Błąd: Wprowadź liczbę całkowitą!")

        while True:
            try:
                dzielnik = int(input("Podaj dzielnik (może być ujemny, ale nie zero!): "))
                if dzielnik == 0:
                    print("Nie można dzielić przez 0")
                    continue
                break
            except ValueError:
                print("Błąd: Wprowadź liczbę całkowitą!")

        dzielna_u2 = dzielna & ((1 << bity) - 1)
        dzielnik_u2 = dzielnik & ((1 << bity) - 1)

    elif wybor0 == "2":
        dzielna = generator_liczb.losuj()
        dzielnik = generator_liczb.losuj()
        while dzielnik == 0:
            dzielnik = generator_liczb.losuj()
        dzielna_u2 = dzielna & ((1 << bity) - 1)
        dzielnik_u2 = dzielnik & ((1 << bity) - 1)
        print(f"Wylosowana dzielna: {dzielna} | {bin(dzielna_u2)[2:].zfill(bity)}")
        print(f"Wylosowany dzielnik: {dzielnik} | {bin(dzielnik_u2)[2:].zfill(bity)}")
    else:
        while wybor0 not in ('1', '2'):
            print("Podałeś nieprawidłowy znak, możesz wybrać tylko 1 lub 2")
            wybor0 = input(
                "\nChcesz sam wpisać liczby, czy wygenerować losowe?\n"
                "1 - Chcę wpisać\n"
                "2 - Losowe\n"
            )

    # Wybór metody dzielenia
    wybor1 = input("\nJaką metodą chcesz dzielić?\n"
                   "1 - Odtwarzająca\n"
                   "2 - Nieodtwarzająca\n")

    while wybor1 not in ('1', '2'):
        print("Podałeś nieprawidłowy znak, możesz wybrać tylko 1 lub 2")
        wybor1 = input("\nJaką metodą chcesz dzielić?\n"
                       "1 - Odtwarzająca\n"
                       "2 - Nieodtwarzająca\n")

    # Czy liczymy czas?
    wybor2 = input("\nCzy chcesz obliczyć też czas dzielenia? T/N - Tak/Nie\n")

    # Ile razy powtarzamy dzielenie?
    while True:
        try:
            wybor3 = int(input("\nIle razy chcesz powtórzyć pomiar? "))
            if wybor3 <= 0:
                print("Liczba powtórzeń musi być dodatnia")
                continue
            break
        except ValueError:
            print("Wprowadź liczbę całkowitą")

    # Start liczenia czasu
    if wybor2 == 'T':
        start = time.perf_counter()

    # Dzielenie określoną liczbę razy
    for i in range(wybor3):
        if wybor1 == '1':
            iloraz_u2, reszta_u2 = odtwarzajace.dzielenie(dzielna_u2, dzielnik_u2, bity)
            zapisz_dzielenie(
                odtwarzajace.u2_na_wartosc(dzielna_u2, bity),
                odtwarzajace.u2_na_wartosc(dzielnik_u2, bity),
                odtwarzajace.u2_na_wartosc(iloraz_u2, bity),
                odtwarzajace.u2_na_wartosc(reszta_u2, bity),
                bity
            )
        elif wybor1 == '2':
            iloraz_u2, reszta_u2 = nieodtwarzajace.dzielenie(dzielna_u2, dzielnik_u2, bity)
            zapisz_dzielenie(
                nieodtwarzajace.u2_na_wartosc(dzielna_u2, bity),
                nieodtwarzajace.u2_na_wartosc(dzielnik_u2, bity),
                nieodtwarzajace.u2_na_wartosc(iloraz_u2, bity),
                nieodtwarzajace.u2_na_wartosc(reszta_u2, bity),
                bity
            )

    # Koniec pomiaru czasu i wyświetlenie
    if wybor2 == 'T':
        koniec = time.perf_counter()
        while True:
            try:
                precyzja = int(input("\nIle cyfr po przecinku ma mieć wynik pomiaru czasu? "))
                if precyzja < 0:
                    print("Precyzja musi być liczbą nieujemną")
                    continue
                break
            except ValueError:
                print("Błąd: Wprowadź liczbę całkowitą")
        print(f"\nCzas wszystkich dzielen: {(koniec - start):.{precyzja}f} s")
        print(f"Usredniony czas 1 dzielenia: {((koniec - start) / wybor3) * 1000:.{precyzja}f} ms")

    # Wyświetlenie wyniku ostatniego dzielenia
    print("\nWynik dzielenia:")
    if wybor1 == '1':
        print(f"Odtwarzające: Iloraz = {odtwarzajace.u2_na_wartosc(iloraz_u2, bity)}, Reszta = {odtwarzajace.u2_na_wartosc(reszta_u2, bity)}")
        print(f"Iloraz (U2): {bin(iloraz_u2)[2:].zfill(bity)}, Reszta (U2): {bin(reszta_u2)[2:].zfill(bity)}")
    else:
        print(f"Nieodtwarzające: Iloraz = {nieodtwarzajace.u2_na_wartosc(iloraz_u2, bity)}, Reszta = {nieodtwarzajace.u2_na_wartosc(reszta_u2, bity)}")
        print(f"Iloraz (U2): {bin(iloraz_u2)[2:].zfill(bity)}, Reszta (U2): {bin(reszta_u2)[2:].zfill(bity)}")
