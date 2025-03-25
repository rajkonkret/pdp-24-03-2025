# pętle - możliwość wykonania kodu wielokrotnie
# for - pętla iteracyjna
import random
from itertools import zip_longest

for i in range(10):  # od 0 do 9
    print(i)

for i in range(10):
    pass  # nic nie rób

for _ in range(10):  # niema zmienna
    print("Test podłoga")
    # print(_) # 9

for i in range(5):
    print(i * 2)
    print(i + 2)

# przerobić lotto na pętle
lista_kule = list(range(1, 50))  # od 1 do 49
lista_wynik = []
for _ in range(6):
    wyn = random.choice(lista_kule)
    lista_kule.remove(wyn)
    print(wyn)
    lista_wynik.append(wyn)

print("Wynik losowania:", lista_wynik)  # Wynik losowania: [41, 30, 16, 10, 42, 29]

for i in range(10):
    if i % 2 == 0:
        print(i, "parzysta")

# 0 parzysta
# 2 parzysta
# 4 parzysta
# 6 parzysta
# 8 parzysta

l3 = []
for j in range(10):
    if j % 2 == 0:
        l3.append(j)
print(l3)  # [0, 2, 4, 6, 8]

# list comprehensions
lista3 = [j for j in range(10) if j % 2 == 0]
print(lista3)  # [0, 2, 4, 6, 8]

for c in lista3:
    if c > 4:
        print("Większe od 4")
    else:
        print("Mniejsze, równe 4")
# Mniejsze, równe 4
# Mniejsze, równe 4
# Mniejsze, równe 4
# Większe od 4
# Większe od 4

for i in range(0, 10, 2):  # (start, stop, krok)
    print(i)

for i in range(-10, 0):
    print(i)

for i in range(10, 0, -2):  # krok ujemny, w dół
    print(i)

for c in lista3:
    if c == 2:
        c += 1
        print(c)  # tylko dla c ==2
    print("Przy każdym przejściu pętli")
# Przy każdym przejściu pętli
# 3
# Przy każdym przejściu pętli
# Przy każdym przejściu pętli
# Przy każdym przejściu pętli
# Przy każdym przejściu pętli

imiona = ["Radek", "Tomek", "Zenek", "Ania"]

for p in imiona:
    print(p)
# Radek
# Tomek
# Zenek
# Ania

# 0 Radek
for p in imiona:
    print(imiona.index(p), p)
# 0 Radek
# 1 Tomek
# 2 Zenek
# 3 Ania

for i in range(len(imiona)):
    print(i, imiona[i])
# 0 Radek
# 1 Tomek
# 2 Zenek
# 3 Ania

# enumerate() - zwraca numer elementu i element
for p in enumerate(imiona):
    print(p)
# (0, 'Radek')
# (1, 'Tomek')
# (2, 'Zenek')
# (3, 'Ania')  -> 3 Ania

for i, name in enumerate(imiona):
    print(i, name)
# 0 Radek
# 1 Tomek
# 2 Zenek
# 3 Ania

for i, name in enumerate(imiona, start=1):
    print(i, name)
# 1 Radek
# 2 Tomek
# 3 Zenek
# 4 Ania

imiona = ["Radek", "Tomek", "Zenek", "Ania", "Ewa"]
wiek = [44, 55, 32, 27]

# Radek 44
# for p in imiona:
#     print(p, wiek[imiona.index(p)])
# Radek 44
# Tomek 55
# Zenek 32
# Ania 27
# IndexError: list index out of range

# zip() - łączy kolekcje
for p in zip(imiona, wiek):
    print(p)
# ('Radek', 44)
# ('Tomek', 55)
# ('Zenek', 32)
# ('Ania', 27)

for i, w in zip(imiona, wiek):
    print(i, w)
# Radek 44
# Tomek 55
# Zenek 32
# Ania 27

# 0 Radek 44
for i in enumerate(zip(imiona, wiek)):
    print(i)
# (0, ('Radek', 44))
# (1, ('Tomek', 55))
# (2, ('Zenek', 32))
# (3, ('Ania', 27)) -> 0 Radek 44

a, b = (0, ('Radek', 44))
c, d = ('Radek', 44)
a, (b, d) = (0, ('Radek', 44))
for i, (p, w) in enumerate(zip(imiona, wiek)):
    print(i, p, w)
# 0 Radek 44
# 1 Tomek 55
# 2 Zenek 32
# 3 Ania 27

zipped = zip_longest(imiona, wiek, fillvalue=None)
print(zipped)  # <itertools.zip_longest object at 0x000001C668BD92B0>
# iterator - podstawia danie na aanie w kolejności
print(5 * "-")
for i in zipped:
    print(i)
    # ('Radek', 44)
    # ('Tomek', 55)
    # ('Zenek', 32)
    # ('Ania', 27)
    # ('Ewa', None)

print(5 * "-*-")
for i in zipped:
    print(i)
print(5 * "-*-")
zipped = zip_longest(imiona, wiek, fillvalue=None)
zip_list = list(zipped)
for i in zip_list:
    print(i)
# ('Radek', 44)
# ('Tomek', 55)
# ('Zenek', 32)
# ('Ania', 27)
# ('Ewa', None)
for i, w in zip_list:
    print(i, w)
# Radek 44
# Tomek 55
# Zenek 32
# Ania 27
# Ewa None
