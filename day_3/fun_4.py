# funkcja wewnętrzna, zagnieżdzona
# dekorator

def fun1():
    print("To jest fun1")

    def fun2():
        print("To jest fun2")

    return fun2  # zwracamy referencję, adres funkcji


xFun = fun1()
print(xFun)  # <function fun1.<locals>.fun2 at 0x0000017EE7AB0B80>
print(type(xFun))  # <class 'function'>
xFun()
# To jest fun1
# <function fun1.<locals>.fun2 at 0x00000177714C4A40>
# <class 'function'>
# To jest fun2
