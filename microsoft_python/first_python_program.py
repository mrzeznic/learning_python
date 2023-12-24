# program.py
sum = 1+2
print(sum)

sum = 1 + 2 # 3
product = sum * 2
print(product)

planets_in_solar_system = 8 # int, pluto used to be the 9th planet, but is too small
distance_to_alpha_centauri = 4.367 # float, lightyears
can_liftoff = True
shuttle_landed_on_the_moon = "Apollo 11" #string

distance_to_alpha_centauri = 4.367 # looks like a float
type(distance_to_alpha_centauri) ## <class 'float'>

left_side = 10
right_side = 5
left_side / right_side # 2

from datetime import date

date.today()
print(date.today())

print("Today's date is: " + str(date.today()))

import sys

print(sys.argv)
print(sys.argv[0]) # program name
print(sys.argv[1]) # first arg