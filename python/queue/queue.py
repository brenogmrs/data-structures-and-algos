import numpy as np

class Queue:

    def __init__(self, capacity):
        self.capacity = capacity
        self.beginig = 0
        self.end = -1
        self.number_of_elements = 0
        self.values = np.empty(self.capacity, dtype=int)

    def __empty_queue(self):
        return self.number_of_elements == 0
    
    def __full_queue(self):
        return self.number_of_elements == self.capacity

    def add(self, value):
        if self.__full_queue():
            print('a pilha está cheia')
            return

        if self.end == self.capacity - 1:
            self.end = -1

        self.end += 1
        self.values[self.end] = value
        self.number_of_elements += 1
    
    def dequeue(self):
        if self.__empty_queue():
            print('a pilha está vazia')
            return

        temp = self.values[self.beginig]
        self.beginig += 1
        if self.beginig == self.capacity:
            self.beginig = 0
        self.number_of_elements -= 1
        return temp
    
    def first(self):
        if self.__empty_queue():
            return -1
        return self.values[self.beginig]

q = Queue(5)

print(q.first())

q.add(1)

print(q.first())
q.add(2)
q.add(3)
q.add(4)
q.add(5)

print(q.first())

q.dequeue()
q.dequeue()

print(q.first())

q.add(6)
q.add(7)

print(q.values)

print(q.beginig, q.end)