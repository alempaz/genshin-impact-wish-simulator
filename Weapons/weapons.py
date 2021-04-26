class Weapon:
    def __init__(self, name, rarity, base_atk_min, base_atk_max, second_stat_type, second_stat_min, second_stat_max,
                 passive_name, passive_description,
                 in_shop, in_gacha, in_battlepass, is_limited, is_forgeable, is_standard, level=1, refinement_level=1,
                 ascension=1):
        """
        :param name: Name of the weapon
        :param rarity: Rarity of the weapon. | 3 Star, 4 Star, 5 Star
        :param base_atk_min: Minimum base ATK of the weapon at level 1
        :param base_atk_max: Maximum base ATK of the weapon at level 90
        :param second_stat_type: Secondary stat type of the weapon, Example: ATK%, Crit Rate, Energy Recharge.
        :param second_stat_min: Minimum secondary stat of the weapon at level 1
        :param second_stat_max: Maximum secondary stat of the weapon at level 90
        :param passive_name: Passive ability name of the weapon
        :param passive_description: Passive ability description
        :param in_shop: Is the weapon available in the shop? | True, False
        :param in_gacha: Is the weapon available in the wish system? | True, False
        :param in_battlepass: Is the weapon available in the battlepass? | True, False
        :param is_limited: Is the weapon available for a limited time? | True, False
        :param is_forgeable: Is the weapon forgeable in-game with a prototype? | True, False
        :param is_standard: Is the weapon available in the standard banner? | True, False
        :param level: Level of the weapon. Weapon level 1 by default
        :param refinement_level: Refinement of the weapon. Refinement Level 1 by default
        :param ascension: Ascension level of the weapon. Ascension Level 1 by default
        """
        self.name = name
        self.rarity = rarity
        self.base_atk_min = base_atk_min
        self.base_atk_max = base_atk_max
        self.secondary_stat_type = second_stat_type
        self.secondary_stat_min = second_stat_min
        self.secondary_stat_max = second_stat_max
        self.passive_name = passive_name
        self.passive_description = passive_description
        self.in_shop = in_shop
        self.in_gacha = in_gacha
        self.in_battlepass = in_battlepass
        self.is_limited = is_limited
        self.is_forgeable = is_forgeable
        self.is_standard = is_standard
        self.level = level
        self.refinement_level = refinement_level
        self.ascension = ascension


class Sword(Weapon):
    def __init__(self, name, rarity, base_atk_min, base_atk_max, second_stat_type, second_stat_min, second_stat_max,
                 passive_name, passive_description,
                 in_shop, in_gacha, in_battlepass, is_limited, is_forgeable, is_standard):
        super().__init__(name, rarity, base_atk_min, base_atk_max, second_stat_type, second_stat_min, second_stat_max,
                         passive_name, passive_description,
                         in_shop, in_gacha, in_battlepass, is_limited, is_forgeable, is_standard, level=1,
                         refinement_level=1,
                         ascension=1)


class Claymore(Weapon):
    def __init__(self, name, rarity, base_atk_min, base_atk_max, second_stat_type, second_stat_min, second_stat_max,
                 passive_name, passive_description,
                 in_shop, in_gacha, in_battlepass, is_limited, is_forgeable, is_standard):
        super().__init__(name, rarity, base_atk_min, base_atk_max, second_stat_type, second_stat_min, second_stat_max,
                         passive_name, passive_description,
                         in_shop, in_gacha, in_battlepass, is_limited, is_forgeable, is_standard, level=1,
                         refinement_level=1,
                         ascension=1)


class Polearm(Weapon):
    def __init__(self, name, rarity, base_atk_min, base_atk_max, second_stat_type, second_stat_min, second_stat_max,
                 passive_name, passive_description,
                 in_shop, in_gacha, in_battlepass, is_limited, is_forgeable, is_standard):
        super().__init__(name, rarity, base_atk_min, base_atk_max, second_stat_type, second_stat_min, second_stat_max,
                         passive_name, passive_description,
                         in_shop, in_gacha, in_battlepass, is_limited, is_forgeable, is_standard, level=1,
                         refinement_level=1,
                         ascension=1)


class Bow(Weapon):
    def __init__(self, name, rarity, base_atk_min, base_atk_max, second_stat_type, second_stat_min, second_stat_max,
                 passive_name, passive_description,
                 in_shop, in_gacha, in_battlepass, is_limited, is_forgeable, is_standard):
        super().__init__(name, rarity, base_atk_min, base_atk_max, second_stat_type, second_stat_min, second_stat_max,
                         passive_name, passive_description,
                         in_shop, in_gacha, in_battlepass, is_limited, is_forgeable, is_standard, level=1,
                         refinement_level=1,
                         ascension=1)


class Catalyst(Weapon):
    def __init__(self, name, rarity, base_atk_min, base_atk_max, second_stat_type, second_stat_min, second_stat_max,
                 passive_name, passive_description,
                 in_shop, in_gacha, in_battlepass, is_limited, is_forgeable, is_standard):
        super().__init__(name, rarity, base_atk_min, base_atk_max, second_stat_type, second_stat_min, second_stat_max,
                         passive_name, passive_description,
                         in_shop, in_gacha, in_battlepass, is_limited, is_forgeable, is_standard, level=1,
                         refinement_level=1,
                         ascension=1)
