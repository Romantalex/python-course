
import time

def time_counter(f):
    def wrap(*args, **kwargs):
        time_before = time.process_time()
        f(*args, **kwargs)
        time_after = time.process_time()
        time_elapsed = time_after - time_before
    return wrap

@time_counter
def list_gen(from_n, to_n):
    list = []
    for i in range (from_n, to_n+1):
        list.append(i)
    return list

@time_counter
def pure_gen(from_n, to_n):
    for i in range (from_n, to_n+1):
        yield (i)

time1_1 = time.process_time()
list1 = list_gen(1, 1000000)
time1_2 = time.process_time()
gen = pure_gen(1, 1000000)
time1_3 = time.process_time()
time_list1 = time1_2 - time1_1
time_gen = time1_3 - time1_2

if time_list1 > time_gen:
    print('Время создания списка больше')
else:
    print('Время создания списка меньше')
