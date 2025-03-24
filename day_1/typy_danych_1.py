import sys

wiek = 47  # int
rok = 2025  # int
temp = 36.6  # float

print(temp)
print(type(temp))  # <class 'float'>

print(wiek + rok)
print(wiek - rok)
print(wiek * rok)
print(wiek / rok)  # 0.023209876543209877 float

print(rok // wiek)  # 43, częśc całkowita z dzielenia
print(rok % wiek)  # reszta z dzielenia - modulo
print(5 % 2)  # r1 bo 2 * 2 + 1 = 5

print(wiek ** rok)  # potęgowanie
# len() długość
print(len(str(wiek ** rok)))  # 3386
# print(len(str(wiek ** rok ** 2))) #
# ValueError: Exceeds the limit (4300 a digits) for integer string conversion;
# use sys.set_int_max_str_digits() to increase the limit

print(54 - 5 * 43 + 4 / 2 + 4 / 2)  # -157.0
print(54 - 5 * 43 + (4 / 2 + 4) / 2)  # -158.0

# liczby float mają bład zaokraglenia
print(0.2 + 0.8)  # 1.0
print(0.2 + 0.7)  # 0.8999999999999999
print(0.2 + 0.1)  # 0.30000000000000004
#  the sum 12.345 + 1.0001 = 13.3451 might be rounded to 13.345.
# decimal - do ominięcia problemu zaokrąglenia
print(sys.float_info)
# sys.float_info(max=1.7976931348623157e+308,
#                max_exp=1024, max_10_exp=308,
#                min=2.2250738585072014e-308,
#                min_exp=-1021,
#                min_10_exp=-307,
#                dig=15,
#                mant_dig=53,
#                epsilon=2.220446049250313e-16, radix=2, rounds=1)

print(f"Sprawdzenie zmiennej {temp} {wiek}")  # Sprawdzenie zmiennej 36.6 47
print(f"""
{temp}
    {wiek}""")
# 36.6
#     47

# typ logiczny
# prawda, fałsz
# True, False
# 1, 0
czy_znasz_pythona = True
print(czy_znasz_pythona)
print(type(czy_znasz_pythona))  # <class 'bool'> typ logiczny

print(int(czy_znasz_pythona))  # 1
print(int(False))  # 0

print(bool(1))  # bool() - rzutowanie na typ logiczny, True
print(bool(0))  # bool() - rzutowanie na typ logiczny, False

print(bool(100))  # True
print(bool(-100))  # True
print(bool("Radek"))  # True

print(bool(""))  # False
print(bool(None))  # False None - nic, nie wiem, stan nieokreslony, odpowidnik null



