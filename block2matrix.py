i, j = int(input()), int(input())
matrix = []
for i in range(i):
    matrix.append([i*j for j in range(j)])
for r in range(i+1):
    for c in range(j):
        print(str(matrix[r][c]).ljust(3), end = '')
    print()