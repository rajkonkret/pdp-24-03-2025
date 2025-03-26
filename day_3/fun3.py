a = 10
b = 10


def dodaj():
    a = 7
    b = 10  # wartości lokalne
    print(a + b)


def dodaj_2():
    print(a + b)


def dodaj_3():
    global a  # uzyj a globalne
    a = 9  # nadpisze globalne a
    b = 89
    print(a + b)


print(f"Wartość a z góry {a=} (globalna)")  # Wartość a z góry a=10 (globalna)
dodaj()  # 17
print(f"Wartość a z góry {a=} (globalna)")  # Wartość a z góry a=10 (globalna)
dodaj_2()  # 20
print(f"Wartość a z góry {a=} (globalna)")  # Wartość a z góry a=10 (globalna)
dodaj_3()  # 98
print(f"Wartość a z góry {a=} (globalna)")  # Wartość a z góry a=9 (globalna)
dodaj_2()  # 19
