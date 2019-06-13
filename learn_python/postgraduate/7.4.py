times=int(input("Ile razy ma wykonać się program?\n"))
print("Program wykona się {} razy.".format(times))
for i in range (0,times):
    number = int(input("Podaj dowolną liczbę: \n"))
    print("Podana przez Ciebie liczba {} jest wielokrotnością 3? {}".format(number,number%3==0))
    print("Podana przez Ciebie liczba {} jest wielokrotnością 4? {}".format(number,number%4==0))
    result = (number%3==0) and (number%4==0)
    print(result)
    print("Podana przez Ciebie liczba {} jest wielokrotnością 4 oraz jest wielokrotnością 3? {}".format(number, result))
