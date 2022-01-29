import numpy as np


class OrderedVector:
    def __init__(self, capacity):
        self.capacity = capacity
        self.last_position = -1
        self.values = np.empty(self.capacity, dtype=int)

    # O(n)
    def print_vector(self):
        if self.last_position == -1:
            print("The vector is empty")
        else:
            vector = []
            for i in range(self.last_position + 1):
                vector.append(self.values[i])
            print(vector)
