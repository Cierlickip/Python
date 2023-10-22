#Zestaw 2 - Piotr Cierlicki

#Zadanie 2.10
line = "b aa\n     cccc\n g e fh"
wyrazy = line.split()
print(f"Zadanie 2.10: {len(wyrazy)}\n")

#Zadanie 2.11 - Piotr Cierlicki
wyraz = "word"
wyraz_z_podkreśleniem = "_".join(wyraz)
print(f"Zadanie 2.11: {wyraz_z_podkreśleniem}\n")

#Zadanie 2.12
pierwszy_line = "".join(wyrazy[:3])
drugi_line = "".join(wyrazy[3:])
print(f"Zadanie 2.12:\n pierwszy wyraz - {pierwszy_line}\n drugi wyraz -"
      f" {drugi_line}\n")

#Zadanie 2.13
dlugosc_wyrazow = sum(len(wyraz) for wyraz in wyrazy)
print(f"Zadanie 2.13: dlugosc wyrazow - {dlugosc_wyrazow}\n")

#Zadanie 2.14
najdluzszy_wyraz = max(wyrazy, key=len)
dlugosc_najdluzszego_wyrazu = len(najdluzszy_wyraz)
print(f"Zadanie 2.14:\n najdluzszy wyraz - {najdluzszy_wyraz}\n dlugosc najdluzszego wyrazu - {dlugosc_najdluzszego_wyrazu}\n")

#Zadanie 2.15
L = [1, 3, 2, 6, 7, 1]
napis = "".join(str(x) for x in L)
print(f"Zadanie 2.15:\n ciag liczb - {napis}\n")

#Zadanie 2.16
line = "GvR"
zamiana = line.replace("GvR", "Guido van Rossum")
print(f"Zadanie 2.16:\n zamieniony ciąg - {zamiana}\n")

#Zadanie 2.17
posortowanie_alfabetyznie = sorted(wyrazy)
posortawanie_dlugosc = sorted(wyrazy, key=len)
print(f"Zadanie 2.17:\n sortowanie alfabetycznie - {posortowanie_alfabetyznie}\n sortowanie dlugoscia - {posortawanie_dlugosc}\n")

#Zadanie 2.18
liczba = 100203947262003746300
liczba_zer = str(liczba).count("0")
print(f"Zadanie 2.18: liczba zer - {liczba_zer}\n")

#Zadanie 2.19
L = [1, 2, 11, 32, 5, 234, 761, 32, 8]
napis = ''.join(str(x).zfill(3) for x in L)
print(f"Zadanie 2.19: napis - {napis}")