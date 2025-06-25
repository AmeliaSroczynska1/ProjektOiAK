import testy


def main():
    print("Program do dzielenia odtwarzajacego i nieodtwarzajacego liczb w systemie U2"
          "\nWybierz jedną z opcji: ")

    wybor = input("1 - Testy automatyczne\n2 - Menu\n")

    while wybor not in ["1", "2"]:
        print("Nieprawidłowy wybór. Wybierz 1 lub 2")
        wybor = input("1 - Testy automatyczne\n2 - Menu\n")

    if wybor == "1":
        testy.sredni_czas()
    elif wybor == "2":
        testy.menu()

if __name__ == '__main__':
    main()
