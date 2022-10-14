x = input().split()
r, c = int(x[0]), int(x[1])
matrix = [[0]*c for _ in range(r)]
for i in range(r):
    for j in range(c):
        matrix[i][j] = (i+j)%c+1
        print(matrix[i][j], end=' ')
    print()