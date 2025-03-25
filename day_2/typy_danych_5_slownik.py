# słownik - para klucz - wartość
# "{"user": "Radek", 'wiek': 76}
# '{"name":"John", "age":30, "car":null}'
# odpowiednik json

# pusty słownik
dictionary = dict()
print(dictionary)  # {}
print(type(dictionary))  # <class 'dict'>

dictionary_1 = {}
print(dictionary_1)  # {}
print(type(dictionary_1))  # <class 'dict'>

# dodanie elementu do słownika
dictionary['imie'] = "Radek"
print(dictionary)  # {'imie': 'Radek'}
dictionary['wiek'] = 48
print(dictionary)  # {'imie': 'Radek', 'wiek': 48}

print(dictionary.keys())  # dict_keys(['imie', 'wiek'])
print(dictionary.values())  # dict_values(['Radek', 48])
print(dictionary.items())  # dict_items([('imie', 'Radek'), ('wiek', 48)])

# nadpisanie elementu
dictionary['imie'] = "Tomek"
print(dictionary)  # {'imie': 'Tomek', 'wiek': 48}

# wypisanie wartości dla elemntu ze słownika
print(dictionary['imie'])  # Tomek

# print(dictionary["Imie"])  # KeyError: 'Imie'
print(dictionary.get("Imie"))  # nie ma klucz -> None
print(dictionary.get("Imie", "default"))  # default

dictionary.update({'data': "12-12-2025"})
print(dictionary)  # {'imie': 'Tomek', 'wiek': 48, 'data': '12-12-2025'}

dict_small = {'x': 2}
print(dict_small)
dict_small.update([('y', 5), ('z', 48)])
print(dict_small)  # {'x': 2, 'y': 5, 'z': 48}

# input() - pozwala wprowadzic dane do komputera
# tekst = input("Podaj imię")
# print(tekst)
# # Podaj imięRadek
# Radek

# napisac aplikację kalkulator
# pobrać dwie liczby
# wypisac wynik np.: dodawania
# a = int(input("Pierwsza liczba"))  # zwraca str
# b = float(input("Druga liczba"))
# print(int(a) + float(b))  # 35.0

# napisac aplikację słownik pol_ang
# stworzyc słownik
# wyswietlic (klucze:
# pobrac słowko od usera
# wyswietlić tłumaczenie

pol_ang = {"kot": 'cat', "pies": "dog", "dach": "roof"}
print("Znam takie słowa:", pol_ang.keys())
odp = input("Podaj słówko do przetłumaczenia")
# print(pol_ang[odp.lower().strip()])
print(pol_ang.get(odp.strip().lower(), "nie ma"))
# ẞ - ss
name1 = "GROSS"
name2 = 'groẞ'

print(name1.lower() == name2.lower())  # False
print(name1.casefold() == name2.casefold())  # True
#  """ Return a version of the string suitable for caseless comparisons. """
# https://www.unicode.org/Public/16.0.0/ucd/CaseFolding.txt
