############
# Part 1   #
############


class MelonType(object):
    """A species of melon at a melon farm."""

    def __init__(self, code, first_harvest, color, is_seedless, is_bestseller,
                 name):
        """Initialize a melon."""

        self.pairings = []
        self.code = code
        self.first_harvest = first_harvest
        self.color = color
        self.is_seedless = is_seedless
        self.is_bestseller = is_bestseller
        self.name = name

    def add_pairing(self, pairing):
        """Add a food pairing to the instance's pairings list."""

        self.pairings.append(pairing)

    def update_code(self, new_code):
        """Replace the reporting code with the new_code."""

        self.code = new_code


def make_melon_types():
    """Returns a list of current melon types."""

    all_melon_types = []

    musk = MelonType('musk', '1998', 'green', True, True, 'Muskmelon')
    casaba = MelonType('cas', '2003', 'orange', False, False, 'Casaba')
    crenshaw = MelonType('cren', '1996', 'green', False, False, 'Crenshaw')
    yellow = MelonType('yw', '2013', 'yellow', False, True, 'Yellow Watermelon')

    musk.add_pairing('mint')
    casaba.add_pairing('strawberries')
    casaba.add_pairing('mint')
    crenshaw.add_pairing('proscuitto')
    yellow.add_pairing('ice cream')

    all_melon_types.extend((musk, casaba, crenshaw, yellow))

    return all_melon_types


def print_pairing_info(melon_types):
    """Prints information about each melon type's pairings."""

    for melons in melon_types:
        print("\n {} pairs with".format(melons.name))
        for each in melons.pairings:
            print("- {}".format(each))


def make_melon_type_lookup(melon_types):
    """Takes a list of MelonTypes and returns a dictionary of melon type by code."""

    codes = {}
    for melons in melon_types:
        codes[melons.code] = melons
    return codes

############
# Part 2   #
############


class Melon(object):
    """A melon in a melon harvest."""
    def __init__(self, code, shape, color, field, harvester):
        """Initialize a melon."""
        self.code = code
        self.shape = shape
        self.color = color
        self.field = field
        self.harvester = harvester

    def is_sellable(self):
        if self.shape > 5 and self.color > 5 and self.field != 3:
            return True


def make_melons(melon_types):
    """Returns a list of Melon objects."""

    all_melons = []

    melon_codes = make_melon_type_lookup(melon_types)

    melon1 = Melon(melon_codes['yw'], 8, 7, 2, 'Sheila')
    melon2 = Melon(melon_codes['yw'], 3, 4, 2, 'Sheila')
    melon3 = Melon(melon_codes['yw'], 9, 8, 3, 'Sheila')
    melon4 = Melon(melon_codes['cas'], 10, 6, 35, 'Sheila')
    melon5 = Melon(melon_codes['cren'], 8, 9, 35, 'Michael')
    melon6 = Melon(melon_codes['cren'], 8, 2, 35, 'Michael')
    melon7 = Melon(melon_codes['cren'], 2, 3, 4, 'Michael')
    melon8 = Melon(melon_codes['musk'], 6, 7, 4, 'Michael')
    melon9 = Melon(melon_codes['yw'], 7, 10, 3, 'Sheila')

    all_melons.extend((melon1, melon2, melon3, melon4, melon5, melon6,
                       melon7, melon8, melon9))

    print(melon1.code.name)
    return all_melons


def get_sellability_report(melons):
    """Given a list of melon object, prints whether each one is sellable."""

    for melon in melons:
            if melon.is_sellable():
                print("Harvested by {} from Field # {} CAN BE SOLD".format(melon.harvester, melon.field))
            else:
                print("Harvested by {} from Field # {} NOT SELLABLE".format(melon.harvester, melon.field))


melon_types = make_melon_types()

melons = make_melons(melon_types)

get_sellability_report(melons)
