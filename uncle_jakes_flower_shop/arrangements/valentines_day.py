from arrangements import Arrangement
from attributes import INotOrganic

class ValentinesDay(Arrangement):

    def __init__(self):
        super().__init__()
        self.stem_length = 7

    def enhance(self, flower):
        try:
            if flower.is_refrigerated == True:
                self._Arrangement__flowers.append(flower)
                print(f"A {flower} was added to this Valentine's Day arrangement.")
            else:
                print(f"A {flower} cannot be added to a Valentine's Day arrangement.")
        except AttributeError:
            return 0

    def __str__(self):
        if len(self._Arrangement__flowers) == 0:
            return "This Valentine's day arrangement doesn't have any flowers yet."
        else:
            flowerList = []
            for flower in self._Arrangement__flowers:
                flowerString = str(flower)
                flowerList.append(flowerString)
                joinFlowerList = ", ".join(flowerList)
            return(f"This Valentine's day arrangement has the following flowers: {joinFlowerList}")