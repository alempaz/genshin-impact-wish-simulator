from time import sleep
from sys import exit
from Inventory import inventory as inv, list_com_banners as bn
from Banners import promo_pity as pp
from Banners import standard_banner, tartaglia_banner, everything_banner, zhongli_rerun_banner

# Current Banner
banner_ = 'standard'


def init():
    """
    Banners:
    Standard Banner = standard (By Default)
    Childe Banner = childe
    Everything Banner = everything
    """
    global banner_

    while True:
        user_input = input('\n  > ')
        try:
            pull = int(user_input)
            if pull == 1 or pull == 10:
                wish(banner_, pull)
                break
            else:
                print('Type help for instructions or try again.')
                continue
        except ValueError:
            x = user_input.lower()
            # Change Banners
            if x == banner_:
                print(f'Banner is already {banner_}.')
                continue
            elif x == 'standard':
                banner_ = 'standard'
                print(Color.RED + f'Changed to {banner_} Banner' + Color.END)
                print('`~`' * 9, '\n')
                continue
            elif x == 'childe':
                banner_ = 'childe'
                print(Color.RED + f'Changed to {banner_} Banner' + Color.END)
                print('`~`' * 9, '\n')
                continue
            elif x == 'everything':
                banner_ = 'everything'
                print(Color.RED + f'Changed to {banner_} Banner' + Color.END)
                print('`~`' * 9, '\n')
                continue
            elif x == 'zhongli':
                banner_ = 'zhongli'
                print(Color.RED + f'Changed to {banner_} Banner' + Color.END)
                print('`~`' * 9, '\n')
                continue
            # Helps
            elif x == 'help':
                help_me()
            elif x == 'more':
                more()
            # Show Inventory
            elif x in ['inv', 'inventory', 'i']:
                inv.show_inventory()
            # Get Pity
            elif x == 'pity':
                print('\n', '`~`' * 13)
                print(Color.YELLOW + f'5 Star pity count ({banner_} Banner): ' + Color.END + f'{get_pity_5(banner_)}')
                print(Color.PURPLE + f'4 Star pity count ({banner_} Banner): ' + Color.END + f'{get_pity_4(banner_)}')
                print('`~`' * 13, '\n')
            # Quit
            elif x in ['q', 'quit', 'bye']:
                bye()
            else:
                print('Type help for instructions or try again.')
                continue


def wish(banner, pull):
    if banner == 'standard':
        standard_banner.standard_banner(pull)
    elif banner == 'childe':
        tartaglia_banner.childe_banner(pull)
    elif banner == 'everything':
        everything_banner.everything_banner(pull)
    elif banner == 'zhongli':
        zhongli_rerun_banner.zhongli_rerun_banner(pull)
    else:
        raise Exception('No specified banner or pull in init')


def get_pity_5(banner):
    if banner == 'standard':
        return standard_banner.five_star_pity_standard
    elif banner == 'everything':
        return everything_banner.five_star_pity_everything
    elif banner in ['childe', 'zhongli']:
        return pp.five_star_promo_pity
    else:
        raise Exception('Not specified what banner is the pity')


def get_pity_4(banner):
    if banner == 'standard':
        return standard_banner.four_star_pity_standard
    elif banner == 'everything':
        return everything_banner.four_star_pity_everything
    elif banner in ['childe', 'zhongli']:
        return pp.four_star_promo_pity
    else:
        raise Exception('Not specified what banner is the pity')


def help_me():
    # Color Commands
    n_1 = Color.DARKCYAN + '1' + Color.END
    n_10 = Color.DARKCYAN + '10' + Color.END
    n_inv = Color.DARKCYAN + 'inv' + Color.END
    n_pity = Color.DARKCYAN + 'pity' + Color.END
    n_help = Color.DARKCYAN + 'help' + Color.END
    n_more = Color.GREEN + 'more' + Color.END
    n_q = Color.RED + 'q' + Color.END
    n_wn = Color.UNDERLINE + 'will not' + Color.END
    print('\n', '`~`' * 9, f'\nType {n_1} for a single pull. | Type {n_10} for a ten pull.\nType {n_inv} to see your '
                           f'inventory.\nType {n_pity} to see the current pity of your current banner.\nType {n_help} '
                           f'to see this message again.\nType {n_more} to read banner instructions and more.'
                           f'\nType {n_q} to quit. Note: Your inventory {n_wn} be saved.\n', '`~`' * 17)
    init()


