import weapons as w
import weapon_description as d

# Note: The 3 Star weapons(and below rarity) that doesn't appear in gatcha, are not stated here.

# Temp:
# x = w.Sword(name='', rarity='Star', base_atk_min=, base_atk_max=,
#                          second_stat_type='', second_stat_min='%', second_stat_max='%',
#                          passive_name='', passive_description=,
#                          in_shop=False, in_gacha=False, in_battlepass=False, is_limited=False, is_forgeable=False,
#                          in_game=True)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ SWORDS ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 5 Star

freedom_sworn = w.Sword(name='Freedom-Sworn', rarity='5 Star', base_atk_min=46, base_atk_max=608,
                                 second_stat_type='Elemental Mastery', second_stat_min='43', second_stat_max='198',
                                 passive_name='Revolutionary Chorale', passive_description=d.revolutionary_chorale,
                                 in_shop=False, in_gacha=True, in_battlepass=False, is_limited=False,
                                 is_forgeable=False, is_standard=False)

primordial_jade_cutter = w.Sword(name='Primordial Jade Cutter', rarity='5 Star', base_atk_min=44, base_atk_max=542,
                                 second_stat_type='Crit Rate', second_stat_min='9.6%', second_stat_max='44.1%',
                                 passive_name='Protector\'s Virtue', passive_description=d.protectors_virtue,
                                 in_shop=False, in_gacha=True, in_battlepass=False, is_limited=False,
                                 is_forgeable=False, is_standard=True)

aquila_favonia = w.Sword(name='Aquila Favonia', rarity='5 Star', base_atk_min=48, base_atk_max=674,
                         second_stat_type='Physical DMG Bonus', second_stat_min='9%', second_stat_max='41.3%',
                         passive_name='Falcon\'s Defiance', passive_description=d.falcons_defiance, in_shop=False,
                         in_gacha=True, in_battlepass=False, is_limited=False, is_forgeable=False, is_standard=True)

summit_shaper = w.Sword(name='Summit Shaper', rarity='5 Star', base_atk_min=46, base_atk_max=608,
                        second_stat_type='ATK',
                        second_stat_min='10.8%', second_stat_max='49.6%', passive_name='Golden Majesty',
                        passive_description=d.golden_majesty, in_shop=False,
                        in_gacha=True,
                        in_battlepass=False, is_limited=False, is_forgeable=False, is_standard=True)

skyward_blade = w.Sword(name='Skyward Blade', rarity='5 Star', base_atk_min=46, base_atk_max=608,
                        second_stat_type='Energy Recharge',
                        second_stat_min='12%', second_stat_max='55.1%', passive_name='Sky-Piercing Fang',
                        passive_description=d.sky_piercing_fang, in_shop=False,
                        in_gacha=True,
                        in_battlepass=False, is_limited=False, is_forgeable=False, is_standard=True)

# 4 Star
blackcliff_longsword = w.Sword(name='Blackcliff Longsword', rarity='4 Star', base_atk_min=44, base_atk_max=565,
                               second_stat_type='Crit Damage', second_stat_min='8%', second_stat_max='35.8%',
                               passive_name='Press the Advantage', passive_description=d.press_the_advantage,
                               in_shop=True,
                               in_gacha=False, in_battlepass=False, is_limited=False, is_forgeable=False,
                               is_standard=False)

royal_longsword = w.Sword(name='Royal Longsword', rarity='4 Star', base_atk_min=42, base_atk_max=510,
                          second_stat_type='ATK', second_stat_min='9%', second_stat_max='41.3%',
                          passive_name='Focus', passive_description=d.focus, in_shop=True, in_gacha=False,
                          in_battlepass=False, is_limited=False, is_forgeable=False, is_standard=False)

the_black_sword = w.Sword(name='The Black Sword', rarity='4 Star', base_atk_min=42, base_atk_max=510,
                          second_stat_type='Crit Rate', second_stat_min='6%', second_stat_max='27.6%',
                          passive_name='Justice', passive_description=d.justice, in_shop=False, in_gacha=False,
                          in_battlepass=True, is_limited=False, is_forgeable=False, is_standard=False)

iron_sting = w.Sword(name='Iron Sting', rarity='4 Star', base_atk_min=42, base_atk_max=510,
                     second_stat_type='Elemental Mastery', second_stat_min='36', second_stat_max='165',
                     passive_name='Infusion Stinger', passive_description=d.infusion_stinger, in_shop=False,
                     in_gacha=False,
                     in_battlepass=False, is_limited=False, is_forgeable=True, is_standard=False)

prototype_rancour = w.Sword(name='Prototype Rancour', rarity='4 Star', base_atk_min=44, base_atk_max=565,
                            second_stat_type='Physical DMG Bonus', second_stat_min='7.5%', second_stat_max='34.5%',
                            passive_name='Smashed Stone', passive_description=d.smashed_stone, in_shop=False,
                            in_gacha=False,
                            in_battlepass=False, is_limited=False, is_forgeable=True, is_standard=False)

