# Напишите программу, которая принимает на вход координаты двух точек
# и находит расстояние между ними в 2D пространстве.

# Пример:

# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21


import math
from random import randrange

A1 = randrange(-10, 10, 1)
A2 = randrange(-10, 10, 1)
B1 = randrange(-10, 10, 1)
B2 = randrange(-10, 10, 1)

print ('Координаты точки А', A1, A2)
print ('Координаты точки B', B1, B2)

print ('Растояние от А до B: ', float(math.sqrt((math.pow((B1 - A1), 2) + math.pow((B2 - A2), 2))))) 
