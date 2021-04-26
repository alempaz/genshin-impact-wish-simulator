from Wish import wishes

# INVENTORY
inv_five_star_characters = {}
inv_four_star_characters = {}
inv_five_star_weapons = {}
inv_four_star_weapons = {}
inv_three_star_weapons = {}


# ---------------------- Adding to Inventory -------------
# Where x = weapon or character
def add_4star_weapon_inv(x):
    global inv_four_star_weapons
    if x not in inv_four_star_weapons.keys():
        inv_four_star_weapons.update({x: 1})
    else:
        inv_four_star_weapons[x] += 1


def add_5star_weapon_inv(x):
    global inv_five_star_weapons
    if x not in inv_five_star_weapons.keys():
        inv_five_star_weapons.update({x: 1})
    else:
        inv_five_star_weapons[x] += 1


def add_4star_char_inv(x):
    global inv_four_star_characters
    if x not in inv_four_star_characters.keys():
        inv_four_star_characters.update({x: 1})
    else:
        inv_four_star_characters[x] += 1


def add_5star_char_inv(x):
    global inv_five_star_characters
    if x not in inv_five_star_characters.keys():
        inv_five_star_characters.update({x: 1})
    else:
        inv_five_star_characters[x] += 1


def add_3star_weapon_inv(x):
    global inv_three_star_weapons
    if x not in inv_three_star_weapons.keys():
        inv_three_star_weapons.update({x: 1})
    else:
        inv_three_star_weapons[x] += 1


def show_inventory():
    # Color fonts!
    char5 = wishes.Color.YELLOW + '\n5 Star Characters owned:' + wishes.Color.END
    char4 = wishes.Color.PURPLE + '\n4 Star Characters owned:' + wishes.Color.END
    weap5 = wishes.Color.YELLOW + '\n5 Star Weapons owned:' + wishes.Color.END
    weap4 = wishes.Color.PURPLE + '\n4 Star Weapons owned:' + wishes.Color.END
    weap3 = wishes.Color.CYAN + '\n3 Star Weapons owned:' + wishes.Color.END

    # 5 Star Characters
    print('\n', '`~`' * 9, f'{char5}')
    if not inv_five_star_characters:
        print('None')
    else:
        # Where key is name, value is amount of
        for key, value in inv_five_star_characters.items():
            if value <= 7:
                print(f'{key} - C{value - 1} -- Amount Pulled = x{value}')
            elif value > 7:
                print(f'{key} - C6 -- Amount Pulled = x{value}')
    print('')
    # 5 Star Weapons
    print('`~`' * 9, f'{weap5}')
    if not inv_five_star_weapons:
        print('None')
    else:
        # Where key is name, value is amount of
        for key, value in inv_five_star_weapons.items():
            if value <= 5:
                print(f'{key} - R{value} -- Amount Pulled = x{value}')
            elif value > 5:
                print(f'{key} - R5 -- Amount Pulled = x{value}')
    print('')
    # 4 Star Characters
    print('`~`' * 9, f'{char4}')
    if not inv_four_star_characters:
        print('None')
    else:
        # Where key is name, value is amount of
        for key, value in inv_four_star_characters.items():
            if value <= 7:
                print(f'{key} - C{value - 1} -- Amount Pulled = x{value}')
            elif value > 7:
                print(f'{key} - C6 -- Amount Pulled = x{value}')
    print('')
    # 4 Star Weapons
    print('`~`' * 9, f'{weap4}')
    if not inv_four_star_weapons:
        print('None')
    else:
        # Where key is name, value is amount of
        for key, value in inv_four_star_weapons.items():
            if value <= 5:
                print(f'{key} - R{value} -- Amount Pulled = x{value}')
            elif value > 5:
                print(f'{key} - R5 -- Amount Pulled = x{value}')
    print('')
    # 3 Star Weapons
    print('`~`' * 9, f'{weap3}')
    if not inv_three_star_weapons:
        print('None')
    else:
        # Where key is name, value is amount of
        for key, value in inv_three_star_weapons.items():
            if value <= 5:
                print(f'{key} - R{value} -- Amount Pulled = x{value}')
            elif value > 5:
                print(f'{key} - R5 -- Amount Pulled = x{value}')
    wishes.init()


# Future
# def color_names(name, element=None):
#     if element == 'Pyro':
#         return wishes.Color.RED + f'{name}' + wishes.Color.END
#     elif element == 'Hydro':
#         return wishes.Color.BLUE + f'{name}' + wishes.Color.END
#     elif element == 'Cryo':
#         return wishes.Color.DARKCYAN + f'{name}' + wishes.Color.END
#     elif element == 'Electro':
#         return wishes.Color.PURPLE + f'{name}' + wishes.Color.END
#     elif element == 'Geo':
#         return wishes.Color.YELLOW + f'{name}' + wishes.Color.END
#     elif element == 'Anemo':
#         return wishes.Color.CYAN + f'{name}' + wishes.Color.END
#     elif element == 'Dendro':
#         return wishes.Color.GREEN + f'{name}' + wishes.Color.END
#     else:
#         return name
