def triangle(n):
    if n == 1:
        return [[1]] 
    else:
        a = triangle(n-1) 
        b = [1]  # b - исходная строка 
        c = a[-1] # c - предыдущая строка
        for i in range(len(c)-1):
            b.append(c[i] + c[i+1])
        b += [1]
        a.append(b)
        return a

def main():
    last = int(input('Введите конечную строку треугольника Паскаля: '))
    d = triangle(int(last))
    for line in d:
        print(line)
if __name__ == '__main__':
    main()
