# Peter Van Horn
# 05/21/2024
# Factory Design Pattern

from Bird import *

class Pigeon(Bird):
    def fly(self):
        return "Pigeon flies!!"
    
    def talk(self):
        return "Pigeon talks!!"

    def carry_a_message(self):
        return "Pigeon carries a message!!"