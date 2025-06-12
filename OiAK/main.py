import testy


def main():
    wybor = input("1 - Testy automatyczne\n2 - Menu\n")
    if wybor == "1":
        testy.sredni_czas()
    else:
        testy.menu()


if __name__ == '__main__':
    main()
