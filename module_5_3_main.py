# Домашняя работа по уроку "Перегрузка операторов."

from module_5_3 import House
# from module_5_3 import *

h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

print(h1)
print(h2)

print(h1 == h2, 'h1 == h2')
h1 = h1 + 10
print(h1)
print(h1 == h2, 'h1 == h2')

h1 += 10
print(h1)

h2 = 10 + h2
print(h2)

print(h1 > h2, 'h1 > h2') # __gt__
print(h1 >= h2, 'h1 >= h2') # __ge__
print(h1 < h2, 'h1 < h2') # __lt__
print(h1 <= h2 , 'h1 <= h2') # __le__
print(h1 != h2, 'h1 != h2') # __ne__

print(h1 * 2)
print(h1 - 2)
print(100 - h1)
print(h1 // 2)
print(h1 / 2)
print(h1 // 2)
print(h2 * 2)
print(h2 // 2)