from abc import ABC, abstractmethod


class Ptak(ABC):
    """
    Kalsa opisująca ptaka w pythonie
    """

    def __init__(self, gatunek, szybkosc):
        """
        Metoda inicjalizująca
        :param gatunek:
        :param szybkosc:
        """
        self.gatunek = gatunek
        self.szybkosc = szybkosc

    def latam(self):
        print("Tu", self.gatunek, "Lecę z szybkością", self.szybkosc)

    @abstractmethod  # metoda abstrakcyjna
    def wydaj_odglos(self):
        pass


class Kura(Ptak):
    """
    Klasa Kura dziedziczy po klasie Ptak
    """

    def __init__(self, gatunek):
        # obowiązkowo musimy wywołac konstruktor klasy wyższej
        # super() - klasa wyższa
        super().__init__(gatunek, 0)

    def latam(self):
        print("Tu", self.gatunek, "Ja nie latam.")

    def wydaj_odglos(self):
        print("ko ko ko ko")

    def dziobanie(self):
        print("Tu", self.gatunek, "Idę sobie podziobać")


class Orzel(Ptak):
    """
    Dziedziczy po Ptak
    """

    def wydaj_odglos(self):
        print("Kir kier kir kir")

    def polowanie(self):
        print("Tu", self.gatunek, "Rozpoczynam polowanie")


class Sowa(Ptak):
    """
    Klasa Sowa
    """


# TypeError: Can't instantiate abstract class
# Ptak without an implementation for abstract method 'wydaj_odglos'
# or1 = Ptak("Orzeł", 50)
# or1.latam()  # Tu Orzeł Lecę z szybkością 50
#
# kur1 = Ptak("Kura", 0)
# kur1.latam()  # Tu Kura Lecę z szybkością 0
#
# or1.wydaj_odglos()
# kur1.wydaj_odglos()

kur2 = Kura("Kura")
kur2.latam()  # Tu Kura Ja nie latam.
kur2.wydaj_odglos()  # ko ko ko ko

or2 = Orzel("Orzel Bielik", 50)
or2.latam()  # Tu Orzel Bielik Lecę z szybkością 50
or2.wydaj_odglos()  # Kir kier kir kir

# TypeError: Can't instantiate abstract class Sowa
# without an implementation for abstract method 'wydaj_odglos'
# musi nadpisac metode wydaj_odglos w klasie Sowa
# sowa = Sowa("Sowa", 20)

# polimorfizm - obiekty różnych kals mają wspólny trzon, wydaj_odglos
lista = [kur2, or2]
for i in lista:
    i.wydaj_odglos()
# ko ko ko ko
# Kir kier kir kir

or2.polowanie()  # Tu Orzel Bielik Rozpoczynam polowanie
kur2.dziobanie()
