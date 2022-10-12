n, m = int(input()), int(input())
mult = [[0 for _ in range(m)] for _ in range(n)]
for i in range(n):
    for j in range(m):
        temp = str(i*j)
        print(temp.ljust(3), end=' ')
    print()