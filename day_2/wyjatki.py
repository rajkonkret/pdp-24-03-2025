# wyjątek  - bład podczas wykonywannia programu


# print(5 / 0)
# Traceback (most recent call last):
#   File "C:\Users\radoslawjaniak\PycharmProjects\pdp-24-03-2025\day_2\wyjatki.py", line 4, in <module>
#     print(5 / 0)
#           ~~^~~
# ZeroDivisionError: division by zero

try:
    # print(5/0)
    # print("A" * "23")
    # print(int("A"))
    # raise KeyError("Błąd klucza")  # jawne rzucenie błedu
    wynik = 90 / 33
except ZeroDivisionError:
    print("Nie dziel przez zero")
except TypeError:
    print("Bład typu")
except ValueError:
    print("Bład wartosci")
except Exception as e:  # łapie wszystkie pozostałe błędy
    print("Bład:", e)
else:  # tylko gdy nie ma błędu
    print("Wynik:", wynik)
finally:  # blok programu wykonany zawsze
    print("Koniec przetwarzania danych")

print("Program nadal działa...")
# Nie dziel przez zero
# Program nadal działa...
# Bład typu
# Program nadal działa...
# Bład: 'Błąd klucza'
# Program nadal działa...
# Wynik: 2.727272727272727
# Program nadal działa...
# Wynik: 2.727272727272727
# Koniec przetwarzania danych
# Program nadal działa...
