"""the class for the world"""
from RPGLevel import Level

class World():
    def __init__(self) -> None:
        self.levelList = []

    def addLevel(self, instanceName):
        if isinstance(instanceName, Level):
            self.levelList.append(instanceName)
        else:
            raise TypeError