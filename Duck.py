# Peter Van Horn
# 05/21/2024
# Factory Design Pattern

from Bird import *

class Duck(Bird):
    def fly(self):
        return "Duck flies!!"
    
    def talk(self):
        return "Duck talks!!"
    
    def swim(self):
        return "Duck swims!!"