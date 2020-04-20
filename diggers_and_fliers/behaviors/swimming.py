class ISwimming:

    def __init__(self):
        self.speed = 0
        self.distance = 0
        self.max_depth = 0
        self.does_swim = True

    def swim(self):
        print("The animal swims")