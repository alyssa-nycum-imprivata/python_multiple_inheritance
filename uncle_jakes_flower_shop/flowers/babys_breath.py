from attributes import IOrganic
from .flower import Flower

class BabysBreath(IOrganic, Flower):

    def __init__(self):
        IOrganic.__init__(self)
        Flower.__init__(self)
        self.flower_type = "baby's breath"

    def __str__(self):
        return self.flower_type