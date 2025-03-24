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
