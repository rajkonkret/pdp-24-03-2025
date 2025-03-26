# dekorator - funkcja opakowujaca inną funkcję dodatkową funkcjonalnością
# jako argument przyjmuje funkcję
# wykorzystuje zasady funkcji wewnętrznej
def dekor(funk):
    def wew():
        print("Dekoruj")
        return funk()

    return wew


@dekor  # dekorator
def hej():
    print("Hej!!")


hej()  # Hej!!
# Dekoruj
# Hej!!
