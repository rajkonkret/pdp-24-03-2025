def all_params(a, b, /, c=42, d=256):
    print(f"{a=}, {b=}")
    print(f"{a=}, {b=}, {c=}, {d=}")


all_params(1, 2)  # a=1, b=2
all_params(1, 2, 3, 4)  # a=1, b=2, c=3, d=4
all_params(1, 2, c=3, d=4)  # a=1, b=2, c=3, d=4
# TypeError: all_params() got some positional-only arguments passed as keyword arguments: 'a, b'
# / argumnty po lewej stronie muszą byc przekazane tylko po pozycji
# all_params(a=1, b=2, c=3, d=4)  # a=1, b=2, c=3, d=4

print(10 * "-")


def all_params_2(a, b, /, c=42, *args, d=256, **kwargs):
    print(f"{a=}, {b=}, {c=}, {d=}")
    print(args)
    print(kwargs)


all_params_2(1, 2)  # a=1, b=2, c=42, d=256
all_params_2(1, 2, 3, 4)  # a=1, b=2, c=3, (4,)
all_params_2(1, 2, 3, 4, 5)  # a=1, b=2, c=3, (4, 5)
all_params_2(1, 2, 3, 4, 5, 6, 7, 8, 9, d=78)
# a=1, b=2, c=3, d=78
# (4, 5, 6, 7, 8, 9)
# {}
all_params_2(1, 2, 3, 4, 5, 6, 7, 8, 9, d=78, e=90, h=99, name="Radek")
# a=1, b=2, c=3, d=78
# (4, 5, 6, 7, 8, 9)
# {'e': 90, 'h': 99, 'name': 'Radek'}
all_params_2(1, 2, 3, 4, 5, 6, 7, 8, 9, d=78, e=90, h=99, name="Radek", a=199)
# a trafia do słownika
# a=1, b=2, c=3, d=78
# (4, 5, 6, 7, 8, 9)
# {'e': 90, 'h': 99, 'name': 'Radek', 'a': 199}
