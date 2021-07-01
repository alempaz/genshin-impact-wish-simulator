from Characters import character_list as c
from Weapons import weapon_list as w
# ------------------------------------------------------ LISTS -------------------------------------------------------
# All Characters in-game
char_list_obj = [c.diluc, c.jean, c.keqing, c.mona, c.qiqi, c.albedo, c.ganyu, c.hu_tao, c.klee, c.tartaglia, c.venti,
                 c.xiao, c.zhongli, c.ayaka, c.eula, c.amber, c.barbara, c.beidou, c.bennet, c.chongyun, c.diona,
                 c.fischl, c.kaeya, c.lisa, c.ningguang, c.noelle, c.razor, c.rosaria, c.sucrose, c.xianglin,
                 c.xingqiu, c.xinyan, c.yanfei, c.kazuha, c.ayaka, c.yoimiya, c.sayu]

# All Weapons in-game
weapon_list_obj = [w.aquila_favonia,w.primordial_jade_cutter,w.summit_shaper,w.skyward_blade,w.blackcliff_longsword,
                   w.royal_longsword,w.the_black_sword,w.iron_sting,w.prototype_rancour,w.favonius_sword,
                   w.lions_roar,w.sacrificial_sword,w.the_flute,w.the_alley_flash,w.festering_desire,w.cool_steel,
                   w.sword_of_descension,w.harbinger_of_dawn,w.skyrider_sword,w.freedom_sworn,

                   w.song_of_broken_pines,w.skyward_pride,w.the_unforged,w.wolfs_gravestone,w.blackcliff_slasher,
                   w.royal_greatsword,w.serpent_spine,w.snow_tombed_starsilver,w.whiteblind,w.prototype_archaic,
                   w.sacrificial_greatsword,w.lithic_blade,w.the_bell,w.rainslasher,w.favonius_greatsword,w.debate_club,
                   w.ferrous_shadow,w.bloodtainted_greatsword,

                   w.staff_of_homa,w.vortex_vanquisher,w.skyward_spine,w.primordial_jade_winged_spear,w.blackcliff_pole,
                   w.royal_spear,w.deathmatch,w.dragonspine_spear,w.prototype_starglitter,w.crescent_pike,w.lithic_spear,
                   w.favonius_lance,w.dragons_bane,w.black_tassel,

                   w.lost_prayer_to_the_sacred_winds,w.skyward_atlas,w.memory_of_dust,w.blackcliff_agate,w.royal_grimoire,
                   w.solar_pearl,w.mappa_mare,w.prototype_amber,w.frostbearer,w.eye_of_perception,w.the_widsith,
                   w.wine_and_song,w.favonious_codex,w.sacrificial_fragments,w.thrilling_tales,w.magic_guide,
                   w.emerald_orb,

                   w.amos_bow,w.elegy_of_the_end,w.skyward_harp,w.blackcliff_warbow,w.royal_bow,w.the_viridescent_hunt,
                   w.prototype_crescent,w.compound_bow,w.favonius_warbow,w.the_stringless,w.rust,w.sacrificial_bow,
                   w.alley_hunter,w.windblume_ode,w.slingshot,w.sharpshooters_oath,w.raven_bow]

# Character List combinations
star5_standard_characters = []
star5_promotional_characters = []
star5_upcoming_characters = []
star4_standard_characters = []
star4_upcoming_characters = []

all_5star_characters = []
all_4star_characters = []

# Weapon List combinations
star5_standar_weapons = []
star5_promotional_weapons = []
star4_standar_weapons = []
star4_promotional_weapons = []

shop_weapons = []
battlepass_weapons = []
limited_weapons = []
forging_weapons = []
star3_weapons = []

# ALL
all_5star_weapons = []
all_4star_weapons = []





# Adding to lists - Char
for obj in char_list_obj:
    if obj.char_type == 'perma' and obj.rarity == '5 Star' and obj.in_game is True:
        star5_standard_characters.append(obj.name)

for obj in char_list_obj:
    if obj.char_type == 'promo' and obj.rarity == '5 Star' and obj.in_game is True:
        star5_promotional_characters.append(obj.name)

for obj in char_list_obj:
    if obj.char_type == 'promo' and obj.rarity == '5 Star' and obj.in_game is False:
        star5_upcoming_characters.append(obj.name)

for obj in char_list_obj:
    if obj.char_type == 'perma' and obj.rarity == '4 Star' and obj.in_game is True:
        star4_standard_characters.append(obj.name)

for obj in char_list_obj:
    if obj.char_type == 'perma' and obj.rarity == '4 Star' and obj.in_game is False:
        star4_upcoming_characters.append(obj.name)

# Adding to lists - Weapons
for obj in weapon_list_obj:
    if obj.rarity == '5 Star' and obj.is_standard is True and obj.in_gacha is True:
        star5_standar_weapons.append(obj.name)

for obj in weapon_list_obj:
    if obj.rarity == '5 Star' and obj.is_standard is False and obj.in_gacha is True:
        star5_promotional_weapons.append(obj.name)

for obj in weapon_list_obj:
    if obj.rarity == '4 Star' and obj.is_standard is True and obj.in_gacha is True:
        star4_standar_weapons.append(obj.name)

for obj in weapon_list_obj:
    if obj.rarity == '4 Star' and obj.is_standard is False and obj.in_gacha is True:
        star4_promotional_weapons.append(obj.name)

for obj in weapon_list_obj:
    if obj.rarity == '3 Star' and obj.is_standard is True and obj.in_gacha is True:
        star3_weapons.append(obj.name)

for obj in weapon_list_obj:
    if obj.in_shop is True:
        shop_weapons.append(obj.name)

for obj in weapon_list_obj:
    if obj.in_battlepass is True:
        battlepass_weapons.append(obj.name)

for obj in weapon_list_obj:
    if obj.is_limited is True:
        limited_weapons.append(obj.name)

for obj in weapon_list_obj:
    if obj.is_forgeable is True:
        forging_weapons.append(obj.name)

# Char and Weapons
for obj in weapon_list_obj:
    if obj.rarity == '5 Star':
        all_5star_weapons.append(obj.name)

for obj in weapon_list_obj:
    if obj.rarity == '4 Star':
        all_4star_weapons.append(obj.name)


for obj in char_list_obj:
    if obj.rarity == '5 Star':
        all_5star_characters.append(obj.name)

for obj in char_list_obj:
    if obj.rarity == '4 Star':
        all_4star_characters.append(obj.name)


# All
all_4star = all_4star_characters + all_4star_weapons
all_5star = all_5star_characters + all_5star_weapons

# All 4 Star Characters except the OGs (Amber, Kaeya, Lisa) used in promotional banners
all_4star_standard_except_akl = star4_standard_characters.copy()
ogs = [c.amber.name, c.kaeya.name, c.lisa.name]
# -----
all_4star_standard_except_akl = [ele for ele in all_4star_standard_except_akl if ele not in ogs]
