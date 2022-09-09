li = []
step = ''
cryption, count = 0, 0
text = input()
for j in range(len(text)):
    if text[j].isalpha():
        count += 1
    else:
        step += str(count)*count
        count = 0
        step += str(0)
step += str(count)*count
for i in range(len(text)):
    if text[i].isalpha():
        if text[i].isupper():
            cryption = ord(text[i]) + int(step[i])
            while cryption > 90:
                cryption -= 26
            li.append(chr(cryption))
        else:
            cryption = ord(text[i]) + int(step[i])
            while cryption > 122:
                cryption -= 26
            li.append(chr(cryption))
    else:
        li.append(text[i])
print(*li, sep='')