#Вводятся целые числа A и B. Гарантируется, что A ≤ B. Выведите все четные числа на заданном отрезке через пробел.

a = int(input())
b = int(input())
n = []
for i in range(a, b+1):
    if i % 2 == 0:
        n.append(i)
print(n)