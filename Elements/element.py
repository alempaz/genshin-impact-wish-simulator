# File made for future content

class Element:
    def __init__(self, element_name, swirl=False, crystallise=False, overload=False, superconduct=False,
                 electro_charge=False, melt=False, vaporize=False, freeze=False, burning=False):
        self.element_name = element_name
        self.swirl = swirl
        self.crystallise = crystallise
        self.overload = overload
        self.superconduct = superconduct
        self.electro_charge = electro_charge
        self.melt = melt
        self.vaporize = vaporize
        self.freeze = freeze
        self.burning = burning


class Pyro(Element):
    def __init__(self, element_name):
        super().__init__(element_name, swirl=False, crystallise=False, overload=False, superconduct=False,
                         electro_charge=False, melt=False, vaporize=False, freeze=False, burning=False)
        self.melt = True
        self.vaporize = True
        self.overload = True
        self.swirl = True
        self.crystallise = True


class Hydro(Element):
    def __init__(self, element_name):
        super().__init__(element_name, swirl=False, crystallise=False, overload=False, superconduct=False,
                         electro_charge=False, melt=False, vaporize=False, freeze=False, burning=False)
        self.electro_charge = True
        self.vaporize = True
        self.freeze = True
        self.swirl = True
        self.crystallise = True


class Cryo(Element):
    def __init__(self, element_name):
        super().__init__(element_name, swirl=False, crystallise=False, overload=False, superconduct=False,
                         electro_charge=False, melt=False, vaporize=False, freeze=False, burning=False)
        self.melt = True
        self.superconduct = True
        self.freeze = True
        self.swirl = True
        self.crystallise = True


class Electro(Element):
    def __init__(self, element_name):
        super().__init__(element_name, swirl=False, crystallise=False, overload=False, superconduct=False,
                         electro_charge=False, melt=False, vaporize=False, freeze=False, burning=False)
        self.electro_charge = True
        self.superconduct = True
        self.overload = True
        self.swirl = True
        self.crystallise = True


class Geo(Element):
    def __init__(self, element_name):
        super().__init__(element_name, swirl=False, crystallise=False, overload=False, superconduct=False,
                         electro_charge=False, melt=False, vaporize=False, freeze=False, burning=False)
        self.crystallise = True


class Anemo(Element):
    def __init__(self, element_name):
        super().__init__(element_name, swirl=False, crystallise=False, overload=False, superconduct=False,
                         electro_charge=False, melt=False, vaporize=False, freeze=False, burning=False)
        self.swirl = True


class Dendro(Element):
    def __init__(self, element_name):
        super().__init__(element_name, swirl=False, crystallise=False, overload=False, superconduct=False,
                         electro_charge=False, melt=False, vaporize=False, freeze=False, burning=False)
        self.swirl = True
        self.crystallise = True
        self.burning = True


# For the Traveler
# class Adaptive(Element):
#     def __init__(self, element_name):
#         super().__init__(element_name, swirl=True, crystallise=True, overload=True, superconduct=True,
#                          electro_charge=True, melt=True, vaporize=True, freeze=True, burning=True)
