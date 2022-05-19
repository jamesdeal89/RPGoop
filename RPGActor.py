"""the actor class"""
class Actor():
    """
    This is the RPG actor which is the parent class for players and enemies.
    Atrributes: name, health, armour, speed, status.
    """
    def __init__(self, name = "bob", health = 100, armour=0, speed=1, x=0, y=0):
        self.name = name
        self.health = health
        self.armour = armour
        self.speed = speed
        self.status = []
        self.x = x
        self.y = y

    def __repr__(self) -> str:
        return("Actor: " + self.name)

if __name__ == "__main__":
    test = Actor()
    print(test)