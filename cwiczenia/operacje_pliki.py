"""
https://kamil.kwapisz.pl/nauka-podstaw-pythona-obsluga-plikow/
“r” – plik otwarty do odczytu (read)
“w” – plik otwarty do zapisu (write), przed zapisem zawartość pliku jest usuwana
“a” – plik otwarty do zapisu, dodaje nową treść na końcu pliku, nie usuwa starej (append)
"""

plik_odczyt = open("notatnik.txt", "r")  # otwarcie pliku

"""
tresc = plik_odczyt.read() #argument to liczba znakow moze byc pusty wtedy odczyta caly plik
tresc = plik_odczyt.readline() #czyta jedna linie
lista = plik_odczyt.readlines() #czyta wiele linii
for linia in tresc:
    print(linia)

"""

#print(type(lista)) #teraz to lista

#czytanie po znaku
"""
znak = plik_odczyt.read(1)
while znak:
    print(znak)
    znak = plik_odczyt.read(1)
"""

plik_zapis = open("notatnik.txt", "w")  # otwarcie pliku
plik_zapis.write(input("Podaj co zapisac do pliku"))
