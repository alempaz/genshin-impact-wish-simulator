import random
from Wish import wishes
from Inventory import inventory as inv
from Inventory import list_comb as lst, list_com_banners as lstbn
from Banners import promo_pity as pp

# pulls used to check inventory
gacha = []
# pulls used to print in console
gacha_show = []

banner_name = 'weapon'


def show_pulls():
    global gacha_show

    print('`~`' * 3, ' Obtained ', '`~`' * 3)
    for _ in gacha_show:
        print(f'{_}')
    wishes.init()


def weapon_banner(limit):
    """
    Banner contains all 5* standard weapons
    Banner contains all standard 4* characters and 4* weapons
    Promotional 5* weapons with higher drop rate are 'Redhorn Stonethresher' and 'Skyward Harp'
    Promotional 4* weapons are 'Mitternachts Waltz, 'The Alley Flash, 'Sacrificial Fragments', 'The Bell',
    'Favonius Lance'.

    5 Star Hard Pity is configured at 80, having higher probability of getting a 5 star after 64 (soft pity)
    4 Star Hard Pity is configured at 9

    Percentages:
    93.3% Chance to get a 3 Star
    5.1% Chance to get a 4 Star
    0.7% Chance to get a 5 Star
    """
    global gacha
    global gacha_show

    # Empty gatcha pulls
    gacha = []
    gacha_show = []

    # Weighted list for pull percentages (0.7% - 5.1% - 93.3%)
    # https://stackoverflow.com/questions/14992521/python-weighted-random
    og_pull_percentage = ['3'] * 933 + ['4'] * 51 + ['5'] * 7
    pull_percentage = og_pull_percentage.copy()

    for _ in range(1, limit + 1):
        # Pity System
        # 80 - Is 5 Star pity (n-1) = 79
        if pp.five_star_weapon_pity >= 79:
            # Returning to the original weight percentages
            pull_percentage = og_pull_percentage.copy()
            get_banner_pity(5)
        # 9 - is 4 star pity (n-1) = 8
        elif pp.four_star_weapon_pity >= 8:
            get_banner_pity(4)
        else:
            # Pulls
            if pp.five_star_weapon_pity > 64:
                # Adding more prob to get a 5 star
                pull_percentage.extend(['5'] * 320)
            magic = random.choice(pull_percentage)
            # 3 Star
            if magic == '3':
                a = random.choice(lst.star3_weapons)
                add_gacha_weapon(3, item=a) # -------------------------------- #
                inv.add_3star_weapon_inv(a)
                add_pity(four=True, five=True)
            # 4 Star
            elif magic == '4':
                # If Promo Weapon was won = 75% Chance of winning another one
                if not pp.flag_4star_weapon:
                    # 75% chance of getting either a promotional character, or a standard character/weapon
                    if random.randint(1, 4) != 1:
                        # Random Promotional 4* Weapon Won
                        b = random.choice(lstbn.current_weapon_banner_4)
                        # Adding to Inventory
                        inv.add_4star_weapon_inv(b)
                    else:
                        pp.flag_4star_weapon = True
                        # 50-50 chance of getting either a character or a weapon (standard)
                        if random.randint(1, 2) == 1:
                            # Character won
                            b = random.choice(lst.all_4star_standard_except_akl)
                            # Adding to Inventory
                            inv.add_4star_char_inv(b)
                        else:
                            # Weapon won
                            b = random.choice(lst.star4_standar_weapons)
                            # Adding to Inventory
                            inv.add_4star_weapon_inv(b)
                    add_gacha_weapon(4, b)
                    add_pity(four=True, five=True)
                    pp.four_star_weapon_pity = 0
                else:
                    # Guaranteed 4 Star Promotional Weapon
                    b = random.choice(lstbn.current_weapon_banner_4)
                    # Adding to Inventory
                    inv.add_4star_weapon_inv(b)
                    pp.flag_4star_weapon = False
                    add_gacha_weapon(4, b)
                    add_pity(four=True, five=True)
                    pp.four_star_weapon_pity = 0
            # 5 Star
            else:
                # If Promo Weapon was won = 75% Chance of winning another one
                if not pp.flag_5star_weapon:
                    # 75% chance of getting a promotional weapon. 25% chance of getting a standard weapon
                    if random.randint(1, 4) == 1:
                        # Non promotional weapon won
                        a = random.choice(lst.star5_standar_weapons)
                    else:
                        # 50-50% chance of getting either promotional weapon A or B
                        a = random.choice(lstbn.current_weapon_banner_5)
                        pp.flag_5star_weapon = True
                    # Adding to Inventory
                    inv.add_5star_weapon_inv(a)
                    add_gacha_weapon(5, item=a)
                    add_pity(four=True, five=True)
                else:
                    # Guaranteed one of the two 5* Promotional Weapons
                    a = random.choice(lstbn.current_weapon_banner_5)
                    # Adding to Inventory
                    inv.add_5star_weapon_inv(a)
                    pp.flag_5star_weapon = False
                    add_gacha_weapon(5, item=a)
                    add_pity(four=True, five=True)
                # Returning to the original weight percentages
                pull_percentage = og_pull_percentage.copy()
                pp.five_star_weapon_pity = 0

    # Init Star Animation
    # Checking if there is a 5*,4* or 3* in the pulls. If there are, the animation changes.
    check4 = any(item in gacha for item in lst.all_4star)
    check5 = any(item in gacha for item in lst.all_5star)
    if check5:
        # 5 Star animation
        wishes.animation(5, f'{wishes.banner_}')
    elif check4:
        # 4 Star animation
        wishes.animation(4, f'{wishes.banner_}')
    else:
        # 3 Star animation
        wishes.animation(3, f'{wishes.banner_}')


