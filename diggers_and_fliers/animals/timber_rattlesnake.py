from behaviors import IMoving

class TimberRattlesnake(IMoving):

    def __init__(self):
        super().__init__()

    def move(self):
        print("The animal slithers")
    
    def __str__(self):
        return "Timber Rattlesnake"