favonius_sword = w.Sword(name='Favonius Sword', rarity='4 Star', base_atk_min=41, base_atk_max=454,
                         second_stat_type='Energy Recharge', second_stat_min='13.3%', second_stat_max='61.3%',
                         passive_name='Windfall', passive_description=d.windfall, in_shop=False, in_gacha=True,
                         in_battlepass=False, is_limited=False, is_forgeable=False, is_standard=True)

lions_roar = w.Sword(name='Lion\'s Roar', rarity='4 Star', base_atk_min=42, base_atk_max=510,
                     second_stat_type='ATK', second_stat_min='9%', second_stat_max='41.3%',
                     passive_name='Bane of Fire and Thunder', passive_description=d.bane_of_fire_and_thunder,
                     in_shop=False, in_gacha=True, in_battlepass=False, is_limited=False, is_forgeable=False,
                     is_standard=True)

sacrificial_sword = w.Sword(name='Sacrificial Sword', rarity='4 Star', base_atk_min=41, base_atk_max=454,
                            second_stat_type='Energy Recharge', second_stat_min='13.3%', second_stat_max='61.3%',
                            passive_name='Composed', passive_description=d.composed,
                            in_shop=False, in_gacha=True, in_battlepass=False, is_limited=False, is_forgeable=False,
                            is_standard=True)

the_flute = w.Sword(name='The Flute', rarity='4 Star', base_atk_min=42, base_atk_max=510,
                    second_stat_type='ATK', second_stat_min='9%', second_stat_max='41.3%',
                    passive_name='Chord', passive_description=d.chord,
                    in_shop=False, in_gacha=True, in_battlepass=False, is_limited=False, is_forgeable=False,
                    is_standard=True)

the_alley_flash = w.Sword(name='The Alley Flash', rarity='4 Star', base_atk_min=45, base_atk_max=620,
                          second_stat_type='Elemental Mastery', second_stat_min='12', second_stat_max='55',
                          passive_name='Itinerant Hero', passive_description=d.itinerant_hero, in_shop=False,
                          in_gacha=True,
                          in_battlepass=False, is_limited=False, is_forgeable=False, is_standard=False)

festering_desire = w.Sword(name='Festering Desire', rarity='4 Star', base_atk_min=42, base_atk_max=510,
                           second_stat_type='Energy Recharge', second_stat_min='10%', second_stat_max='45.9%',
                           passive_name='Undying Admiration', passive_description=d.undying_admiration, in_shop=False,
                           in_gacha=False,
                           in_battlepass=False, is_limited=True, is_forgeable=False, is_standard=False)
# Playstation Exclusive
sword_of_descension = w.Sword(name='Sword of Descension', rarity='4 Star', base_atk_min=39, base_atk_max=440,
                              second_stat_type='ATK', second_stat_min='7.7%', second_stat_max='35.2%',
                              passive_name='Descension', passive_description=d.descension,
                              in_shop=False, in_gacha=False,
                              in_battlepass=False, is_limited=True, is_forgeable=False, is_standard=False)

# 3 Star
cool_steel = w.Sword(name='Cool Steel', rarity='3 Star', base_atk_min=39, base_atk_max=401,
                     second_stat_type='ATK', second_stat_min='7.7%', second_stat_max='35.2%',
                     passive_name='Bane of Water and Ice', passive_description=d.bane_of_water_and_ice, in_shop=False,
                     in_gacha=True, in_battlepass=False, is_limited=False, is_forgeable=False, is_standard=True)

harbinger_of_dawn = w.Sword(name='Harbinger of Dawn', rarity='3 Star', base_atk_min=39, base_atk_max=401,
                            second_stat_type='Crit Damage', second_stat_min='10.2%', second_stat_max='46.9%',
                            passive_name='Vigorous', passive_description=d.vigorous, in_shop=False, in_gacha=True,
                            in_battlepass=False, is_limited=False, is_forgeable=False, is_standard=True)

skyrider_sword = w.Sword(name='Skyrider Sword', rarity='3 Star', base_atk_min=38, base_atk_max=354,
                         second_stat_type='Energy Recharge', second_stat_min='11.3%', second_stat_max='51.7%',
                         passive_name='Determination', passive_description=d.determination,
                         in_shop=False, in_gacha=True, in_battlepass=False, is_limited=False, is_forgeable=False,
                         is_standard=True)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ CLAYMORES ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 5 Star
song_of_broken_pines = w.Claymore(name='Song of Broken Pines', rarity='5 Star', base_atk_min=49, base_atk_max=741,
                                  second_stat_type='Physical DMG Bonus', second_stat_min='4.5%',
                                  second_stat_max='20.7%',
                                  passive_name='Rebel\'s Banner-Hymn', passive_description=d.rebels_banner_hymn,
                                  in_shop=False, in_gacha=True, in_battlepass=False, is_limited=False,
                                  is_forgeable=False,
                                  is_standard=False)

