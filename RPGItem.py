"""the class for Items"""
class Item():
    """the class of items which has the attributes and default values of:
    uses: 10
    value: 50
    rarity: "common"
    """
    def __init__(self, uses=10, value=50, rarity="common"):
        self.uses = uses
        self.value = value
        self.rarity = rarity
