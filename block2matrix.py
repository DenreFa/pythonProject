"""i, j = int(input()), int(input())
matrix = []
for i in range(i):
    matrix.append([i*j for j in range(j)])
for r in range(i+1):
    for c in range(j):
        print(str(matrix[r][c]).ljust(3), end = '')
    print()"""

n, m = int(input()), int(input()) # Ввод кол-ва строк и столбцов
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
print(maxstr, maxstolb)
