import random

self = {
    'Name' : "Bruce",
    'Phone' : '07823641610',
    'Address' : 'Swan street'
    }

self = list(self.items())
random.shuffle(self)

for xa, ya in self:
    print (self)
#     print (ya)

