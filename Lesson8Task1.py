#В первой строке вводится число N. Далее в N строк вводится N чисел (1 ≤ N ≤ 10000), по одному числу на строке.
#Все числа по модулю не превышают 10e5. Переверните массив чисел. Выведите N чисел - перевернутый массив.

N = int(input("Введите количество строк:"))
a = []
while N > 0:
    a.append(int(input("Введите число:")))
    N -= 1
a.reverse()
print(a)
