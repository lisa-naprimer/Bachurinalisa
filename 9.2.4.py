m = int(input('введите колво строк'))
n = int(input('введите колво столбцов'))
a = []
for i in range(m):
    b = []
    for j in range(n):
        print('введите i и j элементы')
        b.append(int(input()))
    a.append(b)
print('изм массив')
for i in range(m):
    for j in range(n):
        if a[i][j]<0: a[i][j]=0
        elif a[i][j]>0: a[i][j]=1
        print(a[i][j], end=' ')
    print()
