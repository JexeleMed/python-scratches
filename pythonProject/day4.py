# file = open('dane1.txt', 'a+')
#
# print(file)
# file.write("\nTo jest dopiska")
# file.seek(0)
# content = file.read()
# print(content)
#
#
#
#
# file.close()
#
# import os
# print(os.getcwd())
#
#
# try:
#     wynik = 122121 / 0
# except ZeroDivisionError:
#     print("Nie mozna dzizelic przez zero")
#
#
# try:
#     liczba = int(input("Podaj liczbę: "))
# except ValueError:
#     print("To nie jest liczba!!!")
# else:
#     print("Brawo wpisales liczbe")
# finally:
#     print("Operacja zakonczona")
#

try:
    with open('.idea/danka.txt', 'r') as file:
        zawartosc = file.read()
        print(zawartosc)
except FileNotFoundError:
    print("Nie znaleziono pliku")


try:
    with open('.idea/dane1.txt', 'x') as file:
        file.write("Plik zostal utworzony")
except FileExistsError:
    print("Plik juz istnieje")
else:
    print("Utworzono plik")




