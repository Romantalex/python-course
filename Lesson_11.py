import random

class Compare2V:

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        self.dimensions = [x, y, z]

    def __str__(self):
        return f'Building dimensions: {self.dimensions}'

    def building_volume(self):
        return self.x * self.y * self.z

    def __add__(self, other):
        if self.building_volume() + other.building_volume() >= 500000:
            return 'Common volume is too big for this street'
        else:
            return 'These two buildings could be constructed on this street'

    def __eq__(self, other):
        return self.building_volume() == other.building_volume()

    def __gt__(self, other):
        return self.building_volume() > other.building_volume()

    def __lt__(self, other):
        return self.building_volume() < other.building_volume()

if __name__ == '__main__':

    b1 = Compare2V(random.randint(10, 100), random.randint(10, 100), random.randint(10, 100))
    b2 = Compare2V(random.randint(10, 100), random.randint(10, 100), random.randint(10, 100))
    v1 = b1.building_volume()
    v2 = b2.building_volume()

    print(b1, v1)
    print(b2, v2)
    print(b1 == b2)
    print(b1 > b2)
    print(b1 < b2)
    print(b1 + b2)



