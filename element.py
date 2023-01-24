from square import Square


class Element(Square):
    def __init__(self, row, col, num, nums):
        super().__init__(row, col, num, nums)
        self.nums = nums
        self.num = num
        self.row = row
        self.col = col
        self.box = None




if __name__ == "__main__":
    pass




