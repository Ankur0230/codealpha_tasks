def fibo(num):
    a, b = 0, 1
    for i in range(num):
        yield "{}:: {}".format(i + 1,a)
        a, b = b, a + b
for item in fibo(100):
    print(item)