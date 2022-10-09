from math import factorial
x = int(input())
for i in range(x):
    print(' '*(x-i), end='')
    for j in range(i+1):
        print(factorial(i) // (factorial(j) * factorial(i - j)), end=' ')
    print('')