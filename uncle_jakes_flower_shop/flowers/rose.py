from attributes import INotOrganic
from .flower import Flower

class Rose(INotOrganic, Flower):

    def __init__(self, color):
        INotOrganic.__init__(self)
        Flower.__init__(self)
        self.color = color

    def __str__(self):
        return f"{self.color} rose"