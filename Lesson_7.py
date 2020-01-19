from docxtpl import DocxTemplate
import csv
import json
import random

#Читаем файл и выбираем случайную марку автомобиля
with open('Car_info.txt') as file:
    car_rand = []
    reader = csv.reader(file)
    for row in file:
        car_rand.append(row)
report_car = car_rand[random.randint(0, len(car_rand)-1)]
car_info = report_car.split()

#Генерируем автоматический отчёт о выбранном автомобиле
def get_data (Brand, Model, Fuel_cons, Price):
    return {
        'Brand': Brand,
        'Model': Model,
        'Fuel_cons': Fuel_cons,
        'Price': Price
    }

def from_template(Brand, Model, Fuel_cons, Price, template):
    template = DocxTemplate(template)
    data = get_data(Brand, Model, Fuel_cons, Price)
    template.render(data)
    template.save('Car_info1.docx')

def report(Brand, Model, Fuel_cons, Price):
    template = 'Car_info_template.docx'
    document = from_template(Brand, Model, Fuel_cons, Price, template)

report(car_info[0], car_info[1], car_info[2], car_info[3])

#Создаём csv файл
car_list=[]
with open('Car_info.txt', 'r') as file:
    for row in file:
        inner_list = [x.strip() for x in row.split(',')]
        car_list.append(inner_list)
print(car_list)
with open('car.csv', 'w') as file:
        writer = csv.writer(file, delimiter = '*')
        writer.writerows(car_list)

#Создаём json файл
with open('Car_json.txt', 'w') as f:
    json.dump(str(car_info), f)


