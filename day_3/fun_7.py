def connect(**opcje):  # ** argumenty nazwane, kewords arg, słownikowe
    print(opcje)


connect()
connect(a=10)
connect(a=10, name="Radek")  # {'a': 10, 'name': 'Radek'}


def all_args(*args, **kwargs):
    print(args, kwargs)


all_args()  # () {}
all_args(1, 2, 3, 4, 5)
all_args(1, 2, 3, 4, 5, a=10, b=90)
all_args(a=10, b=90)
# () {}
# (1, 2, 3, 4, 5) {}
# (1, 2, 3, 4, 5) {'a': 10, 'b': 90}
# () {'a': 10, 'b': 90}

# all_args(a=10, 1) # SyntaxError: positional argument follows keyword argument
