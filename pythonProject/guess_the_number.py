import random
mx = int(input('Вітаю, введіть максимальне можливе число: '))
x = random.randint(1, mx)
count = 0
def is_valid(s):
    return s.isdigit() and 1 <= int(s) <= mx

while True:
    count += 1
    y = input(f'Вгадайте число від 1 до {mx}: ')
    if not is_valid(y):
        print('Помилка, введіть число від 1 до', mx)
        continue
    y = int(y)
    if y == x:
        print(f'Ви вгадали, вітаю! Ви витратили {count} спроб.')
        break
    if y < x:
        print('Замало, спробуйте ще раз.')
    elif y > x:
        print('Забагато, спробуйте ще раз.')

input('Press ENTER to exit')