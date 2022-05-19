"""the class for rooms"""
from typing import Union, List
from RPGEnemy import Enemy
from RPGItem import Item

class Room():
    """rooms will contain list of enemy objects and list of item objects"""
    def __init__(self) -> None:
        self.enemyList: List[Enemy] = []
        self.itemList: List[Item] = []

    def addToRoom(self, instance: Union[Enemy, Item]) -> None:
        if isinstance(instance, Enemy):
            self.enemyList.append(instance)
        elif isinstance(instance, Item):
            self.itemList.append(instance)
        else:
            raise TypeError