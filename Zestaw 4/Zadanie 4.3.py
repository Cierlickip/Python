#Napisać iteracyjną wersję funkcji factorial(n) obliczającej silnię.
def factorial(n):
    if n < 0:
        raise ValueError("Liczba nie może być ujemna")
    elif n == 0:
        return 1
    else:
        result = 1
        while n > 0:
            result *= n
            n -= 1
        return result

print(factorial(7))