#На вход подается 1 строка без пробелов. По данной строке определите, является ли она палиндромом
#(то есть, можно ли прочесть ее наоборот, как, например, слово "шалаш"). Необходимо вывести ”yes”,
#если строка является палиндромом, и “no” в противном случае.

tmp = str(input())
a = tmp[::-1]
if tmp == a:
    print("yes")
else:
    print("no")