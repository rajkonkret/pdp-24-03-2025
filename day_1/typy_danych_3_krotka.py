# krotka - tuple - kolekcja niemutowalna, tylko do odczytu
# pozwala efektywniej zarządzać pamięcią
# krotka - zastępstwo stałych

tupla_imiona = ("Radek", "Tomek", "Zenek", 'Anna', "Marek")
print(tupla_imiona)  # ('Radek', 'Tomek', 'Zenek', 'Anna', 'Marek')
print(type(tupla_imiona))  # <class 'tuple'>

tupla_liczby = 43, 55, 22, 34, 11, 200
print(type(tupla_liczby))  # <class 'tuple'>
print(tupla_liczby)  # (43, 55, 22, 34, 11, 200)

# tupla jednoelementowa
tupla = ("radek")
print(type(tupla))  # <class 'str'>
tupla = "Radek",
print(type(tupla))  # <class 'tuple'>

# PEP8 zaleca tuple jedoelementowe umiesczac w nawiasach
tupla = ("Radek",)
print(type(tupla))  # <class 'tuple'>

# tupla jest niemutowalna
# tupla_liczby[3] = 89 # TypeError: 'tuple' object does not support item assignment

# del tupla_liczby
print(tupla_liczby)  # NameError: name 'tupla_liczby' is not defined
# del tupla[0] # TypeError: 'tuple' object doesn't support item deletion

print(tupla_imiona.index("Radek"))  # indeks 0
print(tupla_imiona.count("Radek"))  # występuje 1 raz

# rozpakowanie tupli
tup = 1, 2
print(type(tup))  # <class 'tuple'>

a, b = 1, 2

a, b = tup  # 1, 2
print(f"{a=}, {b=}")  # a=1, b=2

tup2 = 1, 2, 3
# a, b = tup2 # ValueError: too many values to unpack (expected 2)
a, *b = tup2  # * worek na pozostałe dane
print(f"{a=}, {b=}")  # a=1, b=[2, 3]

print(tupla_imiona)  # ('Radek', 'Tomek', 'Zenek', 'Anna', 'Marek')
# name1, name2, name3

name1, name2, *name3 = tupla_imiona
print(f"{name1=}, {name2=}, {name3=}")
# name1='Radek', name2='Tomek', name3=['Zenek', 'Anna', 'Marek']

*name1, name2, name3 = tupla_imiona
print(f"{name1=}, {name2=}, {name3=}")
# name1=['Radek', 'Tomek', 'Zenek'], name2='Anna', name3='Marek'

name1, *name2, name3 = tupla_imiona
print(f"{name1=}, {name2=}, {name3=}")
# name1='Radek', name2=['Tomek', 'Zenek', 'Anna'], name3='Marek'

# sortowanie krotki zwraca listę
print(sorted(tupla_imiona))  # ['Anna', 'Marek', 'Radek', 'Tomek', 'Zenek']
print(tupla_imiona)  # krotka nie ulega zmianie
print(type(tupla_imiona))  # <class 'tuple'>

lista_sorted = sorted(tupla_imiona)
print(type(lista_sorted))  # <class 'list'>
print(lista_sorted)  # ['Anna', 'Marek', 'Radek', 'Tomek', 'Zenek']

lista = list(tupla_imiona)
print(lista)
print(type(lista))
# ['Radek', 'Tomek', 'Zenek', 'Anna', 'Marek']
# <class 'list'>
