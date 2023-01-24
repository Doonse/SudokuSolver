from board import Board
from square import Square


class SudokuBoard(Board):

    def __init__(self):
        super().__init__()
        self.board = [[Square(i, j, self.nums[i][j], self.nums) for j in range(9)] for i in range(9)]

    def solve(self, row, col, number, array):
        Square.insert_number(row, col, number, array)


if __name__ == "__main__":
    board = Board()
    print(board)
    print(SudokuBoard())
    