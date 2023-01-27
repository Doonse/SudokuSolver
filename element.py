from square import Square
import numpy as np

class Element():
    def __init__(self):
        self.element = []
        self.type = type

    # Check legality of number in row, column, and box, calling legality function in square
    
    def elem(self, square):
        self.element.append(square)
        if self.type == "row":
            Square.row = self
        elif self.type == "col":
            Square.col = self
        elif self.type == "box":
            Square.box = self
    
    def check_legal(self, value):
        for square in self.element:
            if square.get_num() == value:
                return False
        return True





