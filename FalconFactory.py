# Peter Van Horn
# 05/21/2024
# Factory Design Pattern

from BirdFactory import *
from Falcon import *

class FalconFactory(BirdFactory):
   def create_bird(self):
       return Falcon()