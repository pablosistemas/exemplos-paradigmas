fib_v = None
fib = None

def fibonacci(n):
    if fib_v[n] == -1:
        fib_v[n-1] = fibonacci(n-1)
        fib_v[n-2] = fibonacci(n-2)
        return fib_v[n-1] + fib_v[n-2]
    else:
        return fib_v[n]

def main():
    global fib_v, fib
    fib = 100
    fib_v = [-1 if i != 0 and i != 1 else 0 if i == 0 else 1 for i in range(fib + 1)]
    resultado = fibonacci(fib)
    print(resultado)

if __name__ == "__main__":
    main()
