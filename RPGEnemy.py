"""the class for enemies"""
from RPGActor import Actor

class Enemy(Actor):
    def __init__(self, name="bob", health=50, armour=0, speed=1, positionx=0, positiony=0):
        super().__init__(name, health, armour, speed, positionx, positiony)
        print("Enemy has spawned...")
        print("Slippity sloop my name is " + self.name + ". Be afraid!")
    
    def pathFind(self):
        # uses a 2D plane as the world
        # finds and moves to player by 
        # increasing a set number of 'pixels' in the players direction
        # in the x and y axis
        pass