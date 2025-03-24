from calendar import prweek

tekst = "Witaj Świecie"
print(tekst)
print(type(tekst))  # <class 'str'>

# teksty są niemutowalne
# """ Return a copy of the string converted to uppercase. """
tekst.upper()
print(tekst)  # Witaj Świecie

print(tekst.upper())  # WITAJ ŚWIECIE
tekst_upper = tekst.upper()
print(tekst_upper)  # WITAJ ŚWIECIE
print(tekst)  # Witaj Świecie

# małe litery, capitalize
print(tekst.lower())  # witaj świecie
print(tekst.capitalize())  # Witaj świecie
print(tekst.swapcase())  # wITAJ śWIECIE

print(tekst)  # Witaj Świecie

# Witaj Świecie
# 0123456789... indeksy numerowane od 0

print(tekst[6])  # Ś
print(tekst.index("Ś"))  # indeks 6
print(tekst.index("i"))  # indeks 1
print(tekst.count("i"))  # występuje 3 razy

print(tekst.count("j", 0, 4))  # wystepuje 0 razy, bo indeksy 0123
print(tekst[4])  # "j"

print(tekst.removeprefix("Witaj"))  # " Świecie"
print(tekst.removesuffix("Świecie"))  # "Witaj "

# usunięcie białych znaków (spacji)
print(tekst.removesuffix("Świecie").strip())  # "Witaj"

name = "   Radek   "
print(name.rstrip())  # "   Radek"
print(name.lstrip())  # "Radek   "

tekst_zamiana = "Witaj Dobry Świecie"
print(tekst_zamiana.replace("Dobry", ""))  # "Witaj  Świecie"

encode_s = tekst.encode('utf-8')
print(encode_s)  # b'Witaj \xc5\x9awiecie' dane typu bajtowego
print(type(encode_s))  # <class 'bytes'>
# \xc5\x9a w zapisie szesnastkowym, 197, 154
# \xc5\x9a kod litery "Ś"  w utf-8
print(encode_s.decode('utf-8'))  # "Witaj Świecie"

imie = "Radek"
# f string, string sformatowany
tekst_format = f"Mam na imię {imie} i lubię Pythona."
print(tekst_format)  # Mam na imię Radek i lubię Pythona.

tekst_format = f"\tMam na imię {imie}\n i lubię pythona.\b"
print(tekst_format)
# "	  Mam na imię Radek
#  i lubię pythona"
# \t - tabulator
# \n - nowa linia
# \b - backspace

starszy = "Witaj %s!"  # %s - w to miejsce podstawi string
print(starszy % imie)  # Witaj Radek!

print("Witaj {}!".format(imie))  # Witaj Radek!

print("Witaj", imie)

print("""Tekst
    wielolinijkowy""")
# "Tekst
#     wielolinijkowy"

"""Komentarz
 wielolinijkowy"""
