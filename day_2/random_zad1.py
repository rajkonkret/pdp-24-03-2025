import random

# operacje na liczbach losowych

"""Return random integer in range [a, b], including both end points."""
print(random.randint(1, 100))  # int od 1 do 100

print(random.randrange(1, 100))  # int od 1 do 99
print(random.randrange(5))  # 4, int od 0 do 4

print(random.random())  # float 0.3222029568881031 od 0 do 0.999999
print(random.random() * 8)  # float 7.759120483280217 od 0 do 7.999999

lista = [67, 45, 32, 68, 69, 90, 42]
print(random.choice(lista))  # 68

lista_kule = list(range(1, 50))  # od 1 do 49
wyn = random.choice(lista_kule)
lista_kule.remove(wyn)
print(wyn)

print(random.choices(lista_kule, k=6))  # [7, 20, 1, 35, 35, 33] losuje z powtózeniami
print(random.sample(lista_kule, 6))
print(random.sample(lista_kule, k=6))
# [9, 12, 3, 14, 18, 42]
# [35, 39, 2, 26, 47, 36]
