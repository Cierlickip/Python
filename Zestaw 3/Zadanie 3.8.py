#Zadanie 3.18 - Dla dwóch sekwencji liczb lub znaków znaleźć: (a) listę elementów występujących jednocześnie w obu sekwencjach (bez powtórzeń), (b) listę wszystkich elementów z obu sekwencji (bez powtórzeń).

sekwencja1 = ['a', 'b', 'c', 'd', 3, 2, 6]
sekwencja2 = ['a', 'c', 'd', 'e', 1, 2, 3]

wspolne_elementy = list(set(sekwencja1) & set(sekwencja2))
wszystkie_elementy = list(set(sekwencja1 + sekwencja2))

print("Elementy wspólne:", wspolne_elementy)
print("Wszystkie elementy:", wszystkie_elementy)