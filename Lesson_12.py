import requests
from statistics import mean
#import pprint - не понадобилось

URL = 'https://api.hh.ru/vacancies'

params = {'text': "Python AND Москва"}

result = requests.get(URL, params = params).json()
result_items = result["items"]

salary_list_min = []
salary_list_max = []
salary_average = []
for i in result_items:
    if i["salary"] is not None:
        if i["salary"]["from"] and i["salary"]["to"] is not None:
            salary_list_min.append(i["salary"]["from"])
            salary_list_max.append(i["salary"]["to"])

salary_average = salary_list_min + salary_list_max
average_min = int(round(mean(salary_list_min)))
average_max = int(round(mean(salary_list_max)))
average = int(round(mean(salary_average)))

print('Средняя стартовая зарплата Python-разработчика в Москве равна', average_min, 'рублей')
print('Средняя предельная зарплата Python-разработчика в Москве равна', average_max, 'рублей')
print('Средняя зарплата Python-разработчика в Москве равна', average, 'рублей')
