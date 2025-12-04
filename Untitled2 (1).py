def Evclid(a1, a2):
    if a1 == 0:
        return a2
    return Evclid(a2 % a1, a1)
number_1 = input('Введите первое число: ')
number_2 = input('Введите второе число: ')
print(f'НОД: {Evclid (int(number_1), int(number_2))}')