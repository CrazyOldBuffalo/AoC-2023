
class Turn:
    
    def __init__(self, turnid, red, green, blue) -> None:
        self.turnid = turnid
        self.reds = red
        self.greens = green
        self.blues = blue


    @property
    def turnid(self):
        return self._turnid
    
    @property
    def reds(self):
        return self._reds
    
    @property
    def greens(self):
        return self._greens
    
    @property
    def blues(self):
        return self._blues
    
    @turnid.setter
    def turnid(self, value):
        self._turnid = value

    @reds.setter
    def reds(self, value):
        self._reds = value

    @blues.setter
    def blues(self, value):
        self._blues = value

    @greens.setter
    def greens(self, value):
        self._greens = value
    
