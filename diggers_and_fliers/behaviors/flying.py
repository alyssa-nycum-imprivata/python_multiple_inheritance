class IFlying:

    def __init__(self):
        self.speed = 0
        self.max_height = 0
        self.does_fly = True

    def fly(self):
        print("The animal flies")