def get_banner_pity(rarity):
    if rarity == 5:
        if not pp.flag_5star_weapon:
            # 75% chance of getting a promotional weapon. 25% chance of getting a standard weapon
            if random.randint(1, 4) == 1:
                # Non promotional weapon won
                a = random.choice(lst.star5_standar_weapons)
                # Adding to Inventory
                inv.add_5star_weapon_inv(a)
            else:
                # 50-50% chance of getting either promotional weapon A or B
                a = random.choice(lstbn.current_weapon_banner_5)
                # Adding to Inventory
                inv.add_5star_weapon_inv(a)
                pp.flag_5star_weapon = True
            add_gacha_weapon(5, item=a)
            add_pity(four=True, five=True)
        else:
            # Guaranteed one of the two 5* Promotional Weapons
            a = random.choice(lstbn.current_weapon_banner_5)
            # Adding to Inventory
            inv.add_5star_weapon_inv(a)
            pp.flag_5star_weapon = False
            add_gacha_weapon(5, item=a)
            add_pity(four=True, five=True)
        pp.five_star_weapon_pity = 0

    elif rarity == 4:
        # If Promo Character was won = 50-50% Chance of winning another one
        if not pp.flag_4star_weapon:
            # 75% chance of getting either a promotional character, or a standard character/weapon
            if random.randint(1, 4) != 1:
                # Random Promotional 4* Weapon Won
                b = random.choice(lstbn.current_weapon_banner_4)
                # Adding to Inventory
                inv.add_4star_weapon_inv(b)
            else:
                pp.flag_4star_weapon = True
                # 50-50 chance of getting either a character or a weapon (standard)
                if random.randint(1, 2) == 1:
                    # Character won
                    b = random.choice(lst.all_4star_standard_except_akl)
                    # Adding to Inventory
                    inv.add_4star_char_inv(b)
                else:
                    # Weapon won
                    b = random.choice(lst.star4_standar_weapons)
                    # Adding to Inventory
                    inv.add_4star_weapon_inv(b)
            add_gacha_weapon(4, b)
            add_pity(four=True, five=True)
            pp.four_star_weapon_pity = 0
        else:
            # Guaranteed 4 Star Promotional Weapon
            b = random.choice(lstbn.current_weapon_banner_4)
            # Adding to Inventory
            inv.add_4star_weapon_inv(b)
            pp.flag_4star_weapon = False
            add_gacha_weapon(4, b)
            add_pity(four=True, five=True)
            pp.four_star_weapon_pity = 0


# Function to keep track of pity
def add_pity(four=False, five=False):
    pp.pull_count(banner_name)
    if five and four:
        pp.five_star_weapon_pity += 1
        pp.four_star_weapon_pity += 1
    elif not five:
        pp.four_star_weapon_pity += 1
    elif not four:
        pp.five_star_weapon_pity += 1
    else:
        raise Exception('Error while adding pity to weapon pity. There needs to be a True statement')


# Add to the list for
def add_gacha_weapon(rarity, item):
    global gacha
    global gacha_show

    if rarity == 3:
        gacha.append(item)
        gacha_show.append(item)
    elif rarity == 4:
        gacha.append(item)
        gacha_show.append(wishes.Color.PURPLE + f'{item}   ⭐⭐⭐⭐' + wishes.Color.END)
    elif rarity == 5:
        gacha.append(item)
        gacha_show.append(wishes.Color.YELLOW + f'{item}   🌟🌟🌟🌟🌟' + wishes.Color.END)
    else:
        raise Exception('Invalid rarity type. Rarity can be 3,4 or 5.')

# -----------------------------------------------------------------------------------------------------
