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

podatek = 0
zarobki = int(input("Podaj zarobki"))

# kolejnosć ma znaczenie
# pierwszy spełniony warunek wychodzi z tego ifa
if zarobki < 10_000:
    podatek = 0
elif zarobki < 40_000:
    podatek = 0.2
elif zarobki < 100_000:
    podatek = 0.4

else:
    podatek = 0.9

print(f"Podatek wynosi {podatek * zarobki} pln")
# podatek 0.2 dla zarobków od 10000 do 39999
