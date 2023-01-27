# HARD необязательная, идет за 3 обязательных 
# Найдите сумму цифр любого вещественного или целого числа. Можно использовать decimal. Через строку решать нельзя.

number = int(input('введи число: '))
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
print('сумма цифр равна: ', sum)

