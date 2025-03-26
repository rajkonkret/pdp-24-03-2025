# stworzyc funkcję obliczającą średnią

def liczby(name=None, *cyfry):
    start = 0
    if isinstance(name, str):
        name = name
    else:
        start = int(name)
        name = None
        pass

    print(cyfry, start)
    count = len(cyfry)
    suma = start
    try:
        for c in cyfry:
            suma += c

        avg = suma / count
    except Exception as e:
        print("Błąd", e)
    else:
        print(f"Średnia ucznia {name} wynosi {avg}")
    finally:
        print(f"Koniec obliczeń dla ucznia {name}")


# (1, 2, 3, 4, 5, 6)
# Średnia wynosi 3.5
# Koniec obliczeń dla tego rekordu
# ()
# Błąd division by zero
# Koniec obliczeń dla tego rekordu
# (1, 2, 3)
# Średnia wynosi 2.0
# Koniec obliczeń dla tego rekordu

liczby(1, 2, 3, 4, 5, 6)
# liczby()
liczby(1, 2, 3)
# (1, 2, 3, 4, 5, 6)
# Średnia wynosi 3.5
# Koniec obliczeń dla tego rekordu
# ()
# Błąd division by zero
# Koniec obliczeń dla tego rekordu
# (1, 2, 3)
# Średnia wynosi 2.0
# Koniec obliczeń dla tego rekordu
liczby("Radek", 5, 5, 5, 6, 5, 4, 5)
