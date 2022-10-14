x = int(input())
A = [[int(i) for i in input().split()] for _ in range(x)]
m = int(input())
Am = [i[:] for i in A]
for z in range(m-1):
    Az = [[0]*x for _ in range(x)]
    for i in range(x):
        for j in range(x):
            for k in range(x):
                Az[i][j] += A[i][k]*Am[k][j]
    Am = Az
for f in range(x):
    print(*Az[f], end=' ')
    print()
