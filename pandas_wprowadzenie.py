#Zad 1
#Wczytaj do DataFrame arkusz z narodzinami dzieci w Polsce dostępny w pliku /datasets/imiona.xlsx

import pandas as pd

# plik = pd.ExcelFile('imiona.xlsx')
# df = pd.read_excel(plik, header=0)

#Zad2
#Z danych z zadania 1 wyświetl (korzystając w miarę możliwości z funkcji biblioteki Pandas):
# tylko te rekordy gdzie liczba nadanych imion była większa niż 1000 w danym roku
# tylko rekordy gdzie nadane imię jest takie jak Twoje
# sumę wszystkich urodzonych dzieci w całym danym okresie,
# sumę dzieci urodzonych w latach 2000-2005
# sumę urodzonych chłopców i dziewczynek,
# najbardziej popularne imię dziewczynki i chłopca w danym roku ( czyli po 2 rekordy na rok),
# najbardziej popularne imię dziewczynki i chłopca w całym danym okresie,

# print(df[df.Liczba > 1000])
# print('')
# print(df[df.Imie == 'RADOSŁAW'])
# print('')
# print(df.Liczba.sum())
# print('')
# grupa = df[df.Rok < 2006]
# print(grupa.Liczba.sum())
# grupa = df[df.Rok < 2006].groupby('Rok').agg({'Liczba': ['sum']})
# print(grupa)
# print('')
#
# print(df.groupby('Plec').agg({'Liczba':['sum']}))
#
# print(df.sort_values('Liczba', ascending=False).groupby(['Rok', 'Plec']).first())
#
# new_df = df.sort_values('Liczba', ascending=False).groupby(['Rok', 'Plec'])
#
# for index, group in enumerate(new_df, start=1):
#     print(f"{index} {group[0]}")
#     print(f" {group[1].iloc[0]['Imie']}", end='')
#     print(f" {group[1].iloc[0]['Liczba']}")
# grupa = df.groupby(['Rok', 'Plec']).agg('Liczba').max()
# print(grupa)
#
# for i,g in enumerate(grupa, start=1):
#     print(i)
#     print(df[df['Liczba'] == g])
# grupa = df.groupby(['Rok', 'Plec']).agg({'Liczba':['max']})
# print(grupa[max])
# for i, g in enumerate(grupa[max], start=1):
#     print(df[df['Liczba'] == g])
# print('')
# print("Chłopiec")
# print(df[df['Plec'] == 'M'].groupby(['Imie']).agg({'Liczba': ['sum']}).sort_values(('Liczba', 'sum'),
#                                                                                    ascending=False).iloc[0])
# print("Dziewczynka")
# print(df[df['Plec'] == 'K'].groupby(['Imie']).agg({'Liczba': ['sum']}).sort_values(('Liczba', 'sum'),
#                                                                                    ascending=False).iloc[0])

#Zad 3
#Wczytaj plik /datasets/zamowieniana.csv a następnie wyświetl:
# listę unikalnych nazwisk sprzedawców (przetwarzając zwróconą pojedynczą kolumnę z DataFrame)
# 5 najwyższych wartości zamówień
# ilość zamówień złożonych przez każdego sprzedawcę
# sumę zamówień dla każdego kraju
# sumę zamówień dla roku 2005, dla sprzedawców z Polski
# średnią kwotę zamówienia w 2004 roku,
# zapisz dane za 2004 rok do pliku zamówienia_2004.csv a dane za 2005 do pliku zamówienia_2005.csv

# df = pd.read_csv('zamowienia.csv', header=0, sep=';', decimal='.')
#
# print(df['Sprzedawca'].unique())
# # print('')
# print(df.sort_values('Utarg', ascending=False).head(5))
# # print('')
# print(df.groupby('Sprzedawca').size())
# print('')
# print(df.groupby('Kraj').agg({'Utarg': ['sum']}))
# print(df.groupby('Kraj').size())
# # print('')
# print(df[(df['Kraj'] == 'Polska') & (df['Data zamowienia'] >= '2005-01-01') & (df['Data zamowienia'] <= '2005-12-31')].
#       agg({'Utarg': ['sum']}))
# # print('')
# print(df[df['Data zamowienia'].str[:4] == '2004'].agg({'Utarg': ['mean']}))
# rok_2004 = df[((df[ 'Data zamowienia'] >= '2004-01-01') & (df['Data zamowienia'] <= '2004-12-31'))]
# rok_2004.to_csv("zamowienia_2004.csv", index=False)
#
