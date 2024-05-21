# Peter Van Horn
# 05/21/2024
# Factory Design Pattern

from BirdFactory import *
from Pigeon import *

class PigeonFactory(BirdFactory):
   def create_bird(self):
       return Pigeon()