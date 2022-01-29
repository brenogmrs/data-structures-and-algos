import numpy as np


class OrderedVector:
    def __init__(self, capacity):
        self.capacity = capacity
        self.last_position = -1
        self.values = np.empty(self.capacity, dtype=int)

    # O(n)
    def print(self):
        if self.last_position == -1:
            print("The vector is empty")
        else:
            print("-----")
            for i in range(self.last_position + 1):
                print(i, "-", self.values[i])
            print("-----")

    # O(n)
    def add(self, value):
        if self.last_position == self.capacity - 1:
            print("limit capacity hit")
            return

        position = 0
        for i in range(self.last_position + 1):
            position = i
            if self.values[i] > value:
                break
            if i == self.last_position:
                position = i + 1

        x = self.last_position
        while x >= position:
            self.values[x + 1] = self.values[x]
            x -= 1

        self.values[position] = value
        self.last_position += 1


vector = OrderedVector(10)

vector.add(6)
vector.add(4)
vector.add(3)
vector.add(5)
vector.add(2)
vector.add(4)
vector.add(2)
vector.add(4)
vector.add(5)

vector.print()
