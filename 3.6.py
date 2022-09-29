r1=int(input("Строка 1=")); c1=int(input("Колонка 1="))
r2=int(input("Строка 2=")); c2=int(input("Колонка 2="))
s1=r1+c1; s2=r2+c2
if s1%2==0:
    b=(s2%2==0)
else:
    b=(s2%2!=0)
if b:
    print("Yes")
else:
    print("No")
