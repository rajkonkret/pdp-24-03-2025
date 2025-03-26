# stworzyc funkcję kantor
# ma mieć dwie wewnętrne funkcje usd, eur
# w zależności od parametru zwracamy funkcje usd lub eur
def kantor(waluta):
    def usd(kwota):
        return 4.1 * kwota

    def eur(kwota):
        return 4.2 * kwota

    if waluta == "eur":
        return eur  # zwracamy adres funkcji
    else:
        return usd


kantor_eur = kantor("eur")
print(kantor_eur(1000))

kantor_usd = kantor("usd")
print(kantor_usd(1500))

print(kantor_eur(4567))
# 4100.0
# 6149.999999999999
# 18724.699999999997
