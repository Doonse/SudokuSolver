from square import Square

class Element():
    def __init__(self, type):
        self.element = []
        self.type = type

    def add_square(self, square):
        self.element.append(square)
        if self.type == "row":
            square.set_row(self) 
        elif self.type == "col":
            square.set_col(self)
        elif self.type == "box":
            square.set_box(self)

    
    def check_legal(self, value):
        for square in self.element:
            if square.get_num() == value:
                return False
        return True

if __name__ == "__main__":
    e = Element("row")
    s = Square()
    e.add_square(s)
    print(e.element)
