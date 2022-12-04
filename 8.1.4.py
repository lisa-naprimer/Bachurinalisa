d = int(input())
c = int(input())
b = int(input())
a = int(input())
x = a/b
y = c/d
while x!= 0 and y!=0:
    if x > y:
        x = x % y
    else:
        y = y%x
print(x+y)
print(x/y)