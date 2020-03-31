

import random
import functools
#1
name_list=['Анна','Георгий','Виктор','Елена','Светлана','Мария','Алексей','Пётр','Святослав','Михаил','Евгения','Надежда','Вера','Любовь','Константин','Вероника','Дмитрий','Ярополк','Тит','Феофан']
print('Список имён: ', name_list[:])

def F (randlist, quant):
    random_list=[]
    len_list=len(randlist)-1
    for i in range (0, quant):
        random_list.insert(i, randlist[random.randint(0, len_list)])
    return random_list

name_list_random=F(name_list, 100)
print(name_list_random)

#2
def maxF (source):
    count=[]
    count=list(map(lambda x: source.count(x), source))
    dictnames={}
    for x, y in zip(source, count):
        dictnames[x]=y
    print(dictnames)
    pop_name=functools.reduce(lambda x, y: x if y <= x else y, dictnames.values())
    return [key for (key, val) in dictnames.items() if val==pop_name]

print('Самые популярные имена:', maxF(name_list_random))

#3
from collections import Counter
def letterF (lF):
    lF = list(map(lambda x: x[0], lF))
    return Counter(lF).most_common()[-1][0]

print('Самая редкая первая буква имени: ', letterF(name_list_random))
