# Магічна квадратна матриця тоді, коли суми по кожному стовпцю, кожному рядку та кожній з двох діагоналей
# рівні між собою, та коли вся матриця построєна з чисел x^2 (без нуля)
x = int(input())
total, total1 = 0, 0
flag = True
wow = [i for i in range(1, x**2+1)]
matrix = [input().split() for _ in range(x)]
for i in range(x):
    for j in range(x):
        total += int(matrix[i][j])
        total1 += int(matrix[j][i])
        if int(matrix[i][j]) in wow and int(matrix[i][j]) != 0:
            wow[int(matrix[i][j])-1] = 0
    if total != total1:
        flag = False
        break
    total, total1 = 0, 0
if flag and sum(wow) == 0:
    print('YES')
else:
    print('NO')