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
