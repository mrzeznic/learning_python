# -*- coding: utf8 -*-

"""
Napisz skrypt, który, który obliczy stan konta za kilka lat.
Program pyta użytkownika o:
- stan początkowy konta,
- stopę oprocentowania rocznego
- liczbę lat na lokacie
Wynik wyświetl jako zdanie używając dowolnego sposobu formatowania tekstu.
Wypisz np. takie zdanie:
Twoje *stan_początkowy* zł przez *czas* lata na lokacie *oprocentowanie* % urośnie do *wynik*.
"""

start = float(input("Stan początkowy konta wynosi: "))

#np. stopa oprocenotwania 6% = 0.06
rate = float(input("Stopa oprocenotowania w skali roku: "))

n = int(input("Liczba lat na lokacie: "))
end = start*(1 + rate*n)

print("Po {} latach kapitał będzie wynosił {} zł".format(n, end))
