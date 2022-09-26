import math
x = float(input())
y = float(input())
z = float(input())

a = 2*math.cos(x - 2/3)/(1/2+(math.sin(y)**2))*(1+(z**2)/(3-z**2)/5)
print('Ответ: ', a)
