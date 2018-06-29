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


# class Melon(object):
#     """A melon in a melon harvest."""



# def make_melons(melon_types):
#     """Returns a list of Melon objects."""



# def get_sellability_report(melons):
#     """Given a list of melon object, prints whether each one is sellable."""
