names = []
names1 = []
for name in range (0,5):
    name = input("Podaj dowolne imionę:")
    names1.append(name)
    ##print(names1)
for name in names1:
                print("Cześć {}!".format(name))

name = input("Podaj dowolne imiona oddzielone spacją:").split()
names.append(name)
print(names)
for name in names:
                print("Cześć {}!".format(name))
    