skyward_pride = w.Claymore(name='Skyward Pride', rarity='5 Star', base_atk_min=48, base_atk_max=674,
                           second_stat_type='Energy Recharge', second_stat_min='8%', second_stat_max='36.8%',
                           passive_name='Sky-ripping Dragon Spine', passive_description=d.sky_ripping_dragon_spine,
                           in_shop=False, in_gacha=True, in_battlepass=False, is_limited=False, is_forgeable=False,
                           is_standard=True)

the_unforged = w.Claymore(name='The Unforged', rarity='5 Star', base_atk_min=46, base_atk_max=608,
                          second_stat_type='ATK', second_stat_min='10.8%', second_stat_max='49.6%',
                          passive_name='Golden Majesty', passive_description=d.golden_majesty,
                          in_shop=False, in_gacha=True, in_battlepass=False, is_limited=False, is_forgeable=False,
                          is_standard=True)

wolfs_gravestone = w.Claymore(name='Wolf\'s Gravestone', rarity='5 Star', base_atk_min=46, base_atk_max=608,
                              second_stat_type='ATK', second_stat_min='10.8%', second_stat_max='49.6%',
                              passive_name='Wolfish Tracker', passive_description=d.wolfish_tracker,
                              in_shop=False, in_gacha=True, in_battlepass=False, is_limited=False, is_forgeable=False,
                              is_standard=True)

# 4 Star
blackcliff_slasher = w.Claymore(name='Blackcliff Slasher', rarity='4 Star', base_atk_min=42, base_atk_max=510,
                                second_stat_type='Crit Damage', second_stat_min='12%', second_stat_max='55.1%',
                                passive_name='Press the Advantage', passive_description=d.press_the_advantage,
                                in_shop=True, in_gacha=False, in_battlepass=False, is_limited=False,
                                is_forgeable=False, is_standard=False)

royal_greatsword = w.Claymore(name='Royal Greatsword', rarity='4 Star', base_atk_min=44, base_atk_max=565,
                              second_stat_type='ATK', second_stat_min='6%', second_stat_max='27.6%',
                              passive_name='Focus', passive_description=d.focus,
                              in_shop=True, in_gacha=False, in_battlepass=False, is_limited=False, is_forgeable=False,
                              is_standard=False)

serpent_spine = w.Claymore(name='Serpent Spine', rarity='4 Star', base_atk_min=42, base_atk_max=510,
                           second_stat_type='Crit Rate', second_stat_min='6%', second_stat_max='27.6%',
                           passive_name='Wavesplitter', passive_description=d.wavesplitter,
                           in_shop=False, in_gacha=False, in_battlepass=True, is_limited=False, is_forgeable=False,
                           is_standard=False)

snow_tombed_starsilver = w.Claymore(name='Snow-Tombed Starsilver', rarity='4 Star', base_atk_min=44, base_atk_max=565,
                                    second_stat_type='Physical DMG Bonus', second_stat_min='7.5%',
                                    second_stat_max='34.5%',
                                    passive_name='Frost Burial', passive_description=d.frost_burial,
                                    in_shop=False, in_gacha=False, in_battlepass=False, is_limited=False,
                                    is_forgeable=True, is_standard=False)

whiteblind = w.Claymore(name='Whiteblind', rarity='4 Star', base_atk_min=42, base_atk_max=510,
                        second_stat_type='DEF', second_stat_min='11.3%', second_stat_max='51.7%',
                        passive_name='Infusion Blade', passive_description=d.infusion_blade,
                        in_shop=False, in_gacha=False, in_battlepass=False, is_limited=False, is_forgeable=True,
                        is_standard=False)

prototype_archaic = w.Claymore(name='Prototype Archaic', rarity='4 Star', base_atk_min=44, base_atk_max=565,
                               second_stat_type='ATK', second_stat_min='6%', second_stat_max='27.6%',
                               passive_name='Crush', passive_description=d.crush,
                               in_shop=False, in_gacha=False, in_battlepass=False, is_limited=False, is_forgeable=True,
                               is_standard=False)

sacrificial_greatsword = w.Claymore(name='Sacrificial Greatsword', rarity='4 Star', base_atk_min=44, base_atk_max=565,
                                    second_stat_type='Energy Recharge', second_stat_min='6.7%', second_stat_max='30.6%',
                                    passive_name='Composed', passive_description=d.composed,
                                    in_shop=False, in_gacha=True, in_battlepass=False, is_limited=False,
                                    is_forgeable=False,
                                    is_standard=True)

