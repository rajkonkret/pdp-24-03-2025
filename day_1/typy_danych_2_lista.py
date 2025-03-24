# kolekcje - przechowuje wiele lementów danego typu

# lista - przechowuje wiele elementów, róznego typu na raz
# zachowuje kolejnośc przy dodawaniu elementów

# pusta lista
lista = []
print(lista)  # []
print(type(lista))  # <class 'list'>

pusta_lista = list()
print(pusta_lista)  # []
print(type(pusta_lista))  # <class 'list'>

# append() - dodawanie elemntów do listy
lista.append("Radek")
lista.append("Tomek")
lista.append("Zenek")
lista.append("Bogdan")
lista.append("Maciek")
print(lista)  # ['Radek', 'Tomek', 'Zenek', 'Bogdan', 'Maciek']

# ['Radek', 'Tomek', 'Zenek', 'Bogdan', 'Maciek']
#    0         1        2        3         4
#    -5       -4        -3      -2         -1
print(len(lista))  # 5
print(lista[0])  # Radek
print(lista[2])  # Zenek
print(lista[4])  # Maciek

# print(lista[10]) # IndexError: list index out of range

print(lista[4])
print(lista[len(lista) - 1])  # Maciek
print(lista[-1])  # ostatni element z listy, Maciek
print(lista[-3])  # Zenek

# wyświetlenie fragmentu listy (slicowanie)
print(lista[0:3])  # ['Radek', 'Tomek', 'Zenek'] -> 012 indeksy
print(lista[:3])  # ['Radek', 'Tomek', 'Zenek']
print(lista[2:])  # ['Zenek', 'Bogdan', 'Maciek']
print(lista[2:4])  # ['Zenek', 'Bogdan']

print(lista[2:16])  # ['Zenek', 'Bogdan', 'Maciek']
print(lista[:])  # ['Radek', 'Tomek', 'Zenek', 'Bogdan', 'Maciek']
print(lista[2:2])  # []
print(lista[2:3])  # ['Zenek']
print(lista[10:27])  # []

# ['Radek', 'Tomek', 'Zenek', 'Bogdan', 'Maciek']
#    0         1        2        3         4
#    -5       -4        -3      -2         -1

print(lista[-2:0])  # [] -> [3:0]
print(lista[0:-2])  # ['Radek', 'Tomek', 'Zenek'] -> [0:3]

lista_15 = list(range(15))  # od 0 do 14
print(lista_15)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
print(lista_15[0:15:2])  # [start:stop:krok] # [0, 2, 4, 6, 8, 10, 12, 14]
print(list(range(0, 15, 2)))  # [0, 2, 4, 6, 8, 10, 12, 14]
print(lista[::2])  # ['Radek', 'Zenek', 'Maciek'] co drugi

print(lista[::-1])  # krok w tył, wyswietli odwróconą listę
# ['Maciek', 'Bogdan', 'Zenek', 'Tomek', 'Radek']

# nadpisanie elementu w liście
lista[3] = "Ania"
print(lista)  # ['Radek', 'Tomek', 'Zenek', 'Ania', 'Maciek']

# dopisanie lementu we wskazanym indeksie
lista.insert(1, "Krzysztof")
print(lista)  # ['Radek', 'Krzysztof', 'Tomek', 'Zenek', 'Ania', 'Maciek']

lista.insert(15, "Asia")
print(lista)
# ['Radek', 'Krzysztof', 'Tomek', 'Zenek', 'Ania', 'Maciek', 'Asia']
print(lista.index("Asia"))  # 6

# usunięcie elementu po indeksie
lista.remove("Asia")
print(lista)  # ['Radek', 'Krzysztof', 'Tomek', 'Zenek', 'Ania', 'Maciek']

# usunięcie elemntu po indeksie
print(lista.pop(4))  # Ania zwraca element co usunął
print(lista)
print(lista.pop(-3))  # Tomek
print(lista.pop())  # Maciek usunie ostatni element
