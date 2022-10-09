def ls(x):
    li = [[]]
    for j in range(len(x)):
        for i in range(1, len(x)-j+1):
            li.append(x[i-1:i+j])
    return li
print(ls(input().split()))
