from packet1 import Divisor_master

a = int(input('Введите любое число от 1 до 1000:\n '))
if 1<=a<=1000:
    print('Принадлежит ли введённое число к классу простых: ', Divisor_master.Simple(a))
    print('Список делителей введённого числа: ', Divisor_master.alldiv(a))
    print('Максимальный простой делитель введённого числа: ', Divisor_master.max_simple_div(a))
else:
    print('Введите корректные данные!')