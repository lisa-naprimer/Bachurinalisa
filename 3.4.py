a = int(input())
b = int(input())
L = int(input())
K = int(input())
def f(a,b,L,K):
 return (2*L + a + (2*b + 2*a)*(K-1))
print(f(a,b,L,K))
