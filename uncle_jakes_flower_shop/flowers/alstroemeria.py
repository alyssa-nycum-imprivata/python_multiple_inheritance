from attributes import INotOrganic
from .flower import Flower

class Alstroemeria(INotOrganic, Flower):

    def __init__(self):
        INotOrganic.__init__(self)
        Flower.__init__(self)

    def __str__(self):
        return "alstroemeria"

    

    