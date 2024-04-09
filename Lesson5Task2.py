#Дано слово из маленьких латинских букв. Сколько там согласных и гласных букв? Гласными называют буквы «a», «e», «i», «o», «u».
#Для решения задачи создайте переменную и в неё положите слово с помощью input()
#A также определите количество каждой из этих гласных букв Если какой-то из перечисленных букв нет - Выведите False

word = input()
countV = 0
countC = 0
A = 'a'; A1 = 0
E = 'e'; E1 = 0
I = 'i'; I1 = 0
O = 'o'; O1 = 0
U = 'u';U1 = 0

for i in word:
    if i in A:
        A1 += 1
        countV += 1
    elif i in E:
        E1 += 1
        countV += 1
    elif i in I:
        I1 += 1
        countV += 1
    elif i in O:
        O1 += 1
        countV += 1
    elif i in U:
        U1 += 1
        countV += 1
    else:
        countC += 1

if A1 > 0:
    print("a =", A1)
else:
    print("a = false")
if E1 > 0:
    print("e =", E1)
else:
    print("e = false")
if I1 > 0:
    print("i =", I1)
else:
    print("i = false")
if O1 > 0:
    print("o =", O1)
else:
    print("o = false")
if U1 > 0:
    print("u =", U1)
else:
    print("u = false")

print("Количество гласных", countV)
print("Количество согласных", countC)
