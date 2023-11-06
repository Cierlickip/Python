#Zadanie 4.5 - Napisać funkcję odwracanie(L, left, right) odwracającą kolejność elementów na liście od numeru left do right włącznie. Lista jest modyfikowana w miejscu (in place). Rozważyć wersję iteracyjną i rekurencyjną.

def odwracanie(L, left, right):
    if left < 0 or right >= len(L) or left >= right:
        raise ValueError("Złe dane")
    while left < right:
        L[left], L[right] = L[right], L[left]
        left += 1
        right -= 1
    return L

def odwracanie_rekurencyjne(L, left, right):
    if left < 0 or right >= len(L):
        raise ValueError("Złe dane")
    elif left >= right:
        return L
    elif left < right:
        L[left], L[right] = L[right], L[left]
        odwracanie(L, left + 1, right - 1)
    return L



L = ['a', 'b', 'c', 'd', 'e', 'f']
L_s = ['a', 'b', 'c', 'd', 'e', 'f']
print(odwracanie(L, 1,  5))
print(odwracanie_rekurencyjne(L_s, 1, 5))