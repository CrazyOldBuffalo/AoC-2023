from ctypes import Array


class WinningCards:

    def __init__(self, cardid, numbers) -> None:
        self.cardid = cardid
        self.numbers : Array[int] = numbers

