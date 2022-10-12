cord = input()
x, y = ord(cord[0])-97, 8-int(cord[1])
matrix = [['.']*8 for _ in range(8)]
matrix[y][x] = 'N'
for i in range(8):
    for j in range(8):
        if (y-i)**2+(x-j)**2 == 5:
            matrix[i][j] = '*'
    print(*matrix[i])