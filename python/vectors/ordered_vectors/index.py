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

    # O(n)
    def search(self, value):
        for i in range(self.last_position + 1):
            if self.values[i] > value:
                return -1
            if self.values[i] == value:
                return i
            if i == self.last_position:
                return -1

    # O(log n)
    def binary_search(self, value):
        lower_limit = 0
        higher_limit = self.last_position

        while True:
            position = int((lower_limit + higher_limit) / 2)

            if self.values[position] == value:
                return position
            elif lower_limit > higher_limit:
                return -1
            else:
                if self.values[position] < value:
                    lower_limit = position + 1
                else:
                    higher_limit = position - 1

    def remove(self, value):
        position = self.search(value)

        if position == -1:
            return -1
        else:
            for i in range(position, self.last_position):
                self.values[i] = self.values[i + 1]

            self.last_position -= 1


vector = OrderedVector(10)

vector.add(6)
vector.add(4)
vector.add(3)
vector.add(5)

vector.remove(4)

vector.print()
