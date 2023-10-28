# Zadanie 3.5 - Napisać program rysujący "miarkę" o zadanej długości. Należy prawidłowo obsłużyć liczby składające się z kilku cyfr (ostatnia cyfra liczby ma znajdować się pod znakiem kreski pionowej). Należy zbudować pełny string, a potem go wypisać.
length = input("Proszę podać długość miarki: ")
string = "|...."
measure = ''
number = '0    '
for x in range(1, int(length)+1):
    measure += string
    if x >= 9:
        if x >= 99:
            number = number + str(x) + "  "
            continue
        number = number + str(x) + "   "
        continue
    else:
        number = number + str(x) + "    "

measure += '|'
full_string = measure + '\n' + number
print(full_string)