lithic_blade = w.Claymore(name='Lithic Blade', rarity='4 Star', base_atk_min=42, base_atk_max=510,
                          second_stat_type='ATK', second_stat_min='9%', second_stat_max='41.3%',
                          passive_name='Lithic Axiom - Unity', passive_description=d.lithic_axiom_unity,
                          in_shop=False, in_gacha=True, in_battlepass=False, is_limited=False, is_forgeable=False,
                          is_standard=False)

the_bell = w.Claymore(name='The Bell', rarity='4 Star', base_atk_min=42, base_atk_max=510,
                      second_stat_type='HP', second_stat_min='9%', second_stat_max='41.3%',
                      passive_name='Rebellious Guardian', passive_description=d.rebellious_guardian,
                      in_shop=False, in_gacha=True, in_battlepass=False, is_limited=False, is_forgeable=False,
                      is_standard=True)

rainslasher = w.Claymore(name='Rainslasher', rarity='4 Star', base_atk_min=41, base_atk_max=510,
                         second_stat_type='Elemental Mastery', second_stat_min='36%', second_stat_max='165%',
                         passive_name='Bane of Storm and Tide', passive_description=d.bane_of_storm_and_tide,
                         in_shop=False, in_gacha=True, in_battlepass=False, is_limited=False, is_forgeable=False,
                         is_standard=True)

favonius_greatsword = w.Claymore(name='Favonius Greatsword', rarity='4 Star', base_atk_min=41, base_atk_max=454,
                                 second_stat_type='Energy Recharge', second_stat_min='13.3%', second_stat_max='61.3%',
                                 passive_name='Windfall', passive_description=d.windfall,
                                 in_shop=False, in_gacha=True, in_battlepass=False, is_limited=False,
                                 is_forgeable=False,
                                 is_standard=True)

# 3 Star
ferrous_shadow = w.Claymore(name='Ferrous Shadow', rarity='3 Star', base_atk_min=39, base_atk_max=401,
                            second_stat_type='HP', second_stat_min='7.7%', second_stat_max='35.2%',
                            passive_name='Unbending', passive_description=d.unbending,
                            in_shop=False, in_gacha=True, in_battlepass=False, is_limited=False, is_forgeable=False,
                            is_standard=True)

debate_club = w.Claymore(name='Debate Club', rarity='3 Star', base_atk_min=39, base_atk_max=401,
                         second_stat_type='ATK', second_stat_min='7.7%', second_stat_max='35.2%',
                         passive_name='Blunt Conclusion', passive_description=d.blunt_conclusion,
                         in_shop=False, in_gacha=True, in_battlepass=False, is_limited=False, is_forgeable=False,
                         is_standard=True)

bloodtainted_greatsword = w.Claymore(name='Bloodtainted Greatsword', rarity='3 Star', base_atk_min=38, base_atk_max=354,
                                     second_stat_type='Elemental Mastery', second_stat_min='41', second_stat_max='187',
                                     passive_name='Bane of Fire and Thunder',
                                     passive_description=d.bane_of_fire_and_thunder,
                                     in_shop=False, in_gacha=True, in_battlepass=False, is_limited=False,
                                     is_forgeable=False,
                                     is_standard=True)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ POLEARMS ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 5 Star
staff_of_homa = w.Polearm(name='Staff of Homa', rarity='5 Star', base_atk_min=46, base_atk_max=608,
                          second_stat_type='Crit Damage', second_stat_min='14.4%', second_stat_max='66.2%',
                          passive_name='Reckless Cinnabar', passive_description=d.reckless_cinnabar,
                          in_shop=False, in_gacha=True, in_battlepass=False, is_limited=False, is_forgeable=False,
                          is_standard=False)

vortex_vanquisher = w.Polearm(name='Vortex Vanquisher', rarity='5 Star', base_atk_min=46, base_atk_max=608,
                              second_stat_type='ATK', second_stat_min='%', second_stat_max='%',
                              passive_name='Golden Majesty', passive_description=d.golden_majesty,
                              in_shop=False, in_gacha=True, in_battlepass=False, is_limited=False, is_forgeable=False,
                              is_standard=True)

skyward_spine = w.Polearm(name='Skyward Spine', rarity='5 Star', base_atk_min=48, base_atk_max=674,
                          second_stat_type='Energy Recharge', second_stat_min='8%', second_stat_max='36.8%',
                          passive_name='Blackwing', passive_description=d.blackwing,
                          in_shop=False, in_gacha=True, in_battlepass=False, is_limited=False, is_forgeable=False,
                          is_standard=True)

primordial_jade_winged_spear = w.Polearm(name='Primordial Jade Winged-Spear', rarity='5 Star', base_atk_min=48,
                                         base_atk_max=674, second_stat_type='Crit Rate', second_stat_min='4.8%',
                                         second_stat_max='22.1%', passive_name='Eagle Spear of Justice',
                                         passive_description=d.eagle_spear_of_justice,
                                         in_shop=False, in_gacha=True, in_battlepass=False, is_limited=False,
                                         is_forgeable=False, is_standard=True)

