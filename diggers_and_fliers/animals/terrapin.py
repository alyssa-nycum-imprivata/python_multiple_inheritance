from behaviors import ISwimming, IDigging, IMoving

class Terrapin(ISwimming, IDigging, IMoving):

    def __init__(self):
        ISwimming.__init__(self)
        IDigging.__init__(self)
        IMoving.__init__(self)

    def __str__(self):
        return "Terrapin"