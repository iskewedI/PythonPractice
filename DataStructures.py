from sys import getsizeof
from array import array
from collections import deque
data = [
    ("Product 1", 1),
    ("Product 2", 2),
    ("Product 3", 3)
]

# Tuples
(1, 10)

# Mapping
prices = list(map(lambda item: item[1], data))
# Or
prices = [item[1] for item in data]

# Filtering
filtered = list(filter(lambda item: item[1] >= 2, data))
# Or
filtered = [item for item in data if item[1] >= 2]

# Combining lists into tuples
list1 = [1, 2, 3]
list2 = [10, 20, 30]

combined = list(zip(list1, list2))  # [(1, 10), (2, 20), (3, 30)]

# Stacks -> Last-In/First-Out
stack = [1, 2, 3]
if not stack:
    print("empty stack")
else:
    print("fulfilled stack")

# Queue -> First In - First Out

queue = deque([])

queue.append(1)
queue.append(2)

queue.popleft()  # Removes FIRST

# Array

array = array("i", [1, 2, 3])
array.reverse()  # Doesn't return the reversed, it reverses the array directly

# Sets -> Unique values - Are objects
uniques = set([1, 2, 3, 4, 4, 5])
uniques.add(5)

# Combining UNIQUE sets
secondUniques = {1, 5, 7}

# Returns new set with all the values that exists in each set
print(uniques | secondUniques)
# Returns new set with only the values that exists in both sets
print(uniques & secondUniques)
# Returns new set with the values that exists in the left set but not in the right set
print(uniques - secondUniques)
# Returns the values that are either on the left o right set but NOT IN BOTH
print(uniques ^ secondUniques)  # Alt + 94 -> ^

# Dictionaries
dictionary = dict(x=1, y=2)

defaultOrValue = dictionary.get("z", 0)

# Removing items
del dictionary["y"]

# Storing a lot of generated values but NOT IN MEMORY | The SIZE in memory remains constant
values = (x * 2 for x in range(10))

for value in values:
    print(value)

print(getsizeof(values))

# Unpacking
aList = [1, 2, 3]
print(*aList)