# 4 Star
blackcliff_pole = w.Polearm(name='Blackcliff Pole', rarity='4 Star', base_atk_min=42, base_atk_max=510,
                            second_stat_type='Crit Damage', second_stat_min='12%', second_stat_max='55.1%',
                            passive_name='Press the Advantage', passive_description=d.press_the_advantage,
                            in_shop=True, in_gacha=False, in_battlepass=False, is_limited=False, is_forgeable=False,
                            is_standard=False)

royal_spear = w.Polearm(name='Royal Spear', rarity='4 Star', base_atk_min=44, base_atk_max=565,
                        second_stat_type='ATK', second_stat_min='6%', second_stat_max='27.6%',
                        passive_name='Focus', passive_description=d.focus,
                        in_shop=True, in_gacha=False, in_battlepass=False, is_limited=False, is_forgeable=False,
                        is_standard=False)

deathmatch = w.Polearm(name='Deathmatch', rarity='4 Star', base_atk_min=41, base_atk_max=454,
                       second_stat_type='Crit Rate', second_stat_min='8%', second_stat_max='36.8%',
                       passive_name='Gladiator', passive_description=d.gladiator,
                       in_shop=False, in_gacha=False, in_battlepass=True, is_limited=False, is_forgeable=False,
                       is_standard=False)

dragonspine_spear = w.Polearm(name='Dragonspine Spear', rarity='4 Star', base_atk_min=41, base_atk_max=454,
                              second_stat_type='Physical DMG Bonus', second_stat_min='15%', second_stat_max='69%',
                              passive_name='Frost Burial', passive_description=d.frost_burial,
                              in_shop=False, in_gacha=False, in_battlepass=False, is_limited=False, is_forgeable=True,
                              is_standard=False)

prototype_starglitter = w.Polearm(name='Prototype Starglitter', rarity='4 Star', base_atk_min=42, base_atk_max=510,
                                  second_stat_type='Energy Recharge', second_stat_min='10%', second_stat_max='45.9%',
                                  passive_name='Magic Affinity', passive_description=d.magic_affinity,
                                  in_shop=False, in_gacha=False, in_battlepass=False, is_limited=False,
                                  is_forgeable=True,
                                  is_standard=False)

crescent_pike = w.Polearm(name='Crescent Pike', rarity='4 Star', base_atk_min=44, base_atk_max=565,
                          second_stat_type='Physical DMG Bonus', second_stat_min='7.5%', second_stat_max='34.5%',
                          passive_name='Infusion Needle', passive_description=d.infusion_needle,
                          in_shop=False, in_gacha=False, in_battlepass=False, is_limited=False, is_forgeable=True,
                          is_standard=False)

lithic_spear = w.Polearm(name='Lithic Spear', rarity='4 Star', base_atk_min=44, base_atk_max=565,
                         second_stat_type='ATK', second_stat_min='6%', second_stat_max='27.6%',
                         passive_name='Lithic Axiom - Unity', passive_description=d.lithic_axiom_unity,
                         in_shop=False, in_gacha=True, in_battlepass=False, is_limited=False, is_forgeable=False,
                         is_standard=False)

favonius_lance = w.Polearm(name='Favonius Lance', rarity='4 Star', base_atk_min=44, base_atk_max=565,
                           second_stat_type='Energy Recharge', second_stat_min='6.7%', second_stat_max='30.6%',
                           passive_name='Windfall', passive_description=d.windfall,
                           in_shop=False, in_gacha=True, in_battlepass=False, is_limited=False, is_forgeable=False,
                           is_standard=True)

dragons_bane = w.Polearm(name='Dragon\'s Bane', rarity='4 Star', base_atk_min=41, base_atk_max=454,
                         second_stat_type='Elemental Mastery', second_stat_min='48', second_stat_max='221',
                         passive_name='Bane of Flame and Water', passive_description=d.bane_of_flame_and_water,
                         in_shop=False, in_gacha=True, in_battlepass=False, is_limited=False, is_forgeable=False,
                         is_standard=True)

# 3 Star
black_tassel = w.Polearm(name='Black Tassel', rarity='3 Star', base_atk_min=38, base_atk_max=354,
                         second_stat_type='HP', second_stat_min='10.2%', second_stat_max='46.9%',
                         passive_name='Bane of the Soft', passive_description=d.bane_of_the_soft,
                         in_shop=False, in_gacha=True, in_battlepass=False, is_limited=False, is_forgeable=False,
                         is_standard=True)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ CATALYSTS ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 5 Star
lost_prayer_to_the_sacred_winds = w.Catalyst(name='Lost Prayer to the Sacred Winds', rarity='5 Star', base_atk_min=46,
                                             base_atk_max=608, second_stat_type='Crit Rate', second_stat_min='7.2%',
                                             second_stat_max='33.1%',
                                             passive_name='Boundless Blessing',
                                             passive_description=d.boundless_blessing,
                                             in_shop=False, in_gacha=True, in_battlepass=False, is_limited=False,
                                             is_forgeable=False,
                                             is_standard=True)

