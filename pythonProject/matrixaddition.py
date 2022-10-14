r, c = [int(i) for i in input().split()]
matrixC = [[0]*c for _ in range(r)]
matrixA = [[int(i) for i in input().split()] for _ in range(r)]
matrixB = [[int(i) for i in input().split()] for _ in range(r)]
for i in range(r):
    for j in range(c):
        matrixC[i][j] = matrixA[i][j] + matrixB[i][j]
        print(matrixC[i][j], end=' ')
    print()