class AClass:
    default_color = "blue"
    # Constructor || Magic method

    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Used when converting to string
    def __str__(self):
        return f"({self.x}, {self.y})"

    # Used when matching two instances
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    # Used when comparing greaters and lessers
    def __gt__(self, other):
        return self.x > other.x and self.y > other.y

    # Instance method
    def draw(self):
        print(f"Point ({self.x}, {self.y})")

    # Class method
    @classmethod
    def zero(cls):
        cls(0, 0)


AClass.default_color = "red"  # Affects ALL instances of this class

instanceClass = AClass(1, 2)
instanceClass.draw()
print(instanceClass)  # Converted to STRING, uses the __str__ method
