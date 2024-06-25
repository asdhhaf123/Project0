from func import *


name = input('Введи своё имя, путник: ')
player['name'] = name

current_enemy = 0


while True:
    action = input('''Выбери действие:
1 - В бой!
2 - Тренировка
3 - Магазин
4 - получить валюту
5 - Показать инвентарь
6 - Информация об игроке
7 - Информация о текущем противнике
''')
    
    if action == '1':
        current_enemy = fight(current_enemy)
    
    if action == '2':
        training_type = input('1 - тренировать атаку, 2 - тренировать оборону')
        training(training_type)


    if action == '3':
        shop()


    if action == '4':
        get_money()

    if action == '5':
        display_inventory()
    
    if action == '6':
        display_player()


    if action == '7':
        display_enemy(current_enemy)

    
    if current_enemy == 3:
        print('Поздравляю! Вы прошли игру!')