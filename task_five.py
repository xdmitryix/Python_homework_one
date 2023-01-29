# HARD необязательная, идет за 3 обязательных 
# Найдите сумму цифр любого вещественного или целого числа. Можно использовать decimal. Через строку решать нельзя.

from decimal import Decimal
number = Decimal(input('введи число: '))
number_float = number
number_round = round(number) 
count = 0
while number_float % 1 != 0:
    number_float *= 10
    count += 1
if count  > 0:
    for i in range(count):
        number *= 10
sum = 0
if number < 0:
    number = abs(number)
if number < 10:
    sum = sum + number
else:    
    while number >= 10:
        sum = sum + number % 10
        number = number // 10
    sum = sum + number
print('сумма цифр равна: ', round(sum))
