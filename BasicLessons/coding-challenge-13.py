# Using the concept of operator overloading, change the behavior of the multiplication operator in a way that
# multiplication operator behaves like an addition operator

class OpOverload:

    def __init__(self, height):
        self.height = height

    def __mul__(self, other):
        height = self.height + other.height
        return height


max = OpOverload(195)
kim = OpOverload(150)

print(max * kim)