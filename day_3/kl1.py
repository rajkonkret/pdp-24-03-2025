# klasa - elemnt programowania obiektowego
# klasa - szablon, przepis wg którego będą budowane obiekty
# cechy - pol (zmienne)
# metody - funkcje mozliwe do wykonania
# obiekt - instancja klasy
# klasa musi być zadeklarowana przed użyciem
# tworzenie obiektu uruchamia metode __init__ w klasie
# paradygmaty programowania obiektowego -> hermetyzacja, dziedziczenie, polimorfizm, abstrakcja

# PasacalCase
# dekalracja klasy
class Human:
    """
    Klasa Human w pythonie
    """

    imie = ""
    wiek = ""
    plec = "k"

    # self obiekt, który wywołał metode
    def powitanie(self):
        print(f"Nazywam się {self.imie}")

    # wypisz_wiek
    def wypisz_wiek(self):
        print(f"Mam {self.wiek} l.")


#
# print(Human.__doc__)  # Klasa Human w pythonie
# print(print.__doc__)
#   sep
#     string inserted between values, default a space.
#   end
#     string appended after the last value, default a newline.
#   file
#     a file-like object (stream); defaults to the current sys.stdout.
#   flush
#     whether to forcibly flush the stream.


# cd .\day_3\
# pydoc -b - sewer z dokumentacją
# pydoc -w kl1 - tworzy plik html z dokumentacją

cz1 = Human()
print(cz1)  # <__main__.Human object at 0x000001FB1F5256D0>
print(cz1.imie)
print(cz1.wiek)
print(cz1.plec)

cz1.imie = "Radek"
cz1.wiek = 60
cz1.plec = "m"
print(cz1.imie)
print(cz1.wiek)
print(cz1.plec)
# Radek
# 60
# m
cz2 = Human()
cz2.imie = "Anna"
cz2.wiek = 32

print(cz2.imie)
print(cz2.wiek)
print(cz2.plec)

cz1.powitanie()
cz2.powitanie()
# Nazywam się Radek
# Nazywam się Anna
cz1.wypisz_wiek()
cz2.wypisz_wiek()
# Mam 60 l.
# Mam 32 l.
