#Zadanie 3.6 - Napisać program rysujący prostokąt zbudowany z małych kratek. Należy zbudować pełny string, a potem go wypisać. Przykładowy prostokąt składający się 2x4 pól ma postać:
def rysuj_prostokat(wysokosc, szerokosc):
    gorna_krawedz = "+---" * szerokosc + "+"
    wnetrze = "|   " * szerokosc + "|"
    string = gorna_krawedz + '\n' + wnetrze + '\n'
    full_string = string * wysokosc + gorna_krawedz
    print(full_string)

wysokosc = 4
szerokosc = 6
rysuj_prostokat(wysokosc, szerokosc)