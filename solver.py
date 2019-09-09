from itertools import product
import operator
import random

def prGreen(skk): print("\033[92m{}\033[00m" .format(skk), end='')

def highlight_zero(string):
    for char in string:
        if char == '0':
            prGreen(char)
        else:
            print(char, end='')
    print(' ')



class Solver:
    def __init__(self, string):
        self.start_string = string
        self.next_empty = None

    start_string = property(operator.attrgetter('_start_string'))

    @start_string.setter
    def start_string(self, string):
        if len(string) != 81:
            raise Exception(f'Expected length is 81 characters. {string} is {len(string)} character long.')
        if not string.isnumeric():
            raise Exception(f'Expected {string} to contain only numbers.')

        self._start_string = string

    def find_next_empty(self):
        index = self.start_string.find('0')
        if index >= 0:
            self.next_empty = index
            return True
        return False

    def row_has_number(self, row, num):
        return num in list(self.start_string[row*9:row*9+9])

    def col_has_number(self, col, num):
        return num in [self.start_string[n] for n in range(col, 81, 9)]

    def box_has_number(self, box, num):
        boxes = [[] for _ in range(9)]
        for index in range(81):
            boxes[self.box_for(index)].append(self.start_string[index])
        return num in boxes[box]


    def row_for(self, index):
        return index // 9

    def col_for(self, index):
        return index % 9

    def box_for(self, index):
        return 3 * (self.row_for(index)//3) + (self.col_for(index)//3)

    def valid_trial(self, index, possible):
        return (not self.row_has_number(self.row_for(index), possible) and not
                   self.col_has_number(self.col_for(index), possible) and not
                   self.box_has_number(self.box_for(index), possible))

    def replace(self, index, value):
        new_string = list(self.start_string)
        new_string[index] = value
        self.start_string =  "".join(new_string)

    def solve(self):
        # print('Trial : ', end='')
        # highlight_zero(self.start_string)
        self.next_empty = 0

        if not self.find_next_empty():
            return True

        old = self.next_empty
        for possible in map(str,range(1,10)):
            if self.valid_trial(old, possible):
                self.replace(old, possible)

                if(self.solve()):
                    return True

                self.replace(old, '0')

        return False
