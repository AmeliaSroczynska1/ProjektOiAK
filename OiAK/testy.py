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
    dzielna = int(input("Podaj dzielną: "))
    dzielnik = int(input("Podaj dzielnik: "))

    wybor = input("\nJaką metodą chcesz dzielić?\n"
          "1 - Odtwarzającą\n"
          "2 - Nieodtwarzającą\n")
    if(wybor == '1'):
        odtwarzajace.dzielenie(dzielna, dzielnik)
    elif wybor == '2':
        nieodtwarzajace.dzielenie(dzielna, dzielnik)
    else:
        print("Podałeś nieporawidłowy znak, możesz wybrać tylko 1 lub 2")