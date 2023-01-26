# Задача 2: Найдите сумму цифр трехзначного числа.

number = int(input('введи трехзначное число: '))
if number < 100 or number > 999:
    print('некорректный ввод числа !')
else:
    result = (number // 100) + (number // 10 % 10) + (number % 10)
    print('сумма равна: ',  result)