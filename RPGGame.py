# RPG game
import random
from RPGPlayer import Player
from RPGEnemy import Enemy
from RPGWorld import World
from RPGLevel import Level
from RPGRoom import Room

class Game():
    def __init__(self) -> None:
        self.player = Player()
        self.running = True
        self.moveNum = 0
        self.enemyList = ["Gnobby", "Bobby", "Tubby", "Flubby", "Creepy"]

    def spawnEnemy(self):
        self.moveNum = 0
        enemyName = self.enemyList[random.randint(0,len(self.enemyList)-1)]
        # found online that using the following will let you use the value of
        # a variable as the instance name
        locals()[enemyName] = Enemy(name=enemyName)
        room.addToRoom(locals()[enemyName])
        print(room.enemyList)

    def playerInput(self):
        self.player.control()

    def play(self):
        while self.running:
            self.playerInput()
            self.moveNum += 1
            if self.moveNum > random.randint(3,8):
                self.spawnEnemy()


if __name__ == "__main__":
    game = Game()
    world = World()
    level = Level()
    room = Room()
    world.addLevel(level)
    level.addRoom(room)
    print("generating the world...")
    game.play()
    # initialize game world
    # consisting of levels
    # consiting of rooms

    # each room can contain enemies
    # there is one player

    # player can have weapons or items
    # the player will need to move and attack
    # enemies will be able to move and attack
    pass