def Euclid(a, b):
    if a == 0:
        return b
    return Euclid(b % a, a)

def main():
    a = int(input('Введите первое число: '))
    b = int(input('Введите второе число: '))
    print(f'НОД: {Euclid (int(a), int(b))}')
if __name__ == '__main__':
    main()

