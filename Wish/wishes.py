from time import sleep
from sys import exit
from Inventory import inventory as inv, list_com_banners as bn
from Banners import promo_pity as pp
from Banners import standard_banner, tartaglia_rerun_banner, everything_banner, zhongli_rerun_banner, eula_banner
from Banners import klee_rerun_banner, kazuha_banner, ayaka_banner, yoimiya_banner, raiden_banner, kokomi_banner
from Banners import tartaglia_rerun2_banner, hutao_rerun_banner, eula_rerun_banner, albedo_rerun_banner, itto_banner
from Weapon_Banner import current_weapon_banner

# Current Banner - Default
banner_ = 'standard'
banner_name = 'Standard'
wish_animation = True


def init():
    """
    Banners:
    Standard Banner = standard (By Default)
    Childe Rerun Banner = childe_re
    Zhongli Rerun Banner = zhongli_re
    Eula Banner = eula
    Klee Rerun Banner = klee_re
    Kamisato Ayaka Banner = ayaka
    Yoimiya Banner = yoimiya
    Raiden Shogun Banner = raiden
    Sangonomiya Kokomi Banner = kokomi
    Childe Second Rerun Banner = childe_re2
    Hu Tao Rerun Banner = hutao_re
    Eula Rerun Banner = eula_re
    Albedo Rerun Banner = albedo_re
    Arataki 'Numero Uno' Itto Banner = itto
    Everything Banner = everything
    Current Weapon Banner = weapon
    """
    global banner_
    global banner_name
    global wish_animation

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
                banner_name, banner_ = 'Standard', 'standard'
                print(Color.RED + f'Changed to {banner_name} Banner' + Color.END)
                print('`~`' * 9, '\n')
                continue
            elif x == 'weapon':
                banner_name, banner_ = 'Weapon', 'weapon'
                print(Color.RED + f'Changed to {banner_name} Banner' + Color.END)
                print('`~`' * 9, '\n')
                continue
            elif x == 'everything':
                banner_name, banner_ = 'Everything Banner', 'everything'
                print(Color.RED + f'Changed to {banner_name} Banner' + Color.END)
                print('`~`' * 9, '\n')
                continue
            elif x == 'childe_re':
                banner_name, banner_ = 'Childe Rerun', 'childe_re'
                print(Color.RED + f'Changed to {banner_name} Banner' + Color.END)
                print('`~`' * 9, '\n')
                continue
            elif x == 'zhongli_re':
                banner_name, banner_ = 'Zhongli Rerun', 'zhongli_re'
                print(Color.RED + f'Changed to {banner_name} Banner' + Color.END)
                print('`~`' * 9, '\n')
                continue
            elif x == 'eula':
                banner_name, banner_ = 'Eula', 'eula'
                print(Color.RED + f'Changed to {banner_name} Banner' + Color.END)
                print('`~`' * 9, '\n')
                continue
            elif x == 'klee_re':
                banner_name, banner_ = 'Klee Rerun', 'klee_re'
                print(Color.RED + f'Changed to {banner_name} Banner' + Color.END)
                print('`~`' * 9, '\n')
                continue
            elif x == 'kazuha':
                banner_name, banner_ = 'Kazuha', 'kazuha'
                print(Color.RED + f'Changed to {banner_name} Banner' + Color.END)
                print('`~`' * 9, '\n')
                continue
            elif x == 'ayaka':
                banner_name, banner_ = 'Kamisato Ayaka', 'ayaka'
                print(Color.RED + f'Changed to {banner_name} Banner' + Color.END)
                print('`~`' * 9, '\n')
                continue
            elif x == 'yoimiya':
                banner_name, banner_ = 'Yoimiya', 'yoimiya'
                print(Color.RED + f'Changed to {banner_name} Banner' + Color.END)
                print('`~`' * 9, '\n')
                continue
            elif x == 'raiden':
                banner_name, banner_ = 'Raiden Shogun', 'raiden'
                print(Color.RED + f'Changed to {banner_name} Banner' + Color.END)
                print('`~`' * 9, '\n')
                continue
            elif x == 'kokomi':
                banner_name, banner_ = 'Sangonimiya Kokomi', 'kokomi'
                print(Color.RED + f'Changed to {banner_name} Banner' + Color.END)
                print('`~`' * 9, '\n')
                continue
            elif x == 'childe_re2':
                banner_name, banner_ = 'Childe Rerun 2', 'childe_re2'
                print(Color.RED + f'Changed to {banner_name} Banner' + Color.END)
                print('`~`' * 9, '\n')
                continue
            elif x == 'hutao_re':
                banner_name, banner_ = 'Hu Tao Rerun', 'hutao_re'
                print(Color.RED + f'Changed to {banner_name} Banner' + Color.END)
                print('`~`' * 9, '\n')
                continue
            elif x == 'eula_re':
                banner_name, banner_ = 'Eula Rerun', 'eula_re'
                print(Color.RED + f'Changed to {banner_name} Banner' + Color.END)
                print('`~`' * 9, '\n')
                continue
            elif x == 'albedo_re':
                banner_name, banner_ = 'Albedo Rerun', 'albedo_re'
                print(Color.RED + f'Changed to {banner_name} Banner' + Color.END)
                print('`~`' * 9, '\n')
                continue
            elif x == 'itto':
                banner_name, banner_ = 'Arataki Itto', 'itto'
                print(Color.RED + f'Changed to {banner_name} Banner' + Color.END)
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
                print(Color.YELLOW + f'5 Star pity count ({banner_name} Banner): ' + Color.END + f'{get_pity_5(banner_)}')
                print(Color.PURPLE + f'4 Star pity count ({banner_name} Banner): ' + Color.END + f'{get_pity_4(banner_)}')
                print('---')
                print(f'Total pulls in {banner_name} Banner: {pp.get_pull_count(banner_)}')
                print('`~`' * 13, '\n')
            # Star Animation ON or OFF
            elif x in ['on', 'animation on', 'animationon']:
                wish_animation = True
                print(Color.RED + 'Star Animation turned ON' + Color.END)
                print('`~`' * 9, '\n')
            elif x in ['off', 'animation off', 'animationoff']:
                wish_animation = False
                print(Color.RED + 'Star Animation turned OFF' + Color.END)
                print('`~`' * 9, '\n')
            # Quit
            elif x in ['q', 'quit', 'bye', 'exit']:
                bye()
            else:
                print('Type help for instructions or try again.')
                continue


