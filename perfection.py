def summa(a, b):
    if b == sum(a):
        print('Число совершенное')
    else:
        print('Число несовершенное')

def div(n):
    a = []
    for i in range(1, n):
        if n % i == 0:
            a.append(i)
    return a

def main():
    b = int(input('Введите число: '))
    print(div(b))
    summa(div(b), b)
    
if __name__ == "__main__":  
    main()

