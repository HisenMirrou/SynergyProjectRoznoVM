fish = int(input("Введите количество рыбаков:"))
weight = int(input("Введите вес который выдержит лодка:"))
boat = 0
mass = []
loosers = 0

while fish > 0:
    fish -= 1
    mass.append(float(input("Введите вес рыбака:")))
    mass.sort()
print(len(mass))