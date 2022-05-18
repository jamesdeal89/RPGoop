# RPG game
import random
from RPGPlayer import Player
from RPGEnemy import Enemy

class Game():
    def __init__(self) -> None:
        self.player = Player()
        self.running = True
        self.moveNum = 0
        self.enemyList = ["Gnobby", "Bobby", "Tubby", "Flubby", "Creep"]

    def spawnEnemy(self):
        self.moveNum = 0
        enemyName = self.enemyList[random.randint(0,len(self.enemyList)-1)]
        # found online that using the following will let you use the value of a variable as the instance name
        locals()[enemyName] = Enemy(name=enemyName)


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