def wish(banner, pull):
    if banner == 'standard':
        standard_banner.standard_banner(pull)
    elif banner == 'weapon':
        current_weapon_banner.weapon_banner(pull)
    elif banner == 'everything':
        everything_banner.everything_banner(pull)
    elif banner == 'childe_re':
        tartaglia_rerun_banner.childe_rerun_banner(pull)
    elif banner == 'zhongli_re':
        zhongli_rerun_banner.zhongli_rerun_banner(pull)
    elif banner == 'eula':
        eula_banner.eula_banner(pull)
    elif banner == 'klee_re':
        klee_rerun_banner.klee_rerun_banner(pull)
    elif banner == 'kazuha':
        kazuha_banner.kazuha_banner(pull)
    elif banner == 'ayaka':
        ayaka_banner.ayaka_banner(pull)
    elif banner == 'yoimiya':
        yoimiya_banner.yoimiya_banner(pull)
    elif banner == 'raiden':
        raiden_banner.raiden_banner(pull)
    elif banner == 'kokomi':
        kokomi_banner.kokomi_banner(pull)
    elif banner == 'childe_re2':
        tartaglia_rerun2_banner.banner(pull)
    elif banner == 'hutao_re':
        hutao_rerun_banner.banner(pull)
    elif banner == 'eula_re':
        eula_rerun_banner.banner(pull)
    elif banner == 'albedo_re':
        albedo_rerun_banner.banner(pull)
    elif banner == 'itto':
        itto_banner.banner(pull)
    else:
        raise Exception('No specified banner or pull in wishes.init')


def get_pity_5(banner):
    if banner == 'standard':
        return pp.five_star_pity_standard
    elif banner == 'weapon':
        return pp.five_star_weapon_pity
    elif banner == 'everything':
        return pp.five_star_pity_everything
    elif banner in ['childe_re','zhongli_re','eula','klee_re','kazuha','ayaka','yoimiya','raiden','kokomi','childe_re2',
                    'hutao_re','eula_re','albedo_re','itto']:
        return pp.five_star_promo_pity
    else:
        raise Exception('Not specified what banner is the pity. Wishes/def_pity_5')


def get_pity_4(banner):
    if banner == 'standard':
        return pp.four_star_pity_standard
    elif banner == 'weapon':
        return pp.four_star_weapon_pity
    elif banner == 'everything':
        return pp.four_star_pity_everything
    elif banner in ['childe_re','zhongli_re','eula','klee_re','kazuha','ayaka','yoimiya','raiden','kokomi','childe_re2',
                    'hutao_re','eula_re','albedo_re','itto']:
        return pp.four_star_promo_pity
    else:
        raise Exception('Not specified what banner is the pity. Wishes/def_pity_4')


