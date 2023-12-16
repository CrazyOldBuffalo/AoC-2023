
class Bag:

    def __init__(self) -> None:
        self.red = 12
        self.green = 13
        self.blue = 14

    @property
    def red(self):
        return self._red
    
    @property
    def green(self):
        return self._green
    
    @property
    def blue(self):
        return self._blue
    
    @blue.setter
    def blue(self, value):
        self._blue = value
    
    @red.setter
    def red(self, value):
        self._red = value

    @green.setter
    def green(self, value):
        self._green = value

    def removegreen(self, value):
        if value > self._green:
            print("Too many removed")
            return False
        else:
            self._green = self._green - value
            print(f"{self._green} remaining")
            return True
        
    def removeblue(self, value):
        if value > self._blue:
            print("Too many removed")
            return False
        else:
            self._blue = self._blue - value
            print(f"{self._green} remaining")
            return True
        
    def removered(self, value):
        if value > self.red:
            print("Too many removed")
            return False
        else:
            self._red = self._red - value
            print(f"{self._red} remaining")
            return True

    def reset(self):
        self._red = 12
        self._blue = 13
        self._green = 14
