"""the class for potions"""
from RPGItem import Item

class Potion(Item):
    def __init__(self, uses=1, value=100, rarity="uncommon"):
        super().__init__(uses, value, rarity)
