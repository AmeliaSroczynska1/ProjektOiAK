import time

import generator_liczb
import nieodtwarzajace
import odtwarzajace


# Liczy średni czas dzielenia po 1000 iteracjach
def sredni_czas():
    dzielna = generator_liczb.losuj()
    dzielnik = generator_liczb.losuj()
    while dzielnik == 0:
        if dzielnik == 0:
            generator_liczb.losuj()

    # Dla metody odtwarzajacej
    start = time.perf_counter()

    for i in range(1000):
        odtwarzajace.dzielenie(dzielna, dzielnik)

    koniec = time.perf_counter()

    czas_odtwarzajace = koniec - start

    # Dla metody nieodtwarzajacej
    start = time.perf_counter()

    for i in range(1000):
        nieodtwarzajace.dzielenie(dzielna, dzielnik)

    koniec = time.perf_counter()

    czas_nieodtwarzajace = koniec - start

    # Zapis wyniku
    print(f"\nCzas dzielenia odtwarzajacego = {czas_odtwarzajace: .4f} ms")
    print(f"Czas dzielenia nieodtwarzajacego = {czas_nieodtwarzajace: .4f} ms")


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
        dzielna = int(input("Podaj dzielna: "))
        dzielnik = int(input("Podaj dzielnik: "))
        while dzielnik == 0:
            if dzielnik == 0:
                print("Nie mozna dzielic przez 0")
            wybor1 = input("\nPodaj dzielnik jeszcze raz\n")

    elif wybor0 == "2":
        dzielna = generator_liczb.losuj()
        dzielnik = generator_liczb.losuj()
        while dzielnik == 0:
            if dzielnik == 0:
                generator_liczb.losuj()
    else:
        while wybor0 not in ('1', '2'):
            if wybor0 not in ('1', '2'):
                print("Podałeś nieprawidłowy znak, możesz wybrać tylko 1 lub 2")
            wybor0 = input("\nChcesz sam wpisać liczby, ktore program podzieli czy wygenerowac z przedzialu 0-1000 losowe liczby?\n"
                   "1 - Chce wpisac\n"
                   "2 - Losowe\n")

    # Wybor metody dzielenia
    wybor1 = input("\nJaką metoda chcesz dzielic?\n"
          "1 - Odtwarzajaca\n"
          "2 - Nieodtwarzajaca\n")

    while wybor1 not in ('1', '2'):
        if wybor1 not in ('1', '2'):
            print("Podałeś nieprawidłowy znak, możesz wybrać tylko 1 lub 2")
        wybor1 = input("\nJaką metodą chcesz dzielić?\n"
                       "1 - Odtwarzająca\n"
                       "2 - Nieodtwarzająca\n")

    # Wybor czy liczymy czas
    wybor2 = input("\nCzy chcesz obliczyc tez czas dzielenia? T - tak\n")

    # Wybor ile razy powtarzamy dzielenie
    wybor3 = int(input("\nIle razy chcesz powtorzyc pomiar? "))

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
        precyzja = int(input("\nIle cyfr po przecinku ma mieć wynik pomiaru czasu? "))
        print(f"\nCzas wszystkich dzielen: {(koniec - start) * 1000:.{precyzja}f} ms")
        print(f"Usredniony czas 1 dzielenia: {((koniec - start) / wybor3) * 1000:.{precyzja}f} ms")






