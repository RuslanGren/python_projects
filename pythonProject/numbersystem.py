x = int(input('Введіть число: '))
y = int(input('Введіть систему числення: '))
res = ''
vol = [0,1,2,3,4,5,6,7,8,9,"A","B","C","D","E","F"]
while x != 0:
    res += str(vol[x%y])
    x = x//y
print(res[::-1])