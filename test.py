x = 3
y = 100


def fib(y):

    if y <= 1:
        return 1
    return fib(y-1)+fib(y-2)


print(fib(10))
