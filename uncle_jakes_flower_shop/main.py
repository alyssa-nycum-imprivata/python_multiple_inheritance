from arrangements import MothersDay, ValentinesDay
from flowers import Alstroemeria, BabysBreath, Daisy, Lily, Poppy, Rose

valentines_day_arrangement = ValentinesDay()
mothers_day_arrangement = MothersDay()

pink_rose = Rose("pink")
red_rose = Rose("red")
blue_rose = Rose("blue")
poppy = Poppy()
lily = Lily()
daisy = Daisy()
babys_breath = BabysBreath()
alstroemeria = Alstroemeria()

mothers_day_arrangement.enhance(daisy)
mothers_day_arrangement.enhance(babys_breath)
mothers_day_arrangement.enhance(poppy)
# mothers_day_arrangement.enhance(pink_rose)

valentines_day_arrangement.enhance(pink_rose)
valentines_day_arrangement.enhance(red_rose)
valentines_day_arrangement.enhance(blue_rose)
valentines_day_arrangement.enhance(lily)
valentines_day_arrangement.enhance(alstroemeria)
# valentines_day_arrangement.enhance(poppy)


print(mothers_day_arrangement)
print(valentines_day_arrangement)