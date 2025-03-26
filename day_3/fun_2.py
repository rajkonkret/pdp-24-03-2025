# funkcja zwracająca wynik
# końćzy się słówkiem return
# gdy napotka na return zwraca wynik i wychodzi z funkcji

def dodaj(a, b):
    return a + b


print(dodaj(5, 7))  # 12


def odejmij(a, b=0, c=0):
    return a - b - c


print(odejmij(7, 2, 3))  # 2


def oblicz_vat(kwota, vat=23):
    return kwota * (100 + vat) / 100


print(oblicz_vat(1000))  # 1230.0
print(oblicz_vat(1000, 8))  # 1230.0
print(oblicz_vat(vat=15, kwota=1000))  # 1150.0

zm = oblicz_vat(1000)

if zm == 1230:
    print("OK")  # OK

print(dodaj(6, 9) + dodaj(78, 98))  # 191
