m = [random.randint(0, 10) for _ in range(10)]
print(m)
res = []
for el in m:
    if el % 2 != 0:
        res.append(el)


print(sorted(res))