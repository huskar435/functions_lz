def is_even(g):
    if g % 2 == 0:
        return 'Число четное'
    else:
        return 'Число нечетное'

print('Введите число:')
g = int(input())  
result = is_even(g)
print(result)
