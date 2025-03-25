# instrukcje warunkowe
# instrukcje sterownia przepływem programu
# if
# w zależności od warunku wykona jeden lub drugi blok programu
# warunek zwraca typ bool
# Indent Rainbow Plugin
odp = True
odp = False
if odp:
    # blok programu, wykona sie gdy warunek True
    print("Brawo")
    print("Brawo")
    print("Brawo")
    print("Brawo")

print("Dalsza część programu")

odp = "Radek"
print(bool(odp))  # True

if odp:
    print("Dane zostały odebrane")
    # Dane zostały odebrane

if odp == "Radek":
    print("Radek")  # Radek

odp = 0
if odp:
    print("Działa")
else:  # inny, w przeciwnym przypadku
    print("Zero -> False")  # Zero -> False

a = "Radek"
if len(a) > 3:
    print(f"Długość wynosi: {len(a)}, wiecej niż 3")
# Długość wynosi: 5, wiecej niż 3

a = "Radek"
n = len(a)
if n > 3:
    print(f"Długość wynosi: {n}, wiecej niż 3")
    # Długość wynosi: 5, wiecej niż 3

# operator mors, walrus operator :=
if (n := len(a)) > 3:
    print(f"Długość wynosi: {n}, wiecej niż 3")
# Długość wynosi: 5, wiecej niż 3

# podatek = 0
# zarobki = int(input("Podaj zarobki"))

# # kolejnosć ma znaczenie
# # pierwszy spełniony warunek wychodzi z tego ifa
# if zarobki < 10_000:
#     podatek = 0
# elif zarobki < 40_000:
#     podatek = 0.2
# elif zarobki < 100_000:
#     podatek = 0.4
#
# else:
#     podatek = 0.9
#
# print(f"Podatek wynosi {podatek * zarobki} pln")
# # podatek 0.2 dla zarobków od 10000 do 39999

suma_zam = 150
if suma_zam > 100:
    rabat = 25
else:
    rabat = 0

print(f"Rabat wynosi {rabat}")  # Rabat wynosi 25

rabat = 25 if suma_zam > 100 else 0  # operator warunkowy
print(f"Rabat wynosi {rabat}")  # Rabat wynosi 25

# zasymulujemy system logów
# zmienna będzie przechowywac informacją jaki to system wysłał log
# email, console, inny
# gdy log z systemu console -> "Stało się coś strasznego"
# gdy log z systemu email -> "System email"
# gdy alert_system będzie email
# bedzie druga zmienna przechowująca error, medium inny
# nalezy opis błędu dodac do listy błedó
# error -> "Krytyczny"

alert_system = "email"
error = "error"
lista_b = []

if alert_system == "console":
    print("Stało się coś strasznego")
elif alert_system == "email":
    print("System email")  # Stało się coś strasznego
    if error == "error":
        lista_b.append("Krytyczny")
    elif error == "medium":
        lista_b.append("Ostrzeżenie")
    else:
        lista_b.append("Inny")
else:
    print("Inny")

print(lista_b)  # ['Krytyczny']

# napisac program test z...
punkty = 0
odp = input("Podaj date Chrztu Polski (rok)")
if odp.strip().casefold() == "966":
    punkty += 1  # punkty = punkty + 1
    print("Dobrze")
else:
    print("Musisz się dalej uczyć")

odp = input("Stolica Polski (rok)")
if odp.strip().casefold() == "Warszawa".casefold():
    punkty += 1
    print("Dobrze")
else:
    print("Musisz się dalej uczyć")

print(f"Zdobyłes: {punkty} pkt.")
# Podaj date Chrztu Polski (rok)966
# Dobrze
# Stolica Polski (rok)Warszawa
# Dobrze
# Zdobyłes: 2 pkt.

# spam += 1    spam = spam + 1
# spam -= 1    spam = spam - 1
# spam *= 1    spam = spam * 1
# spam /= 1    spam = spam / 1
# spam %= 1    spam = spam % 1
