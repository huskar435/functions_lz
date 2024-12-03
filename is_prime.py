def is_prime(a):
    if a <= 1:
        return False
    for i in range(2, int(a**0.5) + 1):
        if a % i == 0:
            return False
    return True

print('Введите число ')
a = float(input())
result = is_prime(a)
if result:
    print('простое число')
else:
    print('не простое число')
