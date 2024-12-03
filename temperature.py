def temp(c):
    
    f = c * 1.8 + 32
    return f

print('Введите значение в градусах Цельсия:')
c = float(input())  
f = temp(c)  
print('Значение в градусах по Фаренгейту =', f)
