from animals import Ant, BettaFish, CopperheadSnake, Earthworm, Finch, Gerbil, Mouse, Parakeet, Terrapin, TimberRattlesnake
from behaviors import IDigging, IFlying, IMoving, ISwimming
from containers import DiggerContainer, FlierContainer, MoverContainer, SwimmerContainer

digger_container = DiggerContainer()
flier_container = FlierContainer()
mover_container = MoverContainer()
swimmer_container = SwimmerContainer()

ant = Ant()
betta_fish = BettaFish()
copperhead_snake = CopperheadSnake()
earthworm = Earthworm()
finch = Finch()
gerbil = Gerbil()
mouse = Mouse()
parakeet = Parakeet()
terrapin = Terrapin()
timber_rattlesnake = TimberRattlesnake()

digger_container.add_animal(ant)
digger_container.add_animal(earthworm)
print(digger_container)

flier_container.add_animal(finch)
flier_container.add_animal(parakeet)
print(flier_container)

mover_container.add_animal(copperhead_snake)
mover_container.add_animal(gerbil)
mover_container.add_animal(mouse)
mover_container.add_animal(timber_rattlesnake)
print(mover_container)

swimmer_container.add_animal(betta_fish)
swimmer_container.add_animal(terrapin)
print(swimmer_container)