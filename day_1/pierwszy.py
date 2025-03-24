# PEP8
# snake_case
import sys

print()  # wydrukuj/wypisz - pusta linia
# ctrl alt l - formatowanie kodu

print("Nazywam się Radek")  # Nazywam się Radek
print("Nazywam się Radek")  # Nazywam się Radek
print("Nazywam się Radek")  # Nazywam się Radek
print("Nazywam się Radek")  # Nazywam się Radek
print("Nazywam się Radek")  # Nazywam się Radek
print("Nazywam się Radek")  # Nazywam się Radek
print("Nazywam się Radek")  # Nazywam się Radek
# ctrl d - powielanie linii
print('Nazywam się Radek')  # Nazywam się Radek
# print('Nazywam się Radek")
#   File "C:\Users\radoslawjaniak\PycharmProjects\pdp-24-03-2025\day_1\pierwszy.py", line 15
#     print('Nazywam się Radek")
#           ^
# SyntaxError: unterminated string literal (detected at line 15)
# Process finished with exit code 1
# ctrl / - komentarz linni z kursorem

# type() - sprawdzenie typu
print(type("Radek"))  # <class 'str'> dane tekstowe
print("39" + "14")  # łaczy stringi, 3914, konkatenacja

print(39 + 14)  # 53
print(type(39))  # <class 'int'> liczby calkowite

# silne typowanie - nie zmienia typów
# print("39" + 14) # TypeError: can only concatenate str (not "int") to str

# rzutowanie
print(int("39") + 14)  # 53 int() - rzutowanie na int
print("39" + str(14))  # 3914 str() - rzutowanie na str

print(5 * "4")  # 44444
print(25 * "168")
print(25 * 168)

# int
print(sys.int_info)
# sys.int_info(bits_per_digit=30,
#              sizeof_digit=4,
#              default_max_str_digits=4300,
#              str_digits_check_threshold=640)

# zmienna - udełko na dane, posiada nazwe
# snake_case

# typowanie dynamiczne
name = "radek"
print(name)
print(type(name))  # <class 'str'>

name = 67
print(name)  # 67
print(type(name))  # <class 'int'>

# podpowiedzi dla programisty
name: str = 90
print(name)
# mypy
#  pip install mypy
# pip install mypy
# (.venv) PS C:\Users\radoslawjaniak\PycharmProjects\pdp-24-03-2025> mypy .\day_1\pierwszy.py
# day_1\pierwszy.py:58: error: Incompatible types in assignment (expression has type "int", variable has type "str")  [assignment]
# day_1\pierwszy.py:63: error: Name "name" already defined on line 54  [no-redef]
# Found 2 errors in 1 file (checked 1 source file)
# (.venv) PS C:\Users\radoslawjaniak\PycharmProjects\pdp-24-03-2025>

age = 50
print(age)
print(type(age))  # <class 'int'>
