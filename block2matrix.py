"""i, j = int(input()), int(input())
matrix = []
for i in range(i):
    matrix.append([i*j for j in range(j)])
for r in range(i+1):
    for c in range(j):
        print(str(matrix[r][c]).ljust(3), end = '')
    print()"""

"""n, m = int(input()), int(input()) # Ввод кол-ва строк и столбцов
matrix = [input().split() for i in range(n)] # Перевод поданной матрицы в список матричный
indexmaxstr = max([int(matrix[r][c]) for r in range(n) for c in range(m)]) # Нахождение макс эл-та во всей матрице
list2max = [] # Список для максимальных эл-ов у каждой строки
for r in matrix:
    list1 = [] # составление численных списков строк
    for c in range(m):
        list1.append(int(r[c]))
    list2max.append(max(list1)) # Добавление максимальных эл-ов в список
maxstr = list2max.index(indexmaxstr) # Индекс строки
maxstolb = matrix[maxstr].index(str(indexmaxstr)) # Идекс столбца
print(maxstr, maxstolb)"""

"""n, m = int(input()), int(input()) # Строки, столбцы
matrix = [input().split() for _ in range(n)] # матрица в списке
ij = [int(i) for i in input().split()] # номера  столбцов для
i, j = ij[0], ij[1]
for s in matrix: # Обмен столбцов
    s[i], s[j] = s[j], s[i]
for r in range(n): # Вывод матрицы
    for c in range(m):
        print(matrix[r][c], end = ' ')
    print()"""

"""s1 = int(input())
matrix = [input().split() for _ in range(s1)]
for i in range(s1):
        matrix[i][i], matrix[s1-1-i][i] = matrix[s1-1-i][i], matrix[i][i]
for row in matrix:
    print(*row)
"""

"""s1 = int(input())
matrix = [input().split() for _ in range(s1)]
list1 = matrix[::-1]
for row in list1:
    print(*row)"""

s1 = int(input())
matrix = [input().split() for i in range(s1)]
for r in range(s1):
    list1 = []
    for c in range(s1):
        list1.append(matrix[s1-c-1][r])
    print(*list1)


