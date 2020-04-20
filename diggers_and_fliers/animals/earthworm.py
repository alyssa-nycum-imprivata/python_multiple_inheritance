from behaviors import IMoving, IDigging

class Earthworm(IMoving, IDigging):

    def __init__(self):
        IMoving.__init__(self)
        IDigging.__init__(self)

    def move(self):
        print("The animal inches along")

    def __str__(self):
        return "Earthworm"