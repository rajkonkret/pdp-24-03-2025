class Human:
    """
    Klasa Human opisująca człowieka w pythonie
    """

    def __init__(self, imie, wiek, wzrost, plec="k"):
        """
        Metoda inicjalizująca - konstruktor
        :param imie:
        :param wiek:
        :param wzrost:
        :param plec:
        """

        self.imie = imie
        self.wiek = wiek
        self.wzrost = wzrost
        self.plec = plec

        # self obiekt, który wywołał metode

    def powitanie(self):
        print(f"Nazywam się {self.imie}")

        # wypisz_wiek

    def wypisz_wiek(self):
        print(f"Mam {self.wiek} l.")

    # wypisz_wzrost
    def wypisz_wzrost(self):
        print(f'Mam {self.wzrost} cm wzrostu.')

    def ruszaj(self):

        if self.plec == "k":
            print("Ruszyłam w drogę")
        else:
            print("Ruszyłem w drogę")

    def __str__(self):
        return f"{self.imie}, {self.wiek}, {self.wzrost}, {self.plec}"


# cz1 = Human() # TypeError: Human.__init__() missing 3 required positional arguments: 'imie', 'wiek', and 'wzrost'
cz1 = Human("Anna", 34, 156)
print(cz1.wzrost)  # 156
print(cz1.wiek)  # 34
print(cz1.plec)  # k
print(cz1.imie)  # Anna
print(cz1)  # <__main__.Human object at 0x00000244BE1E9D00>

cz1.powitanie()
cz1.wypisz_wiek()
cz1.wypisz_wzrost()

cz2 = Human("Radek", 45, 189, "m")

cz1.ruszaj()
cz2.ruszaj()
# Ruszyłam w drogę
# Ruszyłem w drogę
print(cz1)
print(cz2)
# Anna, 34, 156, k
# Radek, 45, 189, m
