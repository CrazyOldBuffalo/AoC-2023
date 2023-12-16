from game import Game
import re

def main():
    with open(file="input.txt") as file:
        for line in file:
            gameid = re.findall(pattern=r'Game \d+ :', string=line)
            print(gameid)
    test = {1: {'red': 11, 'blue': 11, 'green': 11}, 2: {'red': 11, 'blue': 15, 'green': 12}}
    print(test[1]['red'])
    game = Game(2, test)
    game.runGame()
    if game.isvalid:
        print("game is valid")
    else:
        print("game is invalid")


main()