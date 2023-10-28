#Zadanie 3.10 - Stworzyć słownik tłumaczący liczby zapisane w systemie rzymskim (z literami I, V, X, L, C, D, M) na liczby arabskie (podać kilka sposobów tworzenia takiego słownika). Mile widziany kod tłumaczący całą liczbę [funkcja roman2int()].
# Słownik można utworzyć na kilka sposobów.Używająć zwykłego słownika, używając listy krotek, używając oddzielnych krotek i list.
def roman2int(roman):
    roman_dict = {
        "I" : 1,
        "V" : 5,
        "X" : 10,
        "L" : 50,
        "C" : 100,
        "D" : 500,
        "M" : 1000
    }
    previous_char = 0
    result = 0

    for char in roman[::-1]:
        value = roman_dict[char]
        if value < previous_char:
            result -= value
        else:
            result += value
        previous_char = value

    print(result)

roman2int("MMMDCCXXIV")




