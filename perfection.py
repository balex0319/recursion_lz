def perf():
    a = int(input('Введите число: '))
    b = 0
    for i in range(1, a):   
        if a % i == 0:
            b += i
    print('Сумма делителей: ', b)
    if a == b: print('Число совершенное')
    else: print('Число не совершенное')
    return perf()
if __name__== '__main__':
    perf()

def main():
    a = int(input())
    b = 0
if __name__ == "__main__":  
    main()
