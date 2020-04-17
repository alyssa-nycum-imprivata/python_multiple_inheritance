from attributes import INotOrganic
from .flower import Flower

class Lily(INotOrganic, Flower):

    def __init__(self):
        INotOrganic.__init__(self)
        Flower.__init__(self)

    def __str__(self):
        return "lily"