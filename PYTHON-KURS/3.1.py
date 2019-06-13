# -*- coding: utf8 -*-

"""
A.Utwórz nowy plik, który po podaniu przez użytkownika
długości w cm będzie wyświetlał wynik w metrach i calach
zaokrąglając do 4 miejsc po przecinku.

B.Podobny skrypt możesz wykonać dla zamiany kg na funty.
Wynik wyświetl używając dowolnego sposobu formatowania tekstu.
"""

# Ad. A

cm = int(input("Podaj długość w cm: "))
cm_to_m = cm/100
cm_to_cal = cm/0.394

print("Długość {} cm to {} metrów lub {:.3f} cali".format(cm, cm_to_m, cm_to_cal))

# Ad. B

kg = int(input("Podaj wagę w kg: "))
kg_to_g = kg * 1000
kg_to_funt = kg * 2.4419

print("Waga {}kg to {}g lub {:.4f} funty".format(kg, kg_to_g,kg_to_funt))
