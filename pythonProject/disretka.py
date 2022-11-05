x = [int(z) for z in input('Введіть список, через пробіл в один рядок: ').split()]
n = int(input('Введіть значення максимального елемента: '))
r = len(x)
i = r - 1
for k in range(r):  # Перевірка коректності списка
    if x[k] > (n - r + k):
        print('Помилка, список неправильний')
        i = -1
        break
while i >= 0:
    if x[i] != (n - r + i + 1):
        x = x[:i] + [x[i] + j - i + 1 for j in range(i, r)]
        i = r - 1
        print(x)
    else:
        i -= 1
