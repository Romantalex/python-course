#Задача 1

string='0000000000000000000'
for i in range(1,6):
    print (i, string, sep='. ')

#Задача 2

b=0
for i in range (0, 10):
    a=input ('Введите цифру: ')
    if a=='5':
        b=b+1
print ('Количество цифр 5 равно:', b)


#Задача 3

#Задача 4

sum = 1
for i in range(1,11):
    sum*=i
print(sum)

#Задача 6


a = input ('Введите число для расчёта: ')
b = len(a)
c=0
for i in range (0, b):
    c=c+int(a[i])
print (c)

#Задача 7

a = input ('Введите число для расчёта: ')
b = len(a)
c=1
for i in range (0, b):
    c=c*int(a[i])
print (c)

#Задача 9

a = input ('Введите число для расчёта: ')
b = len(a)
c=0
for i in range (0, b):
    g=int(a[i])
    if g>c:
        c=g
print (c)


#Задача 10

a = input ('Введите число для расчёта: ')
b = len(a)
g = 0
c = 0
for i in range (0, b):
    g=int(a[i])
    if g==5:
        c=c+1
print('Количество 5 равно:',c)