# -*- coding: utf8 -*-

"""
kalkulator BMR - Basal metabolic rate
- na podstawie wzoru BMR dostępnego np. na wikipedii w konsoli oblicz swoje BMR
"""


height = 170
weight = 63
age = 25
S = -161
PPM = 10 * weight + 6.25 * height + 5 * age + S

print("Dzienne zapotrzebowanie kaloryczne wynosi:", PPM * 1.6, "kcal")
