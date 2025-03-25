# while - pętla sterowana warunkiem

# pętla nieskońćzona
# while True:
#     print("Kominikat !")

licznik = 0
while True:
    licznik += 1
    print("Komunikat II II")
    if licznik > 10:
        break

print(licznik)  # 11

licznik = 0
while licznik < 10:
    licznik += 1
    print("Komunikat III III")

# password = input("Podaj hasło")
# while password != "secret":
#     password = input("Błędne hasło, podaj ponownie")
# Podaj hasłodsadafas
# Błędne hasło, podaj ponownieasfafa
# Błędne hasło, podaj ponownieasfafaf
# Błędne hasło, podaj ponownieadsafaf
# Błędne hasło, podaj ponowniesecret

lista = []
lista_int = []
while True:
    #   A string is numeric if all characters in the string are numeric
    wej = input("Podaj liczbę")  # str
    if not wej.isnumeric():
        break
    lista.append(wej)
    lista_int.append(int(wej))

print(lista)  # ['1', '2', '3', '4']
print(lista_int)  # [1, 2, 3, 4]

my_list = [1, 5, 2, 3, 5, 4, 5, 6, 5]
element_to_remove = 5
while element_to_remove in my_list:
    my_list.remove(element_to_remove)

print(my_list)  # [1, 2, 3, 4, 6]

my_list = [1, 5, 2, 3, 5, 4, 5, 6, 5]
print(dict.fromkeys(my_list))
# {1: None, 5: None, 2: None, 3: None, 4: None, 6: None}
unique_numbers = list(dict.fromkeys(my_list))
print(unique_numbers)  # [1, 5, 2, 3, 4, 6]
