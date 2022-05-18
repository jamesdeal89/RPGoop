"""the class for levels"""
from RPGRoom import Room

class Level():
    def __init__(self) -> None:
        self.roomList = []

    def addRoom(self, instanceName):
        if isinstance(instanceName, Room):
            self.roomList.append(self.roomList)
        else:
            raise TypeError