memory_of_dust = w.Catalyst(name='Memory of Dust', rarity='5 Star', base_atk_min=46, base_atk_max=608,
                            second_stat_type='ATK', second_stat_min='10.8%', second_stat_max='49.6%',
                            passive_name='Golden Majesty', passive_description=d.golden_majesty,
                            in_shop=False, in_gacha=True, in_battlepass=False, is_limited=False, is_forgeable=False,
                            is_standard=True)

skyward_atlas = w.Catalyst(name='Skyward Atlas', rarity='5 Star', base_atk_min=48, base_atk_max=674,
                           second_stat_type='ATK', second_stat_min='7.2%', second_stat_max='33.1%',
                           passive_name='Wandering Clouds', passive_description=d.wandering_clouds,
                           in_shop=False, in_gacha=True, in_battlepass=False, is_limited=False, is_forgeable=False,
                           is_standard=True)

# 4 Star
blackcliff_agate = w.Catalyst(name='Blackcliff Agate', rarity='4 Star', base_atk_min=42, base_atk_max=510,
                              second_stat_type='Crit Damage', second_stat_min='12%', second_stat_max='55.1%',
                              passive_name='Press the Advantage', passive_description=d.press_the_advantage,
                              in_shop=True, in_gacha=False, in_battlepass=False, is_limited=False, is_forgeable=False,
                              is_standard=False)

royal_grimoire = w.Catalyst(name='Royal Grimoire', rarity='4 Star', base_atk_min=44, base_atk_max=565,
                            second_stat_type='ATK', second_stat_min='6%', second_stat_max='27.6%',
                            passive_name='Focus', passive_description=d.focus,
                            in_shop=True, in_gacha=False, in_battlepass=False, is_limited=False, is_forgeable=False,
                            is_standard=False)

solar_pearl = w.Catalyst(name='Solar Pearl', rarity='4 Star', base_atk_min=42, base_atk_max=510,
                         second_stat_type='Crit Rate', second_stat_min='6%', second_stat_max='27.6%',
                         passive_name='Solar Shine', passive_description=d.solar_shine,
                         in_shop=False, in_gacha=False, in_battlepass=True, is_limited=False, is_forgeable=False,
                         is_standard=False)

mappa_mare = w.Catalyst(name='Mappa Mare', rarity='4 Star', base_atk_min=44, base_atk_max=565,
                        second_stat_type='Elemental Mastery', second_stat_min='24', second_stat_max='110',
                        passive_name='Infusion Scroll', passive_description=d.infusion_scroll,
                        in_shop=False, in_gacha=False, in_battlepass=False, is_limited=False, is_forgeable=True,
                        is_standard=False)

prototype_amber = w.Catalyst(name='Prototype Amber', rarity='4 Star', base_atk_min=42, base_atk_max=510,
                             second_stat_type='HP', second_stat_min='9%', second_stat_max='41.3%',
                             passive_name='Gilding', passive_description=d.gilding,
                             in_shop=False, in_gacha=False, in_battlepass=False, is_limited=False, is_forgeable=True,
                             is_standard=False)

frostbearer = w.Catalyst(name='Frostbearer', rarity='4 Star', base_atk_min=42, base_atk_max=510,
                         second_stat_type='ATK', second_stat_min='9%', second_stat_max='41.3%',
                         passive_name='Frost Burial', passive_description=d.frost_burial,
                         in_shop=False, in_gacha=False, in_battlepass=False, is_limited=False, is_forgeable=True,
                         is_standard=False)

eye_of_perception = w.Catalyst(name='Eye of Perception', rarity='4 Star', base_atk_min=41, base_atk_max=454,
                               second_stat_type='ATK', second_stat_min='12%', second_stat_max='55.1%',
                               passive_name='Echo', passive_description=d.echo,
                               in_shop=False, in_gacha=True, in_battlepass=False, is_limited=False, is_forgeable=False,
                               is_standard=True)

the_widsith = w.Catalyst(name='The Widsith', rarity='4 Star', base_atk_min=42, base_atk_max=510,
                         second_stat_type='Crit Damage', second_stat_min='12%', second_stat_max='55.1%',
                         passive_name='debut', passive_description=d.debut,
                         in_shop=False, in_gacha=True, in_battlepass=False, is_limited=False, is_forgeable=False,
                         is_standard=True)

wine_and_song = w.Catalyst(name='Wine and Song', rarity='4 Star', base_atk_min=44, base_atk_max=565,
                           second_stat_type='Energy Recharge', second_stat_min='6.7%', second_stat_max='30.6%',
                           passive_name='Ever-Changing', passive_description=d.ever_changing,
                           in_shop=False, in_gacha=True, in_battlepass=False, is_limited=False, is_forgeable=False,
                           is_standard=False)

