from data import *



def fight(current_enemy0):
    enemy = enemies[current_enemy0]
    while player['hp'] > 0 and enemy_hp > 0:

        print(f'{player["name"]} атакует {enemy["name"]}.')
        enemy_hp -= player['attack']

        print(f'{enemy["name"]} атакует {player["name"]}.')
        player['hp'] -= enemy['attack'] * (1 - player['armor'])
        sleep(1)

        print(f'''{player['name']}: {player['hp']}{enemy['name']}: {enemy_hp}''')
        print()
        sleep(1)

    if player['hp'] > 0:
        print(f'Противник - {enemy["name"]}: {enemy["win"]}')
        current_enemy0 += 1
    else:
        print(f'Противник - {enemy["name"]}: {enemy["loss"]}')
    player['hp'] = 100
    print()
    return current_enemy0






def training(training_type0):
    if training_type0 == '1':
        player['attack'] += 2
        print(f'Тренировка окончена! Теперь ваша величина атаки равна {player["attack"]}')
    elif training_type0 == '2':
        player['armor'] -= .09
        print(f'Тренировка окончена! Теперь броня поглощает {100 - player["armor"] * 100}% урона')
    print()



def display_player():
    print(f'Игрок - {player["name"]}')
    print(f'Величина атаки - {player["attack"]}. Шанс критического урона ({player["attack"] * 3}ед.) равен {player["luck"]}%')
    print(f'Броня поглощает {(1 - player["armor"]) * 100}% урона')
    print()


def display_enemy(current_enemy):
    enemy = enemies[current_enemy]
    print(f'Противник - {enemy["name"]}')
    print(f'Величина атаки - {enemy["attack"]}')
    print(f'Здоровье - {enemy["hp"]}')
    print()



def get_money():
    print('Добро пожаловать в казино! У тебя есть 66.66% шанс получить 500 монет. Соответственно, 33.33% чтобы их потерять')
    result = randint(1, 100)
    sleep(1.5)
    print('Результат....')
    sleep(1.5)
    print('Страшно?!')
    if result < 67:
        print('Вы выиграли 500 монет!')
        player['money'] += 500
    else:
        print('Вы проиграли 500 монет :(')
        player['money'] -= 500
    print()
    print(f'Осталось монет: {player["money"]}')
    print()



def display_inventory():
    print(f'У вас {player["money"]} монет\n')

    for key, value in Inventory.items():
        print(f'{key} = {value}')
    print()



def shop():
    h = input('Добро пожаловать в магазин! Чтобы купить Зелье здоровья(5000) введите 1, Зелье силы(2000) - 2')

    if h == '1':
        if player['money'] >= 5000:
            Inventory['Зелье здоровья'] += 1
            player['money'] -= 5000
            print('Вы купили Зелье здоровья!')
        else:
            print('Недостаточно денег')
    if h == '2':
        if player['money'] >= 2000:
            Inventory['Зелье силы'] += 1
            player['money'] -= 2000
            print('Вы купили Зелье силы!')
        else:
            print('Недостаточно денег')
    else:
        print('Вы неправильно ввели!')
