
 #Дмитрий, вижу, что громоздко, но ничего лучше не придумалось:) Задание отняло месяц, поскольку хотелось приблизиться к мастерам. Надеюсь, мы всё успеваем.
 #Версия игры со следующими функциями:
    #Игра идёт без добора карт до момента, когда 1 из игроков избавится от всех карт
    #Вроде получилось: определение козыря, определение права первого хода, полуавтоматическое подкидывание
    #Не совсем удалось реализовать: смену хода, взятие карт на руки после невозможности отбить, завершение игры
    #Карты компьютера показаны для отслеживания правильности работы кода
    
import random
from itertools import product

class Allcards:

    type = ["\u2660", "\u2665", "\u2663", "\u2666"]
    ranking = ['6', '7', '8', '9', '10', 'валет', 'дама', 'король', 'туз']
    values = list(range(1, 10))*4

    def __init__(self):
        self.deck0 = list(product(Allcards.type, Allcards.ranking)) #сборка колоды

    def get_values(self):
        self.all_values = dict(zip(self.deck0, Allcards.values)) #базовое старшинство карт
        return self.all_values

    def get_trump(self): #колода тасуется и определяется козырь
        self.deck = self.deck0
        random.shuffle(self.deck)
        self.trump = self.deck[-1]
        return self.trump[0]

    def get_trump_values(self):  #обозначение ранга козырной масти в колоде
        for key, value in self.all_values.items():
            if self.trump[0] == key[0]:
                self.all_values[key] = value+9
        return self.all_values

    def user_cards(self):    #раздача карт пользователю
        self.usercards = []
        self.usercards = self.deck[:6]
        return self.usercards

    def comp_cards(self):    #раздача карт компьютеру
        self.compcards = []
        self.compcards = self.deck[6:12]
        return self.compcards

    def first_turn(self):     #определяем, кто ходит первым по наличию наименьшего козыря или любой карты
        self.first_player = ''
        self.trumpuser = []
        self.trumpcomp = []
        self.trump_range = []
        keycard = []
        all_range = self.usercards + self.compcards
        cardmin = {}
        for i in range(len(self.usercards)):
            if self.trump[0] in self.usercards[i]:
                self.trumpuser.append(self.usercards[i])
        for y in range(len(self.compcards)):
            if self.trump[0] in self.compcards[y]:
                self.trumpcomp.append(self.compcards[y])
        self.trump_range = self.trumpuser + self.trumpcomp
        if self.trump_range != []:
            for k in self.trump_range:
                if k in self.all_values.keys():
                    cardmin[k] = self.all_values[k]
        else:
             for k in all_range:
                 cardmin[k] = self.all_values[k]
        keycard = min(cardmin, key = cardmin.get)
        if keycard in self.usercards:
            self.first_player = 'user'
            return self.first_player
        else:
            self.first_player = 'comp'
            return self.first_player

    def counter_card(self, turncard1, turncard2):     #сохраняем карты, попавшие на стол
        self.common = []
        self.common.append(turncard1)
        self.common.append(turncard2)
        return self.common

    def check_card(self, rest):       #проверяем наличие карт для подкидывания
        self.check = []
        for k in rest:
            for i in self.common:
                if k[1] == i[1]:
                    self.check.append(k)
                else:
                    continue
        return self.check

    def get_minvalue(self, check):   #выбираем наименьшую годную для отбивания карту
        self.mincard = []
        self.mindict = {}
        for k in check:
            self.mindict[k] = self.all_values[k]
        self.mincard = min(self.mindict, key = self.mindict.get)
        return self.mincard

    def compare_cards(self, card1, card2):     #сравниваем ранг карт одной масти
        self.card1 = card1
        self.card2 = card2
        self.c1 = 0
        self.c2 = 0
        for k, v in self.all_values.items():
            if k == self.card1:
                self.c1 = v
            elif k == self.card2:
                self.c2 = v
            else:
                continue

        if self.c1 > self.c2:
            return True
        else:
            return False

    def play_game(self):        #алгоритм самой игры
        result = 'GameOver'
        turn = 0
        usercard = []
        compcard = []
        userchoice = []
        compchoice = []
        turncards = []
        print('Добро пожаловать в "Экспресс-дурака!"', '\n')
        print('Козырь: ', self.trump, '\n')
        print('Ваши карты: ', self.usercards, '\n')
        print('Карты компьютера: ', self.compcards, '\n')
        try:                                                         #начало игры, если первым ходит пользователь
            while self.first_player == 'user':
                turncards = []
                print('Ваш ход: ', '\n')
                turn = int(input('Выберите карту по индексу: '))
                if turn in range(len(self.usercards)):
                    usercard = self.usercards[turn]
                    print(usercard, '\n')
                    while self.usercards != []:         #попытка сохранить цикл до того, как на руках закончатся все карты
                        try:
                            print('Козырь: ', self.trump, '\n')
                            print('Ваши карты: ', self.usercards, '\n')
                            print('Карты компьютера: ', self.compcards, '\n')
                            compchoice = []
                            userchoice = []
                            for card in self.compcards:    #итерация по критериям выбора карты для отбивания
                                if usercard[0] == card[0]:
                                    if self.compare_cards(card, usercard) == True:
                                        compchoice.append(card)
                                elif usercard[0] == self.trump[0] and self.trumpcomp != []:
                                    for trcard in self.trumpcomp:
                                        if self.compare_cards(trcard, usercard) == True:
                                            compchoice.append(trcard)
                                elif usercard[1] == 'туз' and self.trumpcomp != []:
                                    for trcard in self.trumpcomp:
                                        if self.compare_cards(trcard, usercard) == True:
                                            compchoice.append(trcard)
                                elif self.trumpcomp != []:
                                    compchoice.append(self.get_minvalue(self.trumpcomp))
                                else:
                                    continue
                            if compchoice != []:                 #при наличии выбора - следюущие шаги
                                compcard = self.get_minvalue(compchoice)     #функция поиска минимальной годной карты
                                self.counter_card(compcard, usercard)       #сохранение карт со стола для возможности подкидывания
                                turncards.append(self.common)          #громоздко, но попытка собрать все карты со стола в массив
                                self.compcards.remove(compcard)         #удаление сыгранной карты
                                print(compcard, '\n')
                                if compcard in self.trumpcomp:
                                    self.trumpcomp.remove(compcard)
                                self.usercards.remove(usercard)
                                userchoice = self.check_card(self.usercards)    #функция проверки возможности подкидывания
                                if userchoice != []:
                                    usercard = self.get_minvalue(userchoice)  #само автоматическое подкидывание
                                    print(usercard)          
                                    continue
                                else:
                                    self.first_player = 'comp'     #передача хода компьютеру. Прыгал от радости, что сработала, обратный переход - увы...
                                    break
                            else:
                                self.usercards.remove(usercard)       #??? неудачная попытка осуществить взятие карт на руки со стола
                                turncards.append(usercard)
                                self.compcards.append(turncards)
                                break
                        except ValueError:
                            print('Неверный ввод!')
                            pass
                    else:
                        return result      #??? неудачная попытка выйти на завершение цикла
                else:
                    print('Неверный ввод!')
            else:                                         #начало игры, если первым ходит компьютер
                while self.first_player == 'comp':
                    print('Ход компьютера: ', '\n')
                    compcard = self.get_minvalue(self.compcards)     #выбор минимальной карты для инициации игры
                    print(compcard, '\n')
                    turncards = []                 #обнуление стола
                    while self.compcards != []:          #попытка сохранить работу цикла до того, как у компьютера закончатся все карты
                        try:
                            userchoice = []
                            print('Ваши карты: ', self.usercards, '\n')
                            turn = int(input('Выберите карту по индексу: '))
                            if turn in range(len(self.usercards)):           #проверка годности карты для отбивания (заведомого шулерства, так сказать)
                                usercard = self.usercards[turn]
                                if usercard[0] == compcard[0]:
                                    if self.compare_cards(usercard, compcard) == True:
                                        userchoice.append(usercard)
                                elif usercard[0] == self.trump[0]:
                                    if self.compare_cards(usercard, compcard) == True:
                                        userchoice.append(usercard)
                                else:
                                    self.usercards.append(compcard)
                                    print('Неверный ввод! Может быть, вы шулер?', '\n')
                                    continue
                            else:
                                print('Неверный ввод! Может быть, вы шулер?', '\n')
                                continue
                            if userchoice != []:               #функция поиска минимальной годной карты
                                print(usercard, '\n')
                                self.counter_card(compcard, usercard)   #сохранение карт со стола для возможности подкидывания
                                turncards.append(self.common)          #громоздко, но попытка собрать все карты со стола в массив
                                self.compcards.remove(compcard)        #удаление сыгранной карты
                                self.usercards.pop(turn)         #удаление сыгранной карты
                                compchoice = self.check_card(self.compcards)     #функция проверки возможности подкидывания
                                if compchoice != []:
                                    compcard = self.get_minvalue(compchoice)           #само автоматическое подкидывание
                                    print(compcard)
                                    continue
                                else:
                                    self.first_player = 'user'       #??? Попытка передачи хода пользователю, не работает, теряюсь в циклах и не вижу, почему
                                    break
                            else:
                                self.compcards.remove(compcard)        #??? неудачная попытка осуществить взятие карт на руки со стола
                                self.usercards.append(turncards)
                                break
                        except ValueError:
                            print('Неверный ввод!')
                            pass
                    else:
                        self.first_player = 'user'  #??? Настойчивая попытка передачи хода пользователю
        except:
            result = 'GameOver'
            self.first_player = 'user' #??? Настойчивая попытка передачи хода пользователю
            pass
        return result, self.first_player




