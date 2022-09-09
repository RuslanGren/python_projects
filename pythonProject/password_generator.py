import random
digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_.'
chars = ''
count = int(input('Введіть кількість паролів: '))
lenpasword = int(input('Введіть довжину одного паролю: '))
if input('Чи включати великі літери (y/n) ') == 'y':
    chars += uppercase_letters
if input('Чи включати малі літери (y/n) ') == 'y':
    chars += lowercase_letters
if input('Чи включати символи? (y/n) ') == 'y':
    chars += punctuation
def generate_password(chars, lenght):
    return random.sample(chars, lenght)
for _ in range(count):
    print(*generate_password(chars, lenpasword), sep='')