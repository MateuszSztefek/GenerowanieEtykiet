def fib(n):
    if n < 3:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


def f(n):
    a, b = 0, 1
    for i in range(0, n):
        a, b = b, a + b
    return a


# Fibonacci Series using
# Optimized Method

# function that returns nth
# Fibonacci number
def fiblogn(n):
    F = [[1, 1],
         [1, 0]]
    if (n == 0):
        return 0
    power(F, n - 1)

    return F[0][0]


def multiply(F, M):
    x = (F[0][0] * M[0][0] + F[0][1] * M[1][0])
    y = (F[0][0] * M[0][1] +
         F[0][1] * M[1][1])
    z = (F[1][0] * M[0][0] +
         F[1][1] * M[1][0])
    w = (F[1][0] * M[0][1] +
         F[1][1] * M[1][1])

    F[0][0] = x
    F[0][1] = y
    F[1][0] = z
    F[1][1] = w


def power(F, n):
    if (n == 0 or n == 1):
        return;
    M = [[1, 1],
         [1, 0]];
    power(F, n // 2)
    multiply(F, F)
    if (n % 2 != 0):
        multiply(F, M)


# Driver Code
if __name__ == "__main__":
    print(fiblogn(1000000))
