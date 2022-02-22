import re
import numpy as np

class Stack:
    def __init__(self, capacity):
        self.__capacity = capacity
        self.__top = -1
        self.__values = np.chararray(self.__capacity, unicode=True)
    
    def __full_stack(self):
        if self.__top == self.__capacity - 1:
            return True
        else:
            return False

    def empty_stack(self):
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
        if self.empty_stack():
            print('the stack is empty')
            return -1
        else:
            value = self.__values[self.__top]
            self.__top -= 1
            return value


    def get_top(self):
        if self.__top != -1:
            return self.__values[self.__top]
        else: 
            return -1

    def get(self):
        return self.__values
        
exp = str(input('Digite uma expressão: '))


def exp_validator(exp):
    return


exp_validator(exp)