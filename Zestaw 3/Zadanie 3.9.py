#Zadanie 3.9 - Mamy daną listę sekwencji (listy lub krotki) różnej długości zawierających liczby. Znaleźć listę zawierającą sumy liczb z tych sekwencji. Przykładowa sekwencja [[],[4],(1,2),[3,4],(5,6,7)], spodziewany wynik [0,4,3,7,18].

sekwencje = [(1,6), [4], (1, 2), [3, 4], (5, 6, 7)]
sumy = [sum(s) for s in sekwencje]
print(sumy)