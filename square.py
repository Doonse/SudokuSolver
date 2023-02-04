
class Square:
    def __init__(self, num):
        self.num = num # Number in square
        self.row = None # Row position
        self.col = None # Column position
        self.box = None # Box position

    # Check legality of number in a list
    def check_legal(self, num, array):
        if num in array: 
            return False
        else:
            return True

    # Setters and getters
    def set_num(self, num): 
        self.num = num 
    
    def get_num(self):
        return self.num 




