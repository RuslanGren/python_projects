r, c = [int(i) for i in input().split()]
matrix = [[0]*c for _ in range(r)]
r_now, c_now, r_last, c_last = 0, 0, 0, 0
count = 1
for z in range(r*c):
    if count == r*c+1:
        break
    vector = z % 4
    if vector == 0:
        for i in range(c_last, c - c_last):
            matrix[r_now][i] = count
            count += 1
        c_now = i
        r_last += 1
    if vector == 1:
        for j in range(r_last, r - r_last+1):
            matrix[j][c_now] = count
            count += 1
        r_now = j
        c_last += 1
    if vector == 2:
        for i in range(c - c_last-1, c_last-2, -1):
            matrix[r_now][i] = count
            count += 1
        c_now = i
    if vector == 3:
        for j in range(r - r_last-1, r_last-1, -1):
            matrix[j][c_now] = count
            count += 1
        r_now = j

for l in range(r):
    for k in range(c):
        print(str(matrix[l][k]).ljust(3), end=' ')
    print()