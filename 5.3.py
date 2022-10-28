n = int(input())
t = 1
c = 0
while t <= n:
    t*=2
    c+=1
    print(c-1,t//2)
