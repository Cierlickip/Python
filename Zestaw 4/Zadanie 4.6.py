#Zadanie 4.6 - Napisać funkcję sum_seq(sequence) obliczającą sumę liczb zawartych w sekwencji, która może zawierać zagnieżdżone podsekwencje. Wskazówka: rozważyć wersję rekurencyjną, a sprawdzanie, czy element jest sekwencją, wykonać przez isinstance(item, (list, tuple))

def sum_seq(sequence):
    result = 0
    for item in sequence:
        if isinstance(item, (list, tuple)):
            result += sum_seq(item)
        elif isinstance(item, int):
            result += item
    return result



sekwencje = [(1,6), [4], (1, 2), [3, 4], (5, 6, 7)]
print(sum_seq(sekwencje))