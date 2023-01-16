import numpy as np


class Sudoku_reader:

    def __init__(self, filename):
        self.file = open(filename, "r")
        self.current_line = 0 # Not used, idk atm

    # Returns a 2D list (9*9) of ints
    def next_board(self):
        
        try:
            board_txt = self.file.readline() # Read in the game numbers and store in board_txt
            board_array = np.zeros((9,9)) # 9x9 array filled with only 0s
            sym_num = 0 # 0-80 (81 numbers on board), iteration variable
            

            # O(N^2), optimize to O(N) maybe
            # Itterate through file and insert data to array
            for i in range(9): 
                for j in range(9):
                    board_array[i,j] = int(board_txt[sym_num]) # 
                    
                    sym_num += 1 # ++ 


            return board_array


        except:
            print("Reading error")
            quit(-1)

    def __del__(self):
        self.file.close()
        



if __name__ == "__main__":
    # Test code to see the format
    s = Sudoku_reader("sudoku_10.csv")
    print(s.next_board())
