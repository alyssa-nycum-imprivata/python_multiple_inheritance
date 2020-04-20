from behaviors import IDigging, IMoving

class Ant(IDigging, IMoving):

    def __init__(self):
        IDigging.__init__(self)
        IMoving.__init__(self)
    
    def __str__(self):
        return "Ant"