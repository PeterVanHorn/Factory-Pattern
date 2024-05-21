from Bird import *
from Falcon import *
from Pigeon import *
from Duck import *
p = Pigeon()
f = Falcon()
d = Duck()

# print (p.__class__)
# classes = p.__class__
# print(classes.__name__)
firstMessage = "Hello, World!"
print(firstMessage)

f.fly()
f.talk()
f.hunt()

p.fly()
p.talk()
p.carry_a_message()

d.fly()
d.talk()
d.swim()
