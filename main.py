def fibonacci(x):
    a = 1
    b = 1
    for i in range(0, x):
        c = a + b
        a = b
        b = c
    return b
