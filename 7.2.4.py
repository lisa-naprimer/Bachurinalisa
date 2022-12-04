import random
m = [random.randint(0, 10) for _ in range(10)]
res = []
for ch in m:
    if ch % 2 != 0:
        res.append(ch)

print(m)
print(sorted(res))