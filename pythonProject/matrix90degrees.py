x = int(input())
matrix = [input().split() for _ in range(x)]
matrixt = [[0]*x for _ in range(x)]
for i in range(x):
    for j in range(x):
        matrixt[i][j] = matrix[j][i]
for f in range(x):
    matrixt[f].reverse()
    print(*matrixt[f])