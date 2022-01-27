import numpy as np


class UnorderedVector:
    def __init__(self, capacity):
        self.capacity = capacity
        self.last_position = -1
        self.values = np.empty(self.capacity, dtype=int)

    # O(n)
    def print_vector(self):
        if self.last_position == -1:
            print("The vector is empty")
        else:
            for i in range(self.last_position + 1):
                print(i, "-", self.values[i])

    # O(1)
    def insert(self, value):
        if self.last_position == self.capacity - 1:
            print("limit capacity hit")
        else:
            self.last_position += 1
            self.values[self.last_position] = value

    # O(n)
    def linear_search(self, value):
        for i in range(self.last_position + 1):
            if value == self.values[i]:
                return i

        return -1

    # O(n)
    def remove(self, value):
        index = self.linear_search(value)
        if index != -1:
            for i in range(index, self.last_position):
                self.values[i] = self.values[i + 1]

            self.last_position -= 1

        return -1


vector = UnorderedVector(5)

vector.insert(3)
vector.insert(5)
vector.insert(8)
vector.insert(1)
vector.insert(7)

vector.print_vector()
print("item index", vector.linear_search(5))
print("item index", vector.linear_search(15))

vector.remove(7)
vector.print_vector()
