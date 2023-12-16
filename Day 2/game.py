from ctypes import Array
from bag import Bag
from turn import Turn

class Game:

    def __init__(self, gameid, turns) -> None:
        self.bags : Bag = Bag()
        self.id = gameid
        self.turn: list[Turn] = turns
        self.isvalid = None

    @property
    def bags(self):
        return self._bags
    
    @property
    def id(self):
        return self._id
    
    @property
    def turn(self):
        return self._turn
    
    @property
    def isvalid(self):
        return self._isvalid
    
    @id.setter
    def id(self, value):
        self._id = value

    @bags.setter
    def bags(self, value):
        self._bags = value

    @turn.setter
    def turn(self, value):
        turnarr = []
        for turn in value:
            turn = Turn(turn, red=value[turn]['red'], green=value[turn]['green'], blue=value[turn]['blue'])
            turnarr.append(turn)

        self._turn = turnarr

    @isvalid.setter
    def isvalid(self, value):
        self._isvalid = value


    def runGame(self):
        for currturn in self.turn:
            if not self.bags.removered(currturn.reds):
                self._isvalid = False
                return
            if not self.bags.removegreen(currturn.greens):
                self._isvalid = False
                return
            if not self.bags.removeblue(currturn.blues):
                self._isvalid = False
                return
            else:
                self._isvalid = True
            self.bags.reset()


