# funkcja lambda
# skrócony zapis funkcji
# domyślnie return
from functools import reduce


def odejmij(a, b):
    return a - b


print(odejmij(8, 7))

odejmij2 = lambda a, b: a - b
print(odejmij2(45, 34))  # 11

oblicz_vat = lambda kwota, vat=23: kwota * (100 + vat) / 100
print(oblicz_vat(1000))  # 1230.0

wiek = lambda x: "dziecko" if x < 10 else ("nastolatek" if x < 18 else "dorosły")
print(wiek(9))  # dziecko
print(wiek(10))  # nastolatek
print(wiek(17))  # nastolatek
print(wiek(18))  # dorosły
print(wiek(25))  # dorosły

# mapowanie danych
lista = [1, 2, 3, 4, 24, 50, 100, 500]

l = []
for i in lista:
    l.append(i * 2)
print(l)  # [2, 4, 6, 8, 48, 100, 200, 1000]

print([i * 2 for i in lista])  # [2, 4, 6, 8, 48, 100, 200, 1000]


def zmien(x):
    return x * 2


l2 = []
for i in lista:
    l2.append(zmien(i))
print(l2)  # [2, 4, 6, 8, 48, 100, 200, 1000]

# funkcje wyższego rzędu

# map() - bierze elementy kolekcji i wykonuje na nich funkcję
print(f"Zastosowanie map() {list(map(zmien, lista))}")  # Zastosowanie map() [2, 4, 6, 8, 48, 100, 200, 1000]

# zastosowanie lambdy jako funkcja anonimowa
# definicja w miejscu wywołania
print(f"Zastosowanie map() {list(map(lambda x: x * 2, lista))}")  # Zastosowanie map() [2, 4, 6, 8, 48, 100, 200, 1000]
print(f"Zastosowanie map() {list(map(lambda x: x * 4, lista))}")
# Zastosowanie map() [4, 8, 12, 16, 96, 200, 400, 2000]
print(f"Zastosowanie map() {list(map(lambda x: x * 8, lista))}")
# Zastosowanie map() [8, 16, 24, 32, 192, 400, 800, 4000]
print(f"Zastosowanie map() {list(map(lambda x: x * 1.5, lista))}")
# Zastosowanie map() [1.5, 3.0, 4.5, 6.0, 36.0, 75.0, 150.0, 750.0]

# filtrowanie danych
# filter()
l3 = []
for i in lista:
    if i < 3:
        l3.append(i)
print(l3)  # [1, 2]

print(f"Zastsowanie filter: {list(filter(lambda x: x < 3, lista))}")  # Zastsowanie filter: [1, 2]
print(f"Zastsowanie filter: {list(filter(lambda x: x < 50, lista))}")  # Zastsowanie filter: [1, 2, 3, 4, 24]
print(f"Zastsowanie filter: {list(filter(lambda x: x > 20, lista))}")  # Zastsowanie filter: [24, 50, 100, 500]
print(f"Zastsowanie filter: {list(filter(lambda x: x < 500, lista))}")  # Zastsowanie filter: [24, 50, 100, 500]

# x > 3 i x < 250
print(f"Zastsowanie filter: {list(filter(lambda x: x > 3 and x < 250, lista))}")
# Zastsowanie filter: [4, 24, 50, 100]
print(f"Zastsowanie filter: {list(filter(lambda x: 3 < x < 250, lista))}")  # Zastsowanie filter: [4, 24, 50, 100]

# For example, reduce(lambda x, y: x+y, [1, 2, 3, 4, 5])
#     calculates ((((1 + 2) + 3) + 4) + 5).
sum_all = reduce(lambda a, b: a + b, [1, 2, 3, 4, 5])
print("Wynik reduce:", sum_all)  # Wynik reduce: 15
# 1 + 2 = 3
# 3 + 3 = 6
# 6 + 4 = 10
# 10 + 5 = 15 -> wynik reduce()

product = reduce(lambda a, b: a * b, [1, 2, 3, 4, 5])
print("Wynik mnożenia:", product)  # Wynik mnożenia: 120
print(((((1 * 2) * 3) * 4) * 5))  # 120