sacrificial_fragments = w.Catalyst(name='Sacrificial Fragments', rarity='4 Star', base_atk_min=41, base_atk_max=454,
                                   second_stat_type='Elemental Mastery', second_stat_min='48', second_stat_max='221',
                                   passive_name='Composed', passive_description=d.composed,
                                   in_shop=False, in_gacha=True, in_battlepass=False, is_limited=False,
                                   is_forgeable=False, is_standard=True)

favonious_codex = w.Catalyst(name='Favonius Codex', rarity='4 Star', base_atk_min=42, base_atk_max=510,
                             second_stat_type='Energy Recharge', second_stat_min='10%', second_stat_max='45.9%',
                             passive_name='Windfall', passive_description=d.windfall,
                             in_shop=False, in_gacha=True, in_battlepass=False, is_limited=False, is_forgeable=False,
                             is_standard=True)

# 3 Star
thrilling_tales = w.Catalyst(name='Thrilling Tales of Dragon Slayers', rarity='3 Star', base_atk_min=39,
                             base_atk_max=401, second_stat_type='HP', second_stat_min='7.7%', second_stat_max='35.2%',
                             passive_name='Legacy', passive_description=d.legacy, in_shop=False, in_gacha=True,
                             in_battlepass=False, is_limited=False, is_forgeable=False, is_standard=True)

magic_guide = w.Catalyst(name='Magic Guide', rarity='3 Star', base_atk_min=38, base_atk_max=354,
                         second_stat_type='Elemental Mastery', second_stat_min='41', second_stat_max='187',
                         passive_name='Bane of Storm and Tide', passive_description=d.bane_of_storm_and_tide,
                         in_shop=False, in_gacha=True, in_battlepass=False, is_limited=False, is_forgeable=False,
                         is_standard=True)

emerald_orb = w.Catalyst(name='Emerald Orb', rarity='3 Star', base_atk_min=40, base_atk_max=448,
                         second_stat_type='Elemental Mastery', second_stat_min='20', second_stat_max='94',
                         passive_name='Rapids', passive_description=d.rapids, in_shop=False, in_gacha=True,
                         in_battlepass=False, is_limited=False, is_forgeable=False, is_standard=True)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ BOWS ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 5 Star
amos_bow = w.Bow(name='Amos\' Bow', rarity='5 Star', base_atk_min=46, base_atk_max=608,
                 second_stat_type='ATK', second_stat_min='10.8%', second_stat_max='49.6%',
                 passive_name='Strong-Willed', passive_description=d.strong_willed,
                 in_shop=False, in_gacha=True, in_battlepass=False, is_limited=False, is_forgeable=False,
                 is_standard=True)

elegy_of_the_end = w.Bow(name='Elegy for the End', rarity='5 Star', base_atk_min=46, base_atk_max=608,
                         second_stat_type='Energy Recharge', second_stat_min='12%', second_stat_max='55.1%',
                         passive_name='The Parting Refrain', passive_description=d.the_parting_refrain,
                         in_shop=False, in_gacha=True, in_battlepass=False, is_limited=False, is_forgeable=False,
                         is_standard=False)

skyward_harp = w.Bow(name='Skyward Harp', rarity='5 Star', base_atk_min=48, base_atk_max=674,
                     second_stat_type='Crit Rate', second_stat_min='4.8%', second_stat_max='22.1%',
                     passive_name='Echoing Ballad', passive_description=d.echoing_ballad,
                     in_shop=False, in_gacha=True, in_battlepass=False, is_limited=False, is_forgeable=False,
                     is_standard=True)

# 4 Star
blackcliff_warbow = w.Bow(name='Blackcliff Warbow', rarity='4 Star', base_atk_min=44, base_atk_max=565,
                          second_stat_type='Crit Damage', second_stat_min='8%', second_stat_max='36.8%',
                          passive_name='Press the Advantage', passive_description=d.press_the_advantage,
                          in_shop=True, in_gacha=False, in_battlepass=False, is_limited=False, is_forgeable=False,
                          is_standard=False)

royal_bow = w.Bow(name='Royal Bow', rarity='4 Star', base_atk_min=42, base_atk_max=510,
                  second_stat_type='ATK', second_stat_min='9%', second_stat_max='41.3%',
                  passive_name='Focus', passive_description=d.focus,
                  in_shop=True, in_gacha=False, in_battlepass=False, is_limited=False, is_forgeable=False,
                  is_standard=False)

the_viridescent_hunt = w.Bow(name='The Viridescent Hunt', rarity='4 Star', base_atk_min=42, base_atk_max=510,
                             second_stat_type='Crit Rate', second_stat_min='6%', second_stat_max='27.6%',
                             passive_name='Verdant Wind', passive_description=d.verdant_wind,
                             in_shop=False, in_gacha=False, in_battlepass=True, is_limited=False, is_forgeable=False,
                             is_standard=False)

