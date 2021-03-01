def fibonacci(n):
    x = 0
    y = 1

    if n==1:
        print(x)
    else:
        print(x)
        print(y)
        for i in range(2,n):
            z = x + y
            x = y
            y = z
            print (z)

print(fibonacci(10))
        