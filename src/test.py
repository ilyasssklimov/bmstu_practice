a = [1, 2]
b = {'a': 2, 'b': 12}

for i, j, k in zip(a, b.items()):
    print(i, j, k)