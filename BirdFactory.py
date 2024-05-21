# Peter Van Horn
# 05/21/2024
# Factory Design Pattern

from abc import ABC, abstractmethod
from Bird import *

class BirdFactory(ABC):
    @abstractmethod
    def create_bird(self):
        pass