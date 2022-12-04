def getMatrix(n):
    n1=n
    count = 0
    a=[]
    maxCount=[]
    maxx = 0
    for i in range(n):
        b = []
        for j in range(n):
            print('Введите [',i,',',j,'] элемент')
            b.append(int(input()))
        a.append(b)
    for i in range(n):
        for j in range(n):
            print(a[i][j], end='')
        print()
    for i in range(n):
        for j in range(n):
            while count < n1:
                if maxx < a[i][j]:
                    maxx = a[i]
                    count+=1
                maxCount.append(maxx)
            count = 0
    print(maxCount)
getMatrix(int(input()))