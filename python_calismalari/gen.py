def f():
    a = 0
    b = 1
    while True:
        yield a
        a, b = b, a + b

for i in f():
    if i >100:
        break
    print(i)