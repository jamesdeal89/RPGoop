"""the player class"""
from RPGActor import Actor

class Player(Actor):
    """
    The player class which inherits from the Actor class.
    """
    def __init__(self):
        super().__init__()
        self.keymap = {
            "w":"up",
            "a":"left",
            "s":"down",
            "d":"right",
            " ":"attack"}
        self._inventory = []
    
    def pickUp(self, item):
        """accessor to add an item to inventory"""
        self._inventory.append(item)

    def drop(self, item):
        """accessor to remove an item from the inventory"""
        self._inventory.remove(item)

    def check(self):
        print("in ", self.name, " inventory is:")
        for item in self._inventory:
            print(item, end=", ")

    def control(self):
        command = input("what is your move?:")
        if command in self.keymap:
            if self.keymap[command] == "up":
                print("moving up")
            if self.keymap[command] == "down":
                print("moving down")
            if self.keymap[command] == "left":
                print("moving left")
            if self.keymap[command] == "right":
                print("moving right")
            if self.keymap[command] == "attack":
                print("attacking")
        if command == "quit":
            print("there is no escape")
        if "pickup" in command:
            self.pickUp(command.replace("pickup ",""))
        if "drop" in command:
            self.drop(command.replace("drop",""))
        if command == "check":
            self.check()

