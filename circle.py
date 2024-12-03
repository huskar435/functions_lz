import math
def circle(b):
    PI = 3.14  # значение const
    c = 2 * PI * b  # формула для нахождения длины окружности
    d = PI * b * b  # формула для нахождения площади окружности
    return c, d
print('Введите радиус круга в см:')

b = float(input())
c, d = circle(b)
print('Площадь окружности =', d)
print('Длина окружности =', c)