def more():
    # Getting Characters
    childe_4 = ', '.join([str(elem) for elem in bn.childe_banner_4])
    zhongli_4 = ', '.join([str(elem) for elem in bn.zhongli_re_banner_4])
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    print('\n', '`~`' * 9)
    print('How to change banners:\nType the name of the banner you want to pull in. Banners available are:\n'
          'Standard Banner' + Color.CYAN + ' = standard' + Color.END,
          '\nTartaglia Banner ' + Color.PURPLE + f'({childe_4})' + Color.CYAN + ' = childe' + Color.END,
          '\nZhongli Rerun Banner ' + Color.PURPLE + f'({zhongli_4})' + Color.CYAN + ' = zhongli' + Color.END,
          '\nEverything Banner (Contains every 5*,4* Character/Weapon in the game)' + Color.CYAN + ' = everything'
          + Color.END, '\n\nNotes:\n\t● Standard and Everything Banner have their own pity. Promotional Banners share '
                       'pity.\n\t● Standard Banner have the same functions '
                       'as the original.\n\t● Promotional Banners have the same functions as the '
                       'original, including 50% chance of getting the promotional character,\n\t\tif the '
                       'first time a 5* appeared was not the promotional one, next 5* will be guaranteed the '
                       '5* promotional character; 50% chance of getting\n\t\tone of the promotional 4* Characters, '
                       'if you got a non promotional 4* Character, next 4* will be guaranteed one of the promotional '
                       '4* characters.\n\t● Everything banner contains EVERY 5*/4* Character and Weapon in the game, '
                       'including gacha, shop, forgeable, battlepass, event exclusives\n\t\t and promotional '
                       'weapons. You get a guaranteed character if you got a weapon before. Chances are '
                       '50-50% of getting either a character or a weapon.\n\t● Probabilities: 0.6% of getting a '
                       '5 Star ~ 5.1% of getting a 4 Star, ~ 94.3% of getting a 3 Star.\n\t\t 5* Soft Pity starts '
                       'after the 75th Pull. Hard Pity is in the 90th Pull.\n\t\t 4* is guaranteed in each 10 pull.')
    print('\n', '`~`' * 9)
    init()


def bye():
    print(Color.RED + 'May your wishes come true. Goodbye.' + Color.END)
    exit()


# Animation changes for a 5,4 or 3 star.
def animation(rarity, banner):
    if rarity == 5:
        print('~' * 26)
        sleep(0.30)
        print("`")
        sleep(0.30)
        print('  `')
        sleep(0.30)
        print('    `')
        sleep(0.30)
        print('      `')
        sleep(0.20)
        print(Color.YELLOW + '              `   *  ')
        sleep(0.25)
        print('           **  (  #  ) **       ')
        sleep(0.25)
        print('         *** (    #    ) ***      ')
        sleep(0.25)
        print('    ****  (      ###    )  ****     ')
        sleep(0.25)
        print('   *****(     🌠🌠🌠🌠🌠    )*****  ')
        sleep(0.25)
        print('    ****  (      ###    )  ****     ')
        sleep(0.25)
        print('         *** (    #    ) ***      ')
        sleep(0.25)
        print('           **  (  #  ) **       ')
        sleep(0.25)
        print('                  *           ' + Color.END)
        sleep(0.4)
        print('')
    elif rarity == 4:
        print('~' * 26)
        sleep(0.30)
        print("`")
        sleep(0.30)
        print('  `')
        sleep(0.30)
        print('    `')
        sleep(0.30)
        print('      `')
        sleep(0.30)
        print('         `')
        sleep(0.20)
        print(Color.PURPLE + '           `   *  ')
        sleep(0.25)
        print('         ** (  #  ) **       ')
        sleep(0.25)
        print('      *** (    #    ) ***      ')
        sleep(0.25)
        print('    ****(   🌠🌠🌠🌠   )****   ')
        sleep(0.25)
        print('      *** (    #    ) ***      ')
        sleep(0.25)
        print('         ** (  #  ) **       ')
        sleep(0.25)
        print('               *           ' + Color.END)
        sleep(0.4)
        print('')
    else:
        print('~' * 26)
        sleep(0.30)
        print("`")
        sleep(0.30)
        print('  `')
        sleep(0.30)
        print('    `')
        sleep(0.30)
        print('      `')
        sleep(0.30)
        print('         `')
        sleep(0.20)
        print(Color.CYAN + '           `   *  ')
        sleep(0.25)
        print('         ** (  #  ) **       ')
        sleep(0.25)
        print('      *** (    #    ) ***      ')
        sleep(0.25)
        print('         ** (  #  ) **       ')
        sleep(0.25)
        print('               *           ' + Color.END)
        sleep(0.4)
        print('')

    if banner == 'standard':
        standard_banner.show_pulls()
    elif banner == 'childe':
        tartaglia_banner.show_pulls()
    elif banner == 'everything':
        everything_banner.show_pulls()
    elif banner == 'zhongli':
        zhongli_rerun_banner.show_pulls()
    else:
        raise Exception('No banner.show_pulls specified')


class Color:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'
