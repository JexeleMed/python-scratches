owoce = ["jabłko", "ananas", "cytryna"]


print(owoce)

owoce.append("pomarańcza")

print(owoce)

owoce.remove("pomarańcza")

print(owoce)


print(len(owoce))

for owoc in owoce:
    print(owoc)

owoce.remove(owoce[1])

print(owoce)

krotka = (1, 2, 2, 2, 5, 6)
print(krotka)

print(krotka.count(2))


kolory = {"czerwony", "zielony", "pomaranczowy"}


print("czerwony" in kolory)


kolory.add("czarny")

print("czarny" in kolory)

kolory.remove("czarny")

print("czarny" in kolory)

x = 1
y = 8

if x>15:
    print("Wieksza")
elif x<8:
    print("Malutka")
else:
    print("Srednia")

for owoc in owoce:
    print(owoc)

while x < 10:
    print(x)
    x += 1
for liczba in range(1,12):
    if liczba % 2 == 0:
        print(f"{liczba} jest parzysta")
    else:
        print(f"{liczba} jest nie parzysta")


