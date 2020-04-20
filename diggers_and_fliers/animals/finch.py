from behaviors import IFlying, IMoving

class Finch(IFlying, IMoving):

    def __init__(self):
        IFlying.__init__(self)
        IMoving.__init__(self)

    def __str__(self):
        return "Finch"