class Alchemist:
    def __init__(self):
        self.attack = 0
        self.strength = 0
        self.defense = 0
        self.magic = 0
        self.ranged = 0
        self.necromancy = 0
        self.laboratory = Laboratory
        self.recipes = {
            'Super Attack': ('Irit', 'Eye of Newt'),
            'Super Strength': ('Kwuarm', 'Limpwurt Root'),
            'Super Defence': ('Cadantine', 'White Berries'),
            'Super Magic': ('Lantadyme', 'Potato Cactus'),
            'Super Ranging': ('Dwarf Weed', 'Wine of Zamorak'),
            'Super Necromancy': ('Arbuck', 'Blood of Orcus'),
            'Extreme Attack': ('Avantoe', 'Super Attack'),
            'Extreme Strength': ('Dwarf Weed', 'Super Strength'),
            'Extreme Defence': ('Lantadyme', 'Super Defence'),
            'Extreme Magic': ('Ground Mud Rune', 'Super Magic'),
            'Extreme Ranging': ('Grenwall Spike', 'Super Ranging'),
            'Extreme Necromancy': ('Ground Miasma Rune', 'Super Necromancy'),
        }
    

class Laboratory:
    pass
