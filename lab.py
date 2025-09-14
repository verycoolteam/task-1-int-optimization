result = [0, 0]

for i in range (-1*10**6, 10**6 + 1):
    x = int(str(i))
    y = int(str(i))
    if (id(x) == id(y)):
        result[0] = min(i, result[0])
        result[1] = max(i, result[1])

print(result)
