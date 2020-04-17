from arrangements import Arrangement
from attributes import IOrganic

class MothersDay(Arrangement):

    def __init__(self):
        Arrangement.__init__(self)
        self.stem_length = 4

    def enhance(self, flower):
        try:
            if flower.is_refrigerated == False:
                self._Arrangement__flowers.append(flower)
                print(f"A {flower} was added to this Mother's Day Arrangement.")
            else:
                print(f"A {flower} cannot be added to a Mother's Day arrangement.")
        except AttributeError:
            return 0

    def __str__(self):
        if len(self._Arrangement__flowers) == 0:
            return "This Mother's day arrangement doesn't have any flowers yet."
        else:
            flowerList = []
            for flower in self._Arrangement__flowers:
                flowerString = str(flower)
                flowerList.append(flowerString)
                joinFlowerList = ", ".join(flowerList)
            return(f"This Mother's day arrangement has the following flowers: {joinFlowerList}")