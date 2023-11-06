#Rozwiązania zadań 3.5 i 3.6 z poprzedniego zestawu zapisać w postaci funkcji, które zwracają pełny string przez return. Funkcje nie powinny pytać użytkownika o dane, tylko korzystać z argumentów.

def rysuj_miarke(dlugosc):
    string = "|...."
    measure = ''
    number = '0    '
    for x in range(1, int(dlugosc) + 1):
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
    return full_string


def rysuj_prostokat(wysokosc, szerokosc):
    gorna_krawedz = "+---" * szerokosc + "+"
    wnetrze = "|   " * szerokosc + "|"
    string = gorna_krawedz + '\n' + wnetrze + '\n'
    full_string = string * wysokosc + gorna_krawedz
    return full_string

dlugosc = 10
wysokosc = 4
szerokosc = 6
print(rysuj_miarke(dlugosc) + '\n')
print(rysuj_prostokat(wysokosc, szerokosc))