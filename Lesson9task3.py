#Во входную строку водится последовательность чисел через пробел. Для каждого числа выведите слово ”YES” (в отдельной строке),
#если это число ранее встречалось в последовательности или ”NO”, если не встречалось.

numbers = list(map(int, input().split()))
num_before = set()
for num in numbers:
    if num in num_before:
        print('YES')
    else:
        print('NO')
        num_before.add(num)
