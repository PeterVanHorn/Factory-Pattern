# Peter Van Horn
# 05/21/2024
# Factory Design Pattern

from BirdFactory import *
from Duck import *

class DuckFactory(BirdFactory):
   def create_bird(self):
       return Duck()