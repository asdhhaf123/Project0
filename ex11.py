# data.py
#data = {[player,enemies,items,magic,perks]}
player = {
    'name': 'Герой',
    'hp': 100,
    'inventory': ['sword', 'shield'],
    'equipped': {
        'weapon': None,
        'shield': None
    },
    'gold': 0,
    'perks': []  # будет выставлен один из перков который будет отвечат за то какая способность будет у игрока
}

enemies = [
    {'name': 'Гоблин', 'hp': 30, 'attack': 5, 'gold_reward': 10, 'spawn_chance': 0.5},
    {'name': 'Орк', 'hp': 50, 'attack': 10, 'gold_reward': 100, 'spawn_chance': 0.25},
    {'name': 'Дракон', 'hp': 100, 'attack': 20, 'gold_reward': 1000, 'spawn_chance': 0.1}
]

items = {
    'sword': {'attack_bonus': 7, 'type': 'weapon'},
    'elite_sword': {'attack_bonus': 20, 'armor_destroy_chance': 0.01, 'type': 'weapon'},
    'shield': {'block_chance': 0.5, 'type': 'shield'},
    'sparta_shield': {'block_scaling': True, 'type': 'shield'},
    'bazooka': {'infinite_damage': True, 'type': 'weapon'}
}

magic = {
    'elements': ['fire', 'water', 'electricity'],
    'combinations': {
        ('fire', 'fire'): {'name': 'meteor', 'damage': 100, 'armor_dependent': True},
        ('fire', 'water'): {'name': 'air_strike', 'shield_destroy': True},
        ('water', 'water'): {'name': 'rejuvenation', 'heal_percent': 0.5},
        ('water', 'electricity'): {'name': 'laser', 'percent_damage': 0.25, 'armor_piercing': True}
    }
}

perks = {
    
    'magic_ability': {'mana': True},
    'cosmic_connection': {'attack_multiplier': 1.5, 'hp_decrease': 0.3},
    'vampirism': {'heal_threshold': 0.2, 'heal_percent': 0.15},
    'extra_turn': {'extra_turn_chance': 2}
    
} 

# func.py
import random

def equip_item(item_name, player, items):
    if item_name in player['inventory']:
        item = items[item_name]
        if item['type'] == 'weapon':
            player['equipped']['weapon'] = item
        elif item['type'] == 'shield':
            player['equipped']['shield'] = item
        player['inventory'].remove(item_name)
        print(f"{item_name} экипирован.")
    else:
        print("У вас нет такого предмета.")
    return player

def show_inventory(player):
    if player['inventory']:
        print("В рюкзаке:")
        for item in player['inventory']:
            print(item)
    else:
        print("Рюкзак пуст.")

def choose_enemy(enemies):
    return random.choices(enemies, weights=[enemy['spawn_chance'] for enemy in enemies], k=1)[0]


def choose_elements(magic):
    chosen_elements = []
    print("Выберите два элемента для магии:")
    for i in range(2):
        element = input(f"Элемент {i+1} (огонь, вода, электричество): ")
        chosen_elements.append(element)
    return tuple(chosen_elements)

def use_magic(elements, player, magic, perks):
    if 'magic_ability' in player['perks']:
        combination = magic['combinations'].get(elements)
        if combination:
            if 'damage' in combination:
                print(f"Вы использовали {combination['name']}!")
                
            elif 'heal_percent' in combination:
                heal = int(player['hp'] * combination['heal_percent'])
                player['hp'] += heal
                print(f"Вы восстановили {heal} HP.")
            elif 'shield_destroy' in combination:
                print("Вы уничтожили щит противника.")
                # уничтожения щита противника
            elif 'percent_damage' in combination and 'armor_piercing' in combination:
                print(f"Вы использовали {combination['name']}!")
                # нанесения процентного урона
        return player
    else:
        print("У вас недостаточно маны для использования магии.")
        return player

def fight(enemy, player):
    while enemy['hp'] > 0 and player['hp'] > 0:
        action = input('''Выберите действие:
1 - Атаковать
2 - Защищаться
''')
        if action == '1':
            player_attack = random.randint(1, 10) + (player['equipped']['weapon']['attack_bonus'] if player['equipped']['weapon'] else 0)
            enemy['hp'] -= player_attack
            print(f"Вы нанесли {player_attack} урона. У {enemy['name']} осталось {enemy['hp']} HP.")
            if enemy['hp'] <= 0:
               print(f"Вы победили {enemy['name']}!")
               player['gold'] += enemy['gold_reward']  # Начисление золота в соответствии с типом врага
               print(f"Вы заработали {enemy['gold_reward']} золота. У вас теперь {player['gold']} золота.")

        elif action == '2':
            if player['equipped']['shield']:
                block_chance = player['equipped']['shield']['block_chance']
                if 'block_scaling' in player['equipped']['shield']:
                    #шанс блока
                    block_chance += player['hp'] / 100
                if random.random() < block_chance:
                    print("Вы заблокировали атаку щитом!")
                    continue
            else:
                print("У вас нет щита для защиты.")
        
        #Ход противника  + - % 
        enemy_attack = enemy['attack']
        player['hp'] -= enemy_attack
        print(f"{enemy['name']} нанес вам {enemy_attack} урона. У вас осталось {player['hp']} HP.")
        if player['hp'] <= 0:
            print("Вы пали в бою... Игра окончена.")
            break
    return player



# main.py
#from data import player, enemies, items, magic
#from func import equip_item, show_inventory, choose_elements, use_magic, fight

current_enemy = None

while True: 
    action = input('''Выбери действие:
1 - В бой!
2 - Показать инвентарь
3 - Информация об игроке
4 - Экипировать предмет
5 - Использовать магию
''')

    if action == '1':
        if not current_enemy or current_enemy['hp'] <= 0:
            current_enemy = choose_enemy(enemies)  # Выбор врага с учетом вероятностей
            print(f"На вас напал {current_enemy['name']}!")
        player = fight(current_enemy, player)
    elif action == '2':
        show_inventory(player)
    elif action == '4':
        item_name = input("Введите название предмета для экипировки: ")
        player = equip_item(item_name, player, items)
    elif action == '5':
        elements = choose_elements(magic)
        player = use_magic(elements, player, magic, perks)
