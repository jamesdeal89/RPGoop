"""the actor class"""
class Actor():
    """
    This is the RPG actor which is the parent class for players and enemies.
    Atrributes: name, health, armour, speed, status.
    """
    def __init__(self):
        self.name = "Bob"
        self.health = 100
        self.armour = 0
        self.speed = 1
        self.status = []
        self.positionx = 0
        self.positiony = 0

    def __repr__(self) -> str:
        return("Actor: " + self.name)

if __name__ == "__main__":
    test = Actor()
    print(test)