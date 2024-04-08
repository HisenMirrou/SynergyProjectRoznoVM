#На берегу реки стояли n рыбаков, все они хотели перебраться на другой берег.
#Одна лодка может выдержать не более m килограмм, при этом в лодку помещается не более 2 человек.
#Определите, какое минимальное число лодок нужно, чтобы перевезти на другой берег всех рыбаков.

fish = int(input("Введите количество рыбаков:"))
weight = int(input("Введите вес который выдержит лодка:"))
boat = 0
mass = [1200, 33,23,55,98]
loosers = 0

while fish > 0:
    fish -= 1
    # mass.append(float(input("Введите вес рыбака:")))
mass.sort()
while len(mass) > 0:
    if mass[-1] > weight:
        mass.pop(-1)
        loosers += 1
    elif len(mass) == 1:
        mass.pop(-1)
        boat += 1
    elif mass[-1] == weight:
        boat +=1
        mass.pop(-1)
    elif mass [-1] < weight:
        cnt = 0
        trd = 0
        while trd < weight and cnt < len(mass) and cnt+1 != len(mass):
           trd = mass[-1] + mass[cnt]
           cnt += 1
        if trd < weight:
            mass.pop(-1)
            mass.pop(cnt - 1)
            boat += 1
        if trd == weight:
            mass.pop(-1)
            mass.pop(cnt-1)
            boat += 1
        elif trd > weight:
            mass.pop(-1)
            boat += 1

print(boat,  "лодок")
print(loosers, "рыбаков осталось на берегу")
