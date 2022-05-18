"""the class for rooms"""
from RPGEnemy import Enemy
from RPGItem import Item

class Room():
    """rooms will contain list of enemy objects and list of item objects"""
    def __init__(self) -> None:
        self.enemyList = []
        self.itemList = []

    def addToRoom(self, instanceName):
        if isinstance(instanceName, Enemy):
            self.enemyList.append(instanceName)
        elif isinstance(instanceName, Item):
            self.itemList.append(instanceName)
        else:
            raise TypeError