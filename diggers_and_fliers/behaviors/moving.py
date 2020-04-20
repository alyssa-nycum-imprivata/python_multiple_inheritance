class IMoving:

    def __init__(self):
        self.speed = 0
        self.num_of_legs = 0
        self.distance = 0 
        self.does_move = True

    def move(self):
        print("The animal walks")