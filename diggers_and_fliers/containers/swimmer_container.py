from behaviors import ISwimming

class SwimmerContainer(ISwimming):

    def __init__(self):
        self.animals = []

    def add_animal(self, animal):
        try:
            if animal.does_swim == True:
                self.animals.append(animal)
                print(f"A(n) {animal} has been added to the swimmer's container")

            else:
                print(f"A(n) {animal} cannot be put in this container because it does not swim.")
        except AttributeError:
            return 0

    def __str__(self):
        if len(self.animals) == 0:
            return "The swimmer's container doesn't have any animals in it yet."
        else: 
            animalList = []
            for animal in self.animals:
                animalString = str(animal)
                animalList.append(animalString)
                joinAnimalList = ", ".join(animalList)
            return(f"The swimmer's container has the following animals in it: {joinAnimalList}")