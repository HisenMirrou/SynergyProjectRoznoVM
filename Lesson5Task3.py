#Два инвестора - Майкл и Иван хотят вложиться в стартап. Фаундеры сказали, что минимальная сумма инвестиций - X долларов,
# больше инвестировать можно сколько угодно. У Майкла A долларов, у Ивана B долларов. Если оба могут вложиться - выведите 2,
# если только Майкл - Mike, если только Иван - Ivan, если не могут по отдельности, но вместе им хватает - 1, если никто - 0.

Ivan = int(input())
Mike = int(input())
Invest = int(input())

if (Ivan >= Invest) and (Mike >= Invest):
    print(2)
elif (Ivan <= Invest) and (Mike <= Invest) and ((Ivan + Mike) >= Invest):
    print(1)
elif (Ivan <= Invest) and (Mike <= Invest) and ((Ivan + Mike) <= Invest):
    print(0)
elif (Ivan >= Invest) and (Mike <= Invest):
    print("Ivan")
else:
    print("Mike")