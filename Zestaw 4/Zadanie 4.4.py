#Zadanie 4.4 - Napisać iteracyjną wersję funkcji fibonacci(n) obliczającej n-ty wyraz ciągu Fibonacciego.

def fibonacci(n):
    if n < 0:
        raise ValueError("Liczba nie może być ujemna")
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        fib = [0, 1]
        for i in range(2, n + 1):
            next_fib = fib[i - 1] + fib[i - 2]
            fib.append(next_fib)
        return fib[n]


print(fibonacci(6))