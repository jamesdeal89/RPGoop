"""the class for weapons"""
from RPGItem import Item

class Weapon(Item):
    def __init__(self, uses=10, value=500, rarity="rare"):
        super().__init__(uses, value, rarity)

