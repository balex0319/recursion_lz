def triangle(n):
    if n == 1:
        return [[1]] 
    else:
        result = triangle(n-1) 
        current_line = [1]
        previous_line = result[-1] 
        for i in range(len(previous_line)-1):
            current_line.append(previous_line[i] + previous_line[i+1])
        current_line += [1]
        result.append(current_line)
        return result
last = int(input('Введите конечную строку треугольника Паскаля: '))
a = triangle(int(last))
for line in a:
    print(line)
