from behaviors import IMoving

class Mouse(IMoving):

    def __init__(self):
        super().__init__()

    def __str__(self):
        return "Mouse"