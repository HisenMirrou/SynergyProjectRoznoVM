#С помощью цикла создайте словарь, в котором ключи будут, например от числа 10, до -5 (включительно).
#А значениями этих ключей будут сами эти числа возведённые в степени равных этим числам

diction = {}
numbers = list(map(int, input().split()))

for i in numbers:
    diction[i] = i**i
print(diction)

