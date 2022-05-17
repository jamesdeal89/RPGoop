# RPG game
from RPGPlayer import Player

class Game():
    def __init__(self) -> None:
        self.player = Player()
        self.running = True

    def playerInput(self):
        self.player.control()

    def play(self):
        while self.running:
            self.playerInput()


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