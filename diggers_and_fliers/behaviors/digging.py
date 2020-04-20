class IDigging:

    def __init__(self):
        self.depth = 0
        self.distance = 0
        self.does_dig = True

    def dig(self):
        print("The animal digs")