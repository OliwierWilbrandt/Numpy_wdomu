import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#Zad1
# Za pomocą biblioteki matplotlib utwórz wykres liniowy funkcji f(x) = sin(x) * x, dla x z przedziału [-3,3] z wartościami zmieniającymi się co 1/2.
# Ustaw zakres osi x na wartości -3 i 3, dodaj etykiety do osi x i y, ustaw tytuł wykresu
# def f(x):
#     return np.sin(x) * x
#
# x_wart = np.arange(-3, 3.5, 0.5)
# y_wart = f(x_wart)
#
# plt.figure(figsize=(10, 6))
# plt.plot(x_wart, y_wart, marker='o')
#
# plt.xlim(-3, 3)
#
# plt.xlabel('x')
# plt.ylabel('f(x) = sin(x) * x')
# plt.title('Wykres funkcji f(x) = sin(x) * x')
#
# plt.grid(True)
# plt.show()

#Zad2
# Za pomocą biblioteki pomocą pandas wczytaj zawartość pliku „automobile.csv” do ramki danych, a następnie:
#	Utwórz i wyświetl nową ramkę danych składającą się z rekordów dla samochodów audi i dodge.
#	Na nowej ramce danych dokonaj grupowania danych po kolumnie „Car model” a następnie policz sumę wartości dla tych samochodów (kolumna Price)
#	Na podstawie utworzonej grupy utwórz wykres słupkowy, dodaj tytuł oraz etykiety dla osi x i y. Dopasuj rozmiar wykresu tak aby był on widoczny w całości.


# df = pd.read_csv('automobile.csv', header=0, sep=';', decimal='.')
#
# filtered_df = df[df['Car model'].isin(['audi', 'dodge'])]
#
# grouped_df = filtered_df.groupby('Car model')['Price'].sum().reset_index()
#
# print("Nowa ramka danych audi i dodge:\n", filtered_df)
# print(grouped_df)
#
# plt.figure(figsize=(12, 8))
# plt.bar(grouped_df['Car model'], grouped_df['Price'], color=['blue', 'green'])
#
# plt.title('Sum of Prices for Audi and Dodge Car Models')
# plt.xlabel('Car Model')
# plt.ylabel('Total Price')
#
# plt.xticks(rotation=45)
# plt.tight_layout()
# plt.show()


#Zad3
# Za pomocą biblioteki pomocą pandas wczytaj zawartość pliku „automobile.csv” do ramki danych i  utwórz wykres kołowy przedstawiający procentową ilość samochodów
# z danym rodzajem paliwa (kolumna Fuel-type). Procentowe wartości mają być zaokrąglone do dwóch miejsc po przecinku, rozmiar czcionki 14. Dodaj tytuł i legendę.

# df = pd.read_csv('automobile.csv', header=0, sep=';', decimal='.')
#
# fuel_counts = df['Fuel-type'].value_counts()
#
# fuel_percentages = (fuel_counts / fuel_counts.sum()) * 100
# fuel_percentages = fuel_percentages.round(2)
#
# plt.figure(figsize=(10, 7))
# plt.pie(fuel_percentages, labels=fuel_percentages.index, autopct='%1.2f%%', textprops={'fontsize': 14})
#
# plt.title('Procentowy podział rodzajów paliwa', fontsize=16)
# plt.legend(fuel_percentages.index, title="Rodzaj paliwa", fontsize=14)
#
# plt.show()
