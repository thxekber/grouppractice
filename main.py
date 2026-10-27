print("hi")
def f(x):
    a = 1
    b = 1
    for i in range(0, x):
        c = a + b
        a = b
        b = c
    return b

entered = int(input("Enter a number:"))
print(f(entered))