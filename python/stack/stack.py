import numpy as np

class Stack:
    def __init__(self, capacity):
        self.__capacity = capacity
        self.__top = -1
        self.__values = np.empty(self.__capacity, dtype=int)
    
    def __full_stack(self):
        if self.__top == self.__capacity - 1:
            return True
        else:
            return False

    def __empty_stack(self):
        if self.__top == -1:
            return True
        else: 
            return False

    def stack_up(self, value):
        if self.__full_stack():
            print('The stack is full')
        else: 
            self.__top += 1
            self.__values[self.__top] = value

    def unstack(self):
        if self.__empty_stack():
            print('the stack is empty')
        else:
            self.__top -= 1

    def get_top(self):
        if self.__top != -1:
            return self.__values[self.__top]
        else: 
            return -1


stack = Stack(5)
stack.stack_up(1)
stack.stack_up(2)
stack.stack_up(3)
stack.stack_up(4)
stack.stack_up(5)
stack.unstack()
print(stack.get_top())