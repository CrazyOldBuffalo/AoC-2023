class Boat():

    def __init__(self, holdin: int) -> None:
        self.speed : int = 0
        self.distance : int = 0
        self.hold : int = holdin


    @property
    def speed(self):
        return self._speed

    @speed.setter
    def speed(self, value):
        self._speed = value

    @property
    def distance(self):
        return self._distance

    @distance.setter
    def distance(self, value):
        self._distance = value

    @property
    def hold(self):
        return self._hold

    @hold.setter
    def hold(self, value):
        self._hold = value
        self._speed = self._hold * 1

    def calculate_distance(self, time: int) -> int:
        self._distance = self._speed * time
        return self._distance
    