prototype_crescent = w.Bow(name='Prototype Crescent', rarity='4 Star', base_atk_min=42, base_atk_max=510,
                           second_stat_type='ATK', second_stat_min='9%', second_stat_max='41.3%',
                           passive_name='Unreturning', passive_description=d.unreturning,
                           in_shop=False, in_gacha=False, in_battlepass=False, is_limited=False, is_forgeable=True,
                           is_standard=False)

compound_bow = w.Bow(name='Compound Bow', rarity='4 Star', base_atk_min=41, base_atk_max=454,
                     second_stat_type='Physical DMG Bonus', second_stat_min='15%', second_stat_max='69.9%',
                     passive_name='Infusion Arrow', passive_description=d.infusion_arrow,
                     in_shop=False, in_gacha=False, in_battlepass=False, is_limited=False, is_forgeable=True,
                     is_standard=False)

favonius_warbow = w.Bow(name='Favonius Warbow', rarity='4 Star', base_atk_min=41, base_atk_max=454,
                        second_stat_type='Energy Recharge', second_stat_min='13.3%', second_stat_max='61.3%',
                        passive_name='Windfall', passive_description=d.windfall,
                        in_shop=False, in_gacha=True, in_battlepass=False, is_limited=False, is_forgeable=False,
                        is_standard=True)

the_stringless = w.Bow(name='The Stringless', rarity='4 Star', base_atk_min=42, base_atk_max=510,
                       second_stat_type='Elemental Mastery', second_stat_min='36', second_stat_max='165',
                       passive_name='Arrowless Song', passive_description=d.arrowless_song,
                       in_shop=False, in_gacha=True, in_battlepass=False, is_limited=False, is_forgeable=False,
                       is_standard=True)

rust = w.Bow(name='Rust', rarity='4 Star', base_atk_min=42, base_atk_max=510,
             second_stat_type='ATK', second_stat_min='9%', second_stat_max='41.3%',
             passive_name='Rapid Firing', passive_description=d.rapid_firing,
             in_shop=False, in_gacha=True, in_battlepass=False, is_limited=False, is_forgeable=False,
             is_standard=True)

sacrificial_bow = w.Bow(name='Sacrificial Bow', rarity='4 Star', base_atk_min=44, base_atk_max=565,
                        second_stat_type='Energy Recharge', second_stat_min='6.7%', second_stat_max='30.6%',
                        passive_name='Composed', passive_description=d.composed,
                        in_shop=False, in_gacha=True, in_battlepass=False, is_limited=False, is_forgeable=False,
                        is_standard=True)

alley_hunter = w.Bow(name='Alley Hunter', rarity='4 Star', base_atk_min=44, base_atk_max=565,
                     second_stat_type='ATK', second_stat_min='6%', second_stat_max='27.6%',
                     passive_name='Urban Guerrilla', passive_description=d.urban_guerrilla,
                     in_shop=False, in_gacha=True, in_battlepass=False, is_limited=False, is_forgeable=False,
                     is_standard=False)

windblume_ode = w.Bow(name='Windblume Ode', rarity='4 Star', base_atk_min=42, base_atk_max=510,
                      second_stat_type='Elemental Mastery', second_stat_min='36', second_stat_max='165',
                      passive_name='Windblume Wish', passive_description=d.windblume_wish,
                      in_shop=False, in_gacha=False, in_battlepass=False, is_limited=True, is_forgeable=False,
                      is_standard=False)

# 3 Star
slingshot = w.Bow(name='Slingshot', rarity='3 Star', base_atk_min=38, base_atk_max=354,
                  second_stat_type='Crit Rate', second_stat_min='6.8%', second_stat_max='31.2%',
                  passive_name='Slingshot', passive_description=d.slingshot,
                  in_shop=False, in_gacha=True, in_battlepass=False, is_limited=False, is_forgeable=False,
                  is_standard=True)

sharpshooters_oath = w.Bow(name='Sharpshooter\'s Oath', rarity='3 Star', base_atk_min=39, base_atk_max=401,
                           second_stat_type='Crit Damage', second_stat_min='10.2%', second_stat_max='46.9%',
                           passive_name='Precise', passive_description=d.precise,
                           in_shop=False, in_gacha=True, in_battlepass=False, is_limited=False, is_forgeable=False,
                           is_standard=True)

raven_bow = w.Bow(name='Raven Bow', rarity='3 Star', base_atk_min=40, base_atk_max=448,
                  second_stat_type='Elemental Mastery', second_stat_min='20', second_stat_max='94',
                  passive_name='Bane of Flame and Water', passive_description=d.bane_of_flame_and_water,
                  in_shop=False, in_gacha=True, in_battlepass=False, is_limited=False, is_forgeable=False,
                  is_standard=True)
