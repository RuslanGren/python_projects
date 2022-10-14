rA, cA = [int(i) for i in input().split()]
matrixA = [[int(i) for i in input().split()] for _ in range(rA)]
rB, cB = [int(i) for i in input().split()]
matrixB = [[int(i) for i in input().split()] for _ in range(rB)]
matrixC = [[0]*rA for i in range(rA)]
for i in range(rA):
    for j in range(cB):
        for k in range(cA):
            matrixC[i][j] += matrixA[i][k]*matrixB[k][j]
for f in range(cB):
    print(*matrixC[f], end=' ')
    print()