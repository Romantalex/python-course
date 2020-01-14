
# Функция проверки числа на "простоту"

def Simple (num):
   d = 2
   while num % d != 0:
       d += 1
   return d == num

# Функция поиска всех делителей

def alldiv (n):
    result = [1]
    i = 2
    while i <= n:
        if n % i == 0:
            result.append(i)
            i=i+1
        else:
            i += 1
    return result

# Функция поиска наибольшего простого делителя

def max_simple_div (number):
    mins = 2
    while number > 1:
        if number % mins == 0:
            number = number / mins
        else:
            mins += 1
    return mins

