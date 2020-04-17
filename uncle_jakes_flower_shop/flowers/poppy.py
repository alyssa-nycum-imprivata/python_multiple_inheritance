from attributes import IOrganic
from .flower import Flower

class Poppy(IOrganic, Flower):

    def __init__(self):
        IOrganic.__init__(self)
        Flower.__init__(self)

    def __str__(self):
        return "poppy"