def help_me():
    # Color Commands
    n_1 = Color.DARKCYAN + '1' + Color.END
    n_10 = Color.DARKCYAN + '10' + Color.END
    n_inv = Color.DARKCYAN + 'inv' + Color.END
    n_pity = Color.DARKCYAN + 'pity' + Color.END
    n_ON_OFF = Color.DARKCYAN + 'on' + Color.END + ' or ' + Color.DARKCYAN + 'off' + Color.END
    n_help = Color.DARKCYAN + 'help' + Color.END
    n_more = Color.GREEN + 'more' + Color.END
    n_q = Color.RED + 'q' + Color.END
    n_wn = Color.UNDERLINE + 'will not' + Color.END
    print('\n', '`~`' * 9, f'\nType {n_1} for a single pull. | Type {n_10} for a ten pull.\nType {n_inv} to see your '
                           f'inventory.\nType {n_pity} to see the current pity + total amount of'
                           f' pulls made in your current banner.\nType {n_ON_OFF} to turn On or Off the Star Animation.'
                           f'\nType {n_help} '
                           f'to see this message again.\nType {n_more} to read banner instructions and more.'
                           f'\nType {n_q} to quit. Note: Your inventory {n_wn} be saved.\n', '`~`' * 17)
    init()


def more():
    # Getting Characters
    childe_re_4 = ', '.join([str(elem) for elem in bn.childe_banner_4])
    zhongli_re_4 = ', '.join([str(elem) for elem in bn.zhongli_re_banner_4])
    eula_4 = ', '.join([str(elem) for elem in bn.eula_banner_4])
    klee_re_4 = ', '.join([str(elem) for elem in bn.klee_rerun_banner_4])
    kazuha_4 = ', '.join([str(elem) for elem in bn.kazuha_banner_4])
    ayaka_4 = ', '.join([str(elem) for elem in bn.ayaka_banner_4])
    yoimiya_4 = ', '.join([str(elem) for elem in bn.yoimiya_banner_4])
    raiden_4 = ', '.join([str(elem) for elem in bn.raiden_banner_4])
    kokomi_4 = ', '.join([str(elem) for elem in bn.kokomi_banner_4])
    childe_re2_4 = ', '.join([str(elem) for elem in bn.childe_re2_banner_4])
    hutao_re_4 = ', '.join([str(elem) for elem in bn.hutao_rerun_banner_4])
    eula_re_4 = ', '.join([str(elem) for elem in bn.eula_rerun_banner_4])
    albedo_re_4 = ', '.join([str(elem) for elem in bn.albedo_rerun_banner_4])
    itto_4 = ', '.join([str(elem) for elem in bn.itto_banner_4])
    # Weapons
    current_weapon_5 = ', '.join([str(elem) for elem in bn.current_weapon_banner_5])
    current_weapon_4 = ', '.join([str(elem) for elem in bn.current_weapon_banner_4])
    # weapon_yoimiya_4 = ', '.join([str(elem) for elem in bn.yoi_weapon_banner_4])
    # weapon_yoimiya_5 = ', '.join([str(elem) for elem in bn.yoi_weapon_banner_5])
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    print('\n', '`~`' * 9)
    print('How to change banners:\nType the name of the banner you want to pull in. Banners available are:\n'
          '(Default) Standard Banner' + Color.CYAN + ' = standard' + Color.END,
          '\nCurrent Weapon Banner ' + Color.YELLOW + f'({current_weapon_5})' + Color.PURPLE + f'({current_weapon_4})' + Color.CYAN + ' = weapon' + Color.END,
          '\nTartaglia Rerun Banner ' + Color.PURPLE + f'({childe_re_4})' + Color.CYAN + ' = childe_re' + Color.END,
          '\nZhongli Rerun Banner ' + Color.PURPLE + f'({zhongli_re_4})' + Color.CYAN + ' = zhongli_re' + Color.END,
          '\nEula Banner ' + Color.PURPLE + f'({eula_4})' + Color.CYAN + ' = eula' + Color.END,
          '\nKlee Rerun Banner ' + Color.PURPLE + f'({klee_re_4})' + Color.CYAN + ' = klee_re' + Color.END,
          '\nKazuha Banner ' + Color.PURPLE + f'({kazuha_4})' + Color.CYAN + ' = kazuha' + Color.END,
          '\nAyaka Banner ' + Color.PURPLE + f'({ayaka_4})' + Color.CYAN + ' = ayaka' + Color.END,
          '\nYoimiya Banner ' + Color.PURPLE + f'({yoimiya_4})' + Color.CYAN + ' = yoimiya' + Color.END,
          '\nRaiden Shogun Banner ' + Color.PURPLE + f'({raiden_4})' + Color.CYAN + ' = raiden' + Color.END,
          '\nSangonomiya Kokomi Banner ' + Color.PURPLE + f'({kokomi_4})' + Color.CYAN + ' = kokomi' + Color.END,
          '\nTartaglia Rerun 2 Banner ' + Color.PURPLE + f'({childe_re2_4})' + Color.CYAN + ' = childe_re2' + Color.END,
          '\nHu Tao Rerun Banner ' + Color.PURPLE + f'({hutao_re_4})' + Color.CYAN + ' = hutao_re' + Color.END,
          '\nEula Rerun Banner ' + Color.PURPLE + f'({eula_re_4})' + Color.CYAN + ' = eula_re' + Color.END,
          '\nAlbedo Rerun Banner ' + Color.PURPLE + f'({albedo_re_4})' + Color.CYAN + ' = albedo_re' + Color.END,
          '\nArataki Itto Banner ' + Color.PURPLE + f'({itto_4})' + Color.CYAN + ' = itto' + Color.END,
          '\nEverything Banner (Contains every 5*,4* Character/Weapon in the game)' + Color.CYAN + ' = everything'
          + Color.END, '\n\nNotes:\n\t● Standard and Everything Banner have their own pity. Promotional Banners share '
                       'pity.\n\t● Standard Banner have the same functions '
                       'as the original.\n\t● Promotional Banners have the same functions as the '
                       'original, including 50% chance of getting the promotional character,\n\t\tif the '
                       'first time a 5* appeared was not the promotional one, next 5* will be guaranteed the '
                       '5* promotional character; 50% chance of getting\n\t\tone of the promotional 4* Characters, '
                       'if you got a non promotional 4* Character, next 4* will be guaranteed one of the promotional '
                       '4* characters.\n\t● Weapon Banner includes the CURRENT weapon banner, including the 4* and 5*.'
                       '\n\t● Everything banner contains EVERY 5*/4* Character and Weapon in the game, '
                       'including gacha, shop, forgeable, battlepass, event exclusives\n\t\t and promotional '
                       'weapons. You get a guaranteed character if you got a weapon before. Chances are '
                       '50-50% of getting either a character or a weapon.\n\t● Probabilities: 0.6% of getting a '
                       '5 Star ~ 5.1% of getting a 4 Star, ~ 94.3% of getting a 3 Star.\n\t\t 5* Soft Pity starts '
                       'after the 74th Pull. Hard Pity is in the 90th Pull.\n\t\t 4* is guaranteed in each 10 pull.'
                       '\n\t● Weapon Banner Probabilities: 0.7% of getting a 5 Star ~ 5.1% of getting a 4 Star, '
                       '~ 93.3% of getting a 3 Star.\n\t\t 5* Soft Pity starts after the 64th Pull. Hard Pity is '
                       'in the 80th pull. 4* is guaranteed in each 9 pull.')
    print('\n', '`~`' * 9)
    init()


