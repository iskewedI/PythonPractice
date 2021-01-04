class Point:
    default_color = "blue"
    # Constructor || Magic method

    def __init__(self, x, y):
        self.x = x
        self.y = y
        # Private tags
        self.__tags = {}

    # Used when converting to string
    def __str__(self):
        return f"({self.x}, {self.y})"

    # Used when matching two instances
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    # Used when comparing greaters and lessers
    def __gt__(self, other):
        return self.x > other.x and self.y > other.y

    # For arithmetic
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    # Getter
    def __getitem__(self, tag):
        return self.__tags.get(tag.lower(), 0)

    # Setter
    def __setitem__(self, tag, count):
        self.__tags[tag.lower()] = count

    # Iterators - To use in loops
    def __iter__(self):
        return iter(self.__tags)

    # Instance method
    def draw(self):
        print(f"Point ({self.x}, {self.y})")

    # Class method
    @classmethod
    def zero(cls):
        cls(0, 0)


Point.default_color = "red"  # Affects ALL instances of this class

instanceClass = Point(1, 2)
instanceClass.draw()
print(instanceClass)  # Converted to STRING, uses the __str__ method

instanceClass["a"] = 2
print(instanceClass["a"])

# Access private members - Located in instance.__dict__
print(instanceClass._Point__tags)
