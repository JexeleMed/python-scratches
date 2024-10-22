def dodawanie(a, b):
    return a+b

def powitanie():
    print("Witam dzisiaj")

def suma(*args):
    return sum(args)


def silnia(n):
    if n ==0:
        return 1
    else:
        return n* silnia(n-1)

powitanie()



x = 24.54
y = 12.43
z = 11
c = 55

print(dodawanie(x, y))

print(suma(x, y, z, c))

print("Silnia wynosi: ", silnia(6))



dodaj = lambda a, b: a + b

print(dodaj(x, y))


osoby = [("Anna", 25), ("Jan", 30), ("Kasia", 22)]
osoby.sort(key=lambda x: x[1])  # sortowanie po wieku
print(osoby)  # wynik: [('Kasia', 22), ('Anna', 25), ('Jan', 30)]


liczby = [1, 2, 3, 4]
podwojone = map(lambda x: x * 2, liczby)
print(list(podwojone))  # wynik: [2, 4, 6, 8]


liczby = [1, 2, 3, 4, 5, 6]
parzyste = filter(lambda x: x % 2 == 0, liczby)
print(list(parzyste))  # wynik: [2, 4, 6]
