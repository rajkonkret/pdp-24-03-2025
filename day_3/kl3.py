class Car:
    """
    Klasa opisująca samochód w pythonie
    """

    def __init__(self, model, year):
        """
        Metoda inicjalizująca
        :param model:
        :param year:
        """
        self.model = model
        self.year = year
        # pole prywatne, hermetyzacja
        self.__predkosc = 0

    def gaz(self):
        self.__predkosc += 10

    def licznik(self):
        print(f'Prędkość wynosi {self.__predkosc} km/h')

    def hamuj(self):
        self.__predkosc -= 10
        self.__zmien_bieg()

    def __zmien_bieg(self):
        print("Zmiana biegu")


# hermetyzacja - zablokowanie widoczności pól spoza klasy
# enkapsulacja - wystawienie metod do zapisu i odczytu zahermetyzowanych pól

# tu jesteśmy poza klasą
car = Car("Mitsubishi", 2025)
car.gaz()
car.gaz()
car.gaz()
car.gaz()
car.gaz()
# pole prywatne
# AttributeError: 'Car' object has no attribute '__predkosc'. Did you mean: '_Car__predkosc'?
# print(car.__predkosc)  # 50
car.licznik()  # Prędkość wynosi 50 km/h
car.__predkosc = 0
car.licznik()  # Prędkość wynosi 50 km/h
car.hamuj()
car.hamuj()
car.hamuj()
car.hamuj()
car.hamuj()
car.licznik()  # Prędkość wynosi 0 km/h
# Prędkość wynosi 50 km/h
# Prędkość wynosi 50 km/h
# Zmiana biegu
# Zmiana biegu
# Zmiana biegu
# Zmiana biegu
# Zmiana biegu
# Prędkość wynosi 0 km/h
