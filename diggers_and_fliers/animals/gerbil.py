from behaviors import IMoving, IDigging

class Gerbil(IMoving, IDigging):

    def __init__(self):
        IMoving.__init__(self)
        IDigging.__init__(self)

    def __str__(self):
        return "Gerbil"