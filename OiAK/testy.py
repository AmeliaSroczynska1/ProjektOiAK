import time
import nieodtwarzajace
import odtwarzajace


def sredni_czas(dzielna, dzielnik):
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


def menu():
    dzielna = int(input("Podaj dzielna: "))
    dzielnik = int(input("Podaj dzielnik: "))

    wybor1 = input("\nJaką metoda chcesz dzielic?\n"
          "1 - Odtwarzajaca\n"
          "2 - Nieodtwarzajaca\n")

    wybor2 = input("\nCzy chcesz obliczyc tez czas dzielenia? T - tak\n")

    wybor3 = int(input("\nIle razy chcesz powtorzyc pomiar?"))

    start = 0

    if wybor2 == 'T':
        start = time.perf_counter()

    for i in range(wybor3):
        if wybor1 == '1':
            odtwarzajace.dzielenie(dzielna, dzielnik)

        elif wybor1 == '2':
            nieodtwarzajace.dzielenie(dzielna, dzielnik)

        else:
            print("Podales nieporawidlowy znak, mozesz wybrac tylko 1 lub 2")

    if wybor2 == 'T':
        koniec = time.perf_counter()
        print(f"\nCzas wszystkich dzielen: {(koniec - start) * 1000:.2f} ms")
        print(f"Usredniony czas 1 dzielenia: {((koniec - start) / wybor3) * 1000:.2f} ms")


