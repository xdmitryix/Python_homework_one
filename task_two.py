# Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов.
# Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали одинаковое количество журавликов,
# а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе ?


s = int(input('введи общее количество журавликов S: '))
katia = s / 2
petia_serega = katia / 2
print('Катя сделала', round(katia,1), 'журавликов.')
print('Петя и Сережа сделали по', round(petia_serega,1), 'журавликов(ка) каждый.')

# Сделал вывод с одним знаком после запятой т.к. условие не совсем корректное.
# Например при значении S=6: Катя сделает 3 журавлика, а Петя и Сережа по 1.5 т.к они делают одинаковое количество.