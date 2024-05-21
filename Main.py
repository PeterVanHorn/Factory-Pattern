# Peter Van Horn
# 05/21/2024
# Factory Design Pattern

from FalconFactory import *
from PigeonFactory import *
from DuckFactory import *

print("Hello, World!")

faFactory = FalconFactory()
piFactory = PigeonFactory()
duFactory = DuckFactory()

falcon = faFactory.create_bird()
pigeon = piFactory.create_bird()
duck = duFactory.create_bird()

print(falcon.fly())
print(falcon.talk())
print(falcon.hunt())

print("")

print(pigeon.fly())
print(pigeon.talk())
print(pigeon.carry_a_message())

print("")

print(duck.fly())
print(duck.talk())
print(duck.swim())