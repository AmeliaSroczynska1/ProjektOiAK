import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.ticker as mticker

def generuj_calkowity_czas():
    # Dane z tabeli
    ilosc_powtorzen = np.array([500, 1000, 2000, 4000, 10000, 20000, 50000, 100000, 500000, 1000000])
    czas_nieodtwarzajace = np.array(
        [1.1527, 1.6526, 3.3681, 6.5556, 16.3869, 35.4414, 87.4131, 197.0822, 837.4037, 1977.1564])
    czas_odtwarzajace = np.array(
        [1.0117, 1.8427, 3.9761, 7.7972, 18.7922, 46.1263, 103.1222, 194.4311, 954.5574, 2220.6708])

    plt.figure(figsize=(9, 6))

    plt.plot(ilosc_powtorzen, czas_odtwarzajace, marker='o', color='blue', label='Dzielenie odtwarzające')
    plt.plot(ilosc_powtorzen, czas_nieodtwarzajace, marker='o', color='peru', label='Dzielenie nieodtwarzające')

    plt.xlabel('Ilość powtórzeń')
    plt.ylabel('Czas [ms]')

    # Oś X i Y od zera
    plt.xlim(left=0)
    plt.ylim(bottom=0)

    # Oś X bez notacji wykładniczej
    ax = plt.gca()
    ax.ticklabel_format(style='plain', axis='x', useOffset=False)

    # Siatka na 10 głównych linii
    ax.xaxis.set_major_locator(mticker.MaxNLocator(nbins=10))
    ax.yaxis.set_major_locator(mticker.MaxNLocator(nbins=10))
    ax.grid(True, which='major', linestyle='-', linewidth=0.7)

    # Legenda pod wykresem w ramce
    plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.10), fancybox=True, shadow=False, ncol=2, frameon=True)

    plt.tight_layout()
    plt.show()

def generuj_sredni_czas():
    ilosc_powtorzen = np.array([500, 1000, 2000, 4000, 10000, 20000, 50000, 100000, 500000, 1000000])
    czas_nieodtwarzajace = np.array([2.3054, 1.6526, 1.6840, 1.6389, 1.6387, 1.7721, 1.7483, 1.9708, 1.6748, 1.9772])
    czas_odtwarzajace = np.array([2.0234, 1.8427, 1.9881, 1.9493, 1.8792, 2.3063, 2.0624, 1.9443, 1.9091, 2.2207])

    plt.figure(figsize=(9, 6))

    plt.plot(ilosc_powtorzen, czas_odtwarzajace, marker='o', color='blue', label='Dzielenie odtwarzające')
    plt.plot(ilosc_powtorzen, czas_nieodtwarzajace, marker='o', color='peru', label='Dzielenie nieodtwarzające')

    plt.xlabel('Ilość powtórzeń')
    plt.ylabel('Średni czas wykonania [μs]')

    plt.xlim(left=0)
    plt.ylim(0, 2.75)  # Ustawienie zakresu osi Y

    ax = plt.gca()
    ax.ticklabel_format(style='plain', axis='x', useOffset=False)
    ax.xaxis.set_major_locator(mticker.MaxNLocator(nbins=10))
    ax.yaxis.set_major_locator(mticker.MaxNLocator(nbins=10))
    ax.margins(x=0, y=0)
    ax.grid(True, which='major', linestyle='-', linewidth=0.7)

    plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.10), fancybox=True, shadow=False, ncol=2, frameon=True)

    plt.tight_layout()
    plt.show()



