from boat import Boat

class Race(object):

    def __init__(self, record_distance: int, duration: int) -> None:
        self.record_distance = record_distance
        self.duration = duration
        self.boat : Boat = Boat(0)
        self.winning_races = 0


    @property
    def record_distance(self) -> int:
        return self._record_distance

    @property
    def duration(self) -> int:
        return self._duration

    @property
    def boat(self) -> Boat:
        return self._boat

    @property
    def winning_races(self) -> int:
        return self._winning_races

    @boat.setter
    def boat(self, value) -> None:
        if isinstance(value, Boat):
            self._boat = value
        else:
            print("Not valid")
            return

    @record_distance.setter
    def record_distance(self, value) -> None:
        self._record_distance = value

    @duration.setter
    def duration(self, value) -> None:
        self._duration = value

    @winning_races.setter
    def winning_races(self, value) -> None:
        self._winning_races = value

    def calculate_races(self):
        for millisecond in range(0, self._duration + 1):
            self.boat.hold = millisecond
            current_distance = self.boat.calculate_distance(self._duration - millisecond)
            if current_distance > self._record_distance:
                self._winning_races += 1        
        return self._winning_races
    
        
        

