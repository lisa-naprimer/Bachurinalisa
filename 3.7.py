def f(a):
    if a % 4 == 0 and a % 400 == 0 and a % 100 != 0:
        return print('yes')
    else:
        return print('no')
aa = int(input())
print(f(aa))
