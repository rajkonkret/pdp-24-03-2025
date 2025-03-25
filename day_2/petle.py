# pętle - możliwość wykonania kodu wielokrotnie
# for - pętla iteracyjna
import random

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
