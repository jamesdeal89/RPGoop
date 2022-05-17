"""the class for enemies"""
from RPGActor import Actor

class Enemy(Actor):
    def __init__(self):
        super.__init__()
        self.health = 50
    
    def pathFind(self):
        # uses a 2D plane as the world
        # finds and moves to player by 
        # increasing a set number of 'pixels' in the players direction
        # in the x and y axis
        pass