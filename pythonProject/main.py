x = 12
y = 0


print("Suma: ", (x + y))


print("Roznica", x-y)

print("Iloczyn: ", x*y)

try:
    print("Iloraz", x/y)
    print ("Reszta z dzielenia", (x+1)%y)

except ZeroDivisionError:
    print("Blad! Dzielenie przez 0")

imie = "Anna"
nazwisko = "Kowalska"


print(imie, ",", nazwisko)


print("Inicjaly:", imie[0] + "." + nazwisko[0])
print(imie[0:3])

warzywka =["kabaczek", "brokul", "kalafior", "pomidorek"]


print(warzywka)

warzywka.append("ogoreczek")

print(warzywka)

print(warzywka[1])
print(warzywka[3])


figury = {
    "nazwa": "kwadrat",
    "pole": 25,
    "obwod": 30
}
print(figury)

print(figury["pole"])

try:
    print(figury["adres"])
except KeyError:
    print("Niepoprawny klucz")

print(figury.get("adres"))


print(figury)

figury["przekatna"] = 28
print(figury)


del figury["przekatna"]
print(figury)


for klucz in figury:
    print(klucz)

for wartosc in figury.values():
    print(wartosc)

klucze = figury.keys()
print(klucze)

wartosci = figury.values()
print(wartosci)

pary = figury.items()
print(pary)