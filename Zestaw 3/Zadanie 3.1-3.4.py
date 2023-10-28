#Zestaw 3 - Piotr Cierlicki

# Zadanie 3.1
# x = 2; y = 3;
# if (x > y):
#     result = x;
# else:
#     result = y;
# Kod powyżej jest poprawny składniowo. Jednak W Pythonie, średniki nie są wymagane na końcu linii (chociaż są dopuszczalne), a nawiasy wokół warunków if nie są konieczne, chyba że chcemy wyraźnie wydzielić warunek

# for i in "axby": if ord(i) < 100: print (i)
# Kod powyżej niest niepoprawny składniowo. W pythonie nie można używać instrukcji for i if w jednej linii.

# for i in "axby": print (ord(i) if ord(i) < 100 else i)
# Kod jest poprawny składniowo.

# Zadanie 3.2
# L = [3, 5, 4] ; L = L.sort() - Problem wynika z faktu, że L.sort() to metoda listy, która sortuje listę L w miejscu, ale nie zwraca posortowanej listy. Zamiast tego zwraca None. W wyniku przypisania L = L.sort(), zmienna L będzie miała wartość None.
# x, y = 1, 2, 3 - Kod jest nieprawidłowy, ponieważ występuje niezgodna liczba elementów po prawej i lewej stronie
# X = 1, 2, 3 ; X[1] = 4 - Kod jest nieprawidłowy, ponieważ nie można próbiować zmieniać wartość w krotce
# X = [1, 2, 3] ; X[3] = 4 - Kod zawiera błąd indeksowania. W pythonie indeksy w liscie zacznają sięod 0.
# X = "abc" ; X.append("d") - Kod jest nieprawidłowy, ponieważ zmienna X jest łańcuchem, a łańcuchy nie mają metody append()
# L = list(map(pow, range(8)))# - Funkcja map() wymaga dwóch argumentów: funkcji i iterowalnej sekwencji. FUnkcja pow potrzebuje dwa argumenty, bazę i wykładnik

# Zadanie 3.3 - Wypisać w pętli liczby od 0 do 30 z wyjątkiem liczb podzielnych przez 3.
for x in range(0, 31):
    if x % 3 == 0:
        print(x)

# Zadanie 3.4 - Napisać program pobierający w pętli od użytkownika liczbę rzeczywistą x (typ float) i wypisujący x oraz trzecią potęgę x. Zatrzymanie programu następuje po wpisaniu z klawiatury stop. Jeżeli użytkownik wpisze napis zamiast liczby, to program ma wypisać komunikat o błędzie i kontynuować pracę.
while True:
    user_input = input("Proszę wpisać liczbę: ")
    if user_input == 'stop':
        break
    try:
        x = int(user_input)
        y = x ** 3
        print(f"{x} podniesione do potęgi trzeciej wynosi {y}")
    except ValueError:
        print("Błąd. Proszę wprowadzić liczbę.")


