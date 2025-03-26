# funkcja - wykonuje fragment kodu w dowolnym momencie
# funkcja musi być najpierw zadeklarowana
# w miejscu deklaracji dunkcja się nie wykonuje
# żeby uruchomić funkcję trzeba ją wywołać

# argumenty globalne
a = 8
b = 6


# funkcje nie zwracające wyniku
# definicja funkcji
def dodaj():  # funkcja bezargumentowa
    print(a + b)


def dodaj_1(a, b):  # a, b argumenty obowiązkowe
    # lokalne a i b
    print(a + b)


# pozwala ominąc problem przeciązania funkcji liczbą argumentów
def odejmj(a, b, c=0):  # c - argument domyślny
    print(a - b - c)


# wywołanie funkcji
dodaj()  # 14
# dodaj_1() # TypeError: dodaj_1() missing 2 required positional arguments: 'a' and 'b'

# argumenty po pozycji
dodaj_1(15, 67)  # 82

odejmj(1, 2, 3)
odejmj(1, 2)  # c=0

# argumenty po nazwie
odejmj(b=7, a=8, c=89)  # -88
odejmj(b=7, a=8)  # -88
dodaj_1(b=9, a=87)

# argumenty mieszane
odejmj(1, 2, c=9)

# odejmj(c=9, b=8, 1)  # SyntaxError: positional argument follows keyword argument

# print(dodaj() + dodaj()) # TypeError: unsupported operand type(s) for +: 'NoneType' and 'NoneType'
