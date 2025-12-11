def addition(a, b, c=0):
    if not a and not b and c == 0:
        return ''
    d1 = int(a[-1]) if a else 0
    d2 = int(b[-1]) if b else 0
    summa = d1 + d2 + c
    c = summa // 10
    x = summa % 10
    return addition(a[:-1], b[:-1], c) + str(x)

def main(): 
    a = input('Введите первое число:')
    b = input('Введите второе число:')
    print('Сумма чисел равна: ', addition(a, b))
    d1 = int()
    d2 = int()
if __name__ == "__main__":  
    main()
