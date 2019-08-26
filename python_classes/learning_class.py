# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 12:13:24 2019

@author: MRZEZNIC
"""

class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

my_animal = Animal(name='Kitty', age=2)

print(my_animal.name)
print(my_animal.age)
