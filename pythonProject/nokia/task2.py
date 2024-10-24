lista = list(range(1,101))

nowa_lista = [x**2 if x % 2 == 0 else x**3 for x in lista]
print(nowa_lista)