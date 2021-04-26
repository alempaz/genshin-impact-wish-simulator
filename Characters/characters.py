from Elements import element as e
# ///\\\ FOR FUTURE INFORMATION ABOUT CHARACTERS


class Character:
    def __init__(self, name, rarity, element, gender, nation, description, weapon, in_game, char_type, constellation=0):
        """
        :param name: Name of the character
        :param rarity: Rarity of the character. Either 4 star or 5 star
        :param element: Element control of the character | Pyro, Cryo, Hydro, Anemo, Electro, Geo, Dendro
        :param gender: Is the character Male or Female
        :param description: Description of the character
        :param nation: Nation of the character | Mondstadt, Liyue, Inazuma, Snezhnaya
        :param in_game: Is the character available in-game? | True or False
        :param char_type: Character type. Is it Permanent or Promotional? | perma, promo
        :param constellation: Constellation level of the character. 0 by default
        """
        self.char_type = char_type
        self.in_game = in_game
        self.constellation = constellation
        self.nation = nation
        self.description = description
        self.gender = gender
        self.rarity = rarity
        self.name = name
        self.weapon = weapon
        if element == 'Pyro':
            self.element = e.Pyro(element_name=element)
        elif element == 'Hydro':
            self.element = e.Hydro(element_name=element)
        elif element == 'Cryo':
            self.element = e.Cryo(element_name=element)
        elif element == 'Electro':
            self.element = e.Electro(element_name=element)
        elif element == 'Geo':
            self.element = e.Geo(element_name=element)
        elif element == 'Anemo':
            self.element = e.Anemo(element_name=element)
        elif element == 'Dendro':
            self.element = e.Dendro(element_name=element)
        else:
            raise Exception('Element not exists.')


class SwordUser(Character):
    def __init__(self, name, rarity, element, gender, nation, description, in_game, char_type, weapon):
        super().__init__(name, rarity, element, gender,
                         nation, description, weapon, in_game, char_type, constellation=0)


class ClaymoreUser(Character):
    def __init__(self, name, rarity, element, gender, nation, description, in_game, char_type, weapon):
        super().__init__(name, rarity, element, gender,
                         nation, description, weapon, in_game, char_type, constellation=0)


class PolearmUser(Character):
    def __init__(self, name, rarity, element, gender, nation, description, in_game, char_type, weapon):
        super().__init__(name, rarity, element, gender,
                         nation, description, weapon, in_game, char_type, constellation=0)


class BowUser(Character):
    def __init__(self, name, rarity, element, gender, nation, description, in_game, char_type, weapon):
        super().__init__(name, rarity, element, gender,
                         nation, description, weapon, in_game, char_type, constellation=0)


class CatalystUser(Character):
    def __init__(self, name, rarity, element, gender, nation, description, in_game, char_type, weapon):
        super().__init__(name, rarity, element, gender,
                         nation, description, weapon, in_game, char_type, constellation=0)
