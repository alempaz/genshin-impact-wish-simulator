# Standard Pity Count
five_star_pity_everything = 0
four_star_pity_everything = 0

# Everything Pity Count
five_star_pity_standard = 0
four_star_pity_standard = 0

# Pity Count
five_star_promo_pity = 0
four_star_promo_pity = 0

# Weapon Pity Count
five_star_weapon_pity = 0
four_star_weapon_pity = 0

# Flags if promo character was not won
flag_5star = False
flag_4star = False

# Flags if promo weapon was not won
flag_5star_weapon = False
flag_4star_weapon = False

# Amount of pulls
standard_pulls = 0
everything_pulls = 0
weapon_pulls = 0
childe_rerun_pulls = 0
zhongli_rerun_pulls = 0
eula_pulls = 0
klee_rerun_pulls = 0
kazuha_pulls = 0
ayaka_pulls = 0
yoimiya_pulls = 0
raiden_pulls = 0
kokomi_pulls = 0
childe_rerun2_pulls = 0
hutao_rerun_pulls = 0
eula_rerun_pulls = 0
albedo_rerun_pulls = 0
itto_pulls = 0


def pull_count(banner):
    global standard_pulls
    global everything_pulls
    global weapon_pulls
    global childe_rerun_pulls
    global zhongli_rerun_pulls
    global eula_pulls
    global klee_rerun_pulls
    global kazuha_pulls
    global ayaka_pulls
    global yoimiya_pulls
    global raiden_pulls
    global kokomi_pulls
    global childe_rerun2_pulls
    global hutao_rerun_pulls
    global eula_rerun_pulls
    global albedo_rerun_pulls
    global itto_pulls


    if banner == 'standard':
        standard_pulls += 1
    elif banner == 'everything':
        everything_pulls += 1
    elif banner == 'weapon':
        weapon_pulls += 1
    elif banner == 'childe_re':
        childe_rerun_pulls += 1
    elif banner == 'zhongli_re':
        zhongli_rerun_pulls += 1
    elif banner == 'eula':
        eula_pulls += 1
    elif banner == 'klee_re':
        klee_rerun_pulls += 1
    elif banner == 'kazuha':
        kazuha_pulls += 1
    elif banner == 'ayaka':
        ayaka_pulls += 1
    elif banner == 'yoimiya':
        yoimiya_pulls += 1
    elif banner == 'raiden':
        raiden_pulls += 1
    elif banner == 'kokomi':
        kokomi_pulls += 1
    elif banner == 'childe_re2':
        childe_rerun2_pulls += 1
    elif banner == 'hutao_re':
        hutao_rerun_pulls += 1
    elif banner == 'eula_re':
        eula_rerun_pulls += 1
    elif banner == 'albedo_re':
        albedo_rerun_pulls += 1
    elif banner == 'itto':
        itto_pulls += 1
    else:
        raise Exception('Could not add pull count. Banner not specified.')


def get_pull_count(banner):
    if banner == 'standard':
        return standard_pulls
    elif banner == 'everything':
        return everything_pulls
    elif banner == 'weapon':
        return weapon_pulls
    elif banner == 'weapon':
        return childe_rerun_pulls
    elif banner == 'zhongli_re':
        return zhongli_rerun_pulls
    elif banner == 'eula':
        return eula_pulls
    elif banner == 'klee_re':
        return klee_rerun_pulls
    elif banner == 'kazuha':
        return kazuha_pulls
    elif banner == 'ayaka':
        return ayaka_pulls
    elif banner == 'yoimiya':
        return yoimiya_pulls
    elif banner == 'raiden':
        return raiden_pulls
    elif banner == 'kokomi':
        return kokomi_pulls
    elif banner == 'childe_re2':
        return childe_rerun2_pulls
    elif banner == 'hutao_re':
        return hutao_rerun_pulls
    elif banner == 'eula_re':
        return eula_rerun_pulls
    elif banner == 'albedo_re':
        return albedo_rerun_pulls
    elif banner == 'itto':
        return itto_pulls
    else:
        raise Exception('Could not return pull count. Banner not specified./promo_pity(get_pull_count))')
