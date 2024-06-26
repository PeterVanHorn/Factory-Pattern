# Peter Van Horn
# 05/21/2024
# Factory Design Pattern

from abc import ABC, abstractmethod

class Bird(ABC):
    @abstractmethod
    def fly(self):
        pass

    def talk(self):
        pass