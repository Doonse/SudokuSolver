from square import Square

class Element():
    def __init__(self, type):
        self.element = [] # List of squares 
        self.type = type # Type of element (row, column, box)

    # Method appending a square to the element list
    def add_square(self, square):
        self.element.append(square) # Append the square to the element list
    
    # Check if the value is legal in the element
    def check_legal(self, num):
        return num not in self.element

        
    # Remove square from element list
    def remove_square(self, value):
        for square in self.element:
            if square == value:
                self.element.remove(square)
    
    # Get the element list
    def get_element(self):
        return self.element
    
    # Get the type of element (row, col, box)
    def get_type(self):
        return self.type
