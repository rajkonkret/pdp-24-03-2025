# zbiór (set) - nieprzechowują duplikatów
# nie zachowuje kolejności przy dodawaniu
# nie posiada indeksu

lista = [44, 55, 66, 777, 33, 22, 11, 33, 11]
zbior = set(lista)
print(zbior)  # {33, 66, 777, 11, 44, 22, 55}
print(type(zbior))  # <class 'set'>

# pusty zbiór
zb2 = set()
print(zb2)  # set()
print(type(zb2))  # <class 'set'>

# dodanie lementu do zbioru
zbior.add(33)
zbior.add(33)
zbior.add(33)
zbior.add(18)
zbior.add(33)
zbior.add(33)
zbior.add(24)
print(zbior)
# {33, 66, 777, 11, 44, 18, 22, 55, 24}

# usunięcie elementu ze zbioru
zbior.remove(55)
print(zbior)  # {33, 66, 777, 11, 44, 18, 22, 24}

# pop() - usunięcie pierwszego elemntu ze zbioru
print(zbior.pop())  # 33
print(zbior)  # {66, 777, 11, 44, 18, 22, 24}
print(zbior.pop())  # 66
zmienna = zbior.pop()
print("Usuneliśmy:", zmienna)  # Usuneliśmy: 777

zbior_copy = zbior.copy()
print(zbior_copy)  # {18, 22, 24, 11, 44}
print(zbior)  # {11, 44, 18, 22, 24}
print(id(zbior))  # 1926815211680
print(id(zbior_copy))  # 1926815207200

# opracje na zbiorach
zbior_2 = {667, 11, 44, 12.34, 18, 52, 667, 62}
print(type(zbior_2))  # <class 'set'>
print(zbior_2)  # {18, 667, 52, 11, 44, 12.34, 62}

# suma zbiorów - zwraca nowy zbiór
print(zbior | zbior_2)  # {11, 44, 12.34, 18, 52, 22, 24, 667, 62}
print(zbior.union(zbior_2))  # {11, 44, 12.34, 18, 52, 22, 24, 667, 62}

# cześc wspólna
print(zbior & zbior_2)  # {18, 11, 44}
print(zbior.intersection(zbior_2))  # {18, 11, 44}

# różnica
print(zbior - zbior_2)  # {24, 22}
print(zbior.difference(zbior_2))  # {24, 22}
print(zbior_2.difference(zbior))  # {667, 52, 12.34, 62}

# łączy zbiory, zienia bazowy!
zbior.update(zbior_2)
print(zbior)  # {11, 44, 12.34, 18, 52, 22, 24, 667, 62}

krotka = tuple(zbior)
print(krotka)  # (11, 44, 12.34, 18, 52, 22, 24, 667, 62)

lista = list(zbior)
print(lista)  # [11, 44, 12.34, 18, 52, 22, 24, 667, 62]

# sprawdzenie elemntu w kolekcji
print(667 in zbior)  # True
print(777 in lista)  # False
print(62 in krotka)  # True
