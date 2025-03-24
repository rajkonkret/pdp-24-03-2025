user = "Tomek"  # str
wiek = 39  # int
wersja = 3.90001  # float, liczby zmiennoprzecinkowe
print(type(wersja))
liczba = 456789098765  # int

print("Witaj %s, masz teraz %d lat." % (user, wiek))  # Witaj Tomek, masz teraz 39 lat.
# sprawdza typ %d - liczba
# print("Witaj %d, masz teraz %s lat." % (user, wiek)) # TypeError: %d format: a real number is required, not str
print("Witaj %(user)s, jesteś %(user)s" % {"user": user})  # Witaj Tomek, jesteś Tomek

print(f"Wiataj {user}, masz teraz {wiek} lat.")  # Wiataj Tomek, masz teraz 39 lat.

print("Używamy wersji pythona %i" % 3)  # Używamy wersji pythona 3
print("Używamy wersji pythona %f" % 3)  # Używamy wersji pythona 3.000000
print("Używamy wersji pythona %.2f" % 3.9)  # Używamy wersji pythona 3.90
print("Używamy wersji pythona %.1f" % 3.9)  # Używamy wersji pythona 3.9
print("Używamy wersji pythona %.0f" % 3.9)  # Używamy wersji pythona 4 - zaokraglone
print("Używamy wersji pythona %.f" % 3.9)  # Używamy wersji pythona 4 - zaokraglone

x = 3.8769
print(x)  # 3.8769
print("%.2f" % x)  # 3.88
print(type("%.2f" % x))  # <class 'str'>
print(x)  # 3.8769

print(round(x, 2))  # 3.88
print(type(round(x, 2)))  # <class 'float'>

print(f"Uzywamy wersji pythona {wersja}")  # Uzywamy wersji pythona 3.90001
print(f"Uzywamy wersji pythona {wersja:.2f}")  # Uzywamy wersji pythona 3.90
print(f"Uzywamy wersji pythona {wersja:.1f}")  # Uzywamy wersji pythona 3.9
print(f"Uzywamy wersji pythona {wersja:.0f}")  # Uzywamy wersji pythona 4

print(f"{user:<10}")  # "Tomek     "
print(f"{user:>20}")  # "               Tomek"
print(f"{user:^20}")  # "       Tomek        "

print(liczba)  # 456789098765
print(f"Nasza duza liczba {liczba:,}")  # Nasza duza liczba 456,789,098,765
print(f"Nasza duza liczba {liczba:_}")  # Nasza duza liczba 456_789_098_765
print(f"Nasza duza liczba {liczba:_}".replace("_", " "))  # Nasza duza liczba 456 789 098 765
print(f"Nasza duza liczba {liczba:_}".replace("_", "."))  # Nasza duza liczba 456.789.098.765

liczba = 1500000000000
liczba = 1_500_000_000_000
print(type(liczba))  # <class 'int'>
print(liczba)
