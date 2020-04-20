from behaviors import ISwimming

class BettaFish(ISwimming):

    def __init__(self):
        super().__init__()

    def __str__(self):
        return "Betta Fish"