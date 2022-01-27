import numpy as np


class UnorderedVector:
    def __init__(self, capability):
        self.capability = capability
        self.last_position = -1
        self.values = np.empty(self.capability, dtype=int)

    def print_vector(self):
        if self.last_position == -1:
            print("The vector is empty")
        else:
            for i in range(self.last_position + 1):
                print(i, "-", self.values[i])


vector = UnorderedVector(5)

vector.print_vector()
