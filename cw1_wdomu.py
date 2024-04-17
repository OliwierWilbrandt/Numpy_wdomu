#Zad1
# import numpy as np
#
# tablica = np.arange(3, 3*16, 3)
#
# print(tablica)

#Zad2

# import numpy as np
#
# lista_float = [2.5, 3.7, 4.2, 6.9, 8.1]
#
# tablica_float = np.array(lista_float)
#
# tablica_int64 = tablica_float.astype(np.int64)
#
# print("Oryginalna tablica z wartościami zmiennoprzecinkowymi:")
# print(tablica_float)
# print("\nSkopiowana tablica z wartościami przekonwertowanymi na typ int64:")
# print(tablica_int64)

#Zad3
#
# import numpy as np
# def utworz_tablice(n):
#     tablica = np.arange(1, n*n+1).reshape(n, n)
#     return tablica
#
# n = 3
# wynikowa_tablica = utworz_tablice(n)
# print("Tablica dla n =", n, ":\n", wynikowa_tablica)

#Zad4
#
# import numpy as np
# def generuj(podstawa, ilosc):
#     tablica_poteg = np.logspace(0, ilosc - 1, num=ilosc, base=podstawa, dtype=int)
#     return tablica_poteg
#
# podstawa = 2
# ilosc = 4
# wynik = generuj(podstawa, ilosc)
# print(wynik)

#Zad5

import numpy as np
def generuj_macierz_diagonalna(dlugosc):
    wektor_odwrocony = np.arange(dlugosc, 0, -1)

    macierz_diagonalna = np.diag(wektor_odwrocony)

    return macierz_diagonalna

dlugosc_wektora = 5
wynikowa_macierz = generuj_macierz_diagonalna(dlugosc_wektora)
print("Wygenerowana macierz diagonalna:\n", wynikowa_macierz)