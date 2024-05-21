# Peter Van Horn
# 05/21/2024
# Factory Design Pattern

from Bird import *

class Falcon(Bird):
    def fly(self):
        return "Falcon flies!!"
    
    def talk(self):
        return "Falcon talks!!"

    def hunt(self):
        return "Falcon hunts!!"