def bye():
    print(Color.RED + 'May your wishes come true. Goodbye.' + Color.END)
    exit()


# Animation changes for a 5,4 or 3 star.
def animation(rarity, banner):
    if wish_animation:
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
    elif banner == 'weapon':
        current_weapon_banner.show_pulls()
    elif banner == 'everything':
        everything_banner.show_pulls()
    elif banner == 'childe_re':
        tartaglia_rerun_banner.show_pulls()
    elif banner == 'zhongli_re':
        zhongli_rerun_banner.show_pulls()
    elif banner == 'eula':
        eula_banner.show_pulls()
    elif banner == 'klee_re':
        klee_rerun_banner.show_pulls()
    elif banner == 'kazuha':
        kazuha_banner.show_pulls()
    elif banner == 'ayaka':
        ayaka_banner.show_pulls()
    elif banner == 'yoimiya':
        yoimiya_banner.show_pulls()
    elif banner == 'raiden':
        raiden_banner.show_pulls()
    elif banner == 'kokomi':
        kokomi_banner.show_pulls()
    elif banner == 'childe_re2':
        tartaglia_rerun2_banner.show_pulls()
    elif banner == 'hutao_re':
        hutao_rerun_banner.show_pulls()
    elif banner == 'eula_re':
        eula_rerun_banner.show_pulls()
    elif banner == 'albedo_re':
        albedo_rerun_banner.show_pulls()
    elif banner == 'itto':
        itto_banner.show_pulls()
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
