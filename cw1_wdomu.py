#Zad1

#Za pomocą funkcji arange stwórz tablicę numpy składającą się z 15 kolejnych wielokrotności liczby 3.

# import numpy as np
#
# tablica = np.arange(3, 3*16, 3)
#
# print(tablica)

#Zad2

#Stwórz listę składającą się z wartości zmiennoprzecinkowych a następnie zapisz do innej zmiennej jej kopię przekonwertowaną na typ int64

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

#Napisz funkcję, która będzie:
# Przyjmowała jeden parametr ‘n’ w postaci liczby całkowitej
# Zwracała tablicę Numpy o wymiarach n*n kolejnych liczb całkowitych poczynając od 1

# import numpy as np
# def utworz_tablice(n):
#     tablica = np.arange(1, n*n+1).reshape(n, n)
#     return tablica
#
# n = 3
# wynikowa_tablica = utworz_tablice(n)
# print("Tablica dla n =", n, ":\n", wynikowa_tablica)

#Zad4

#Napisz funkcję, która będzie przyjmowała 2 parametry: liczbę, która będzie podstawą operacji potęgowania oraz ilość kolejnych potęg do wygenerowania.
# Korzystając z funkcji logspace generuj tablicę jednowymiarową kolejnych potęg podanej liczby, np. generuj(2,4) -> [2,4,8,16]

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

#Napisz funkcję, która:
# Na wejściu przyjmuje jeden parametr określający długość wektora
# Na podstawie parametru generuj wektor, ale w kolejności odwróconej
# Generuj macierz diagonalną z w/w wektorem jako przekątną

# import numpy as np
# def generuj_macierz_diagonalna(dlugosc):
#     wektor_odwrocony = np.arange(dlugosc, 0, -1)
#
#     macierz_diagonalna = np.diag(wektor_odwrocony)
#
#     return macierz_diagonalna
#
# dlugosc_wektora = 5
# wynikowa_macierz = generuj_macierz_diagonalna(dlugosc_wektora)
# print("Wygenerowana macierz diagonalna:\n", wynikowa_macierz)

#Zad6

#Stwórz skrypt który na wyjściu wyświetli macierz numpy (tablica wielowymiarowa) w postaci wykreślanki,
# gdzie jedno słowo będzie wypisane w kolumnie, jedno w wierszu i jedno po ukosie. Jedno z tych słów powinno być wypisane od prawej do lewej.

# import numpy as np
# def generate_crossword(word1, word2, word3):
#
#     max_len = max(len(word1), len(word2), len(word3))
#
#     crossword = np.full((max_len, max_len), ' ', dtype=str)
#
#     crossword[:len(word1), 0] = list(word1)
#     crossword[max_len - len(word2):, max_len - 1] = list(word2[::-1])
#     np.fill_diagonal(crossword, list(word3))
#
#     return crossword
#
# word1 = 'PYTHON'
# word2 = 'NUMPY'
# word3 = 'WIZUALIZACJA'
#
# crossword = generate_crossword(word1, word2, word3)
#
# print(crossword)

#Zad7

#Napisz funkcję, która wygeneruje macierz wielowymiarową postaci:
#[[2 4 6]
#[4 2 4]
#[6 4 2]]
#Przy założeniach:
#funkcja przyjmuje parametr n, który określa wymiary macierzy jako n*n i umieszcza wielokrotność liczby 2 na kolejnych jej przekątnych rozchodzących się od głównej przekątnej.

# import numpy as np
# def generate_diagonal_matrix(n):
#
#     matrix = np.zeros((n, n), dtype=int)
#
#     for i in range(n):
#         for j in range(n):
#             if i == j:
#                 matrix[i, j] = 2 * (i + 1)
#             elif i < j:
#                 matrix[i, j] = 2 * (j - i + 1)
#             else:
#                 matrix[i, j] = 2 * (i - j + 1)
#
#     return matrix
#
# n = 3
# result_matrix = generate_diagonal_matrix(n)
# print(result_matrix)

#Zad8



#Zad9

#Wykorzystaj poznane na zajęciach funkcje biblioteki Numpy i stwórz macierz 5x5, która będzie zawierała kolejne wartości ciągu Fibonacciego.

# import numpy as np
# def fibonacci(n):
#
#     fib_matrix = np.zeros((n, n), dtype=int)
#
#     fib_matrix[0, 0] = 0
#     fib_matrix[0, 1] = 1
#
#     for i in range(n):
#         for j in range(n):
#             if i == 0 and j <= 1:
#                 continue
#             fib_matrix[i, j] = fib_matrix[i, j - 1] + fib_matrix[i, j - 2]
#
#     return fib_matrix
#
# fibonacci_matrix = fibonacci(5)
# print(fibonacci_matrix)


