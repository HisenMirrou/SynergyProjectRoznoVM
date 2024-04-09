#Вводятся два списка чисел, которые могут содержать до 100000 чисел каждый.
#Все числа каждого списка находятся на отдельной строке. Выведите, сколько чисел содержится одновременно как в первом списке, так и во втором.

string1 = list(map(int, input().split()))
string2 = list(map(int, input().split()))
N = 0
while len(string1) > 0:
    if string1[0] in string2:
        string1.pop(0)
        N += 1
    else:
        string1.pop(0)


print(N)