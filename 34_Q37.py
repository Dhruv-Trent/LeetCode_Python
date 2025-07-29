# Problem:- 37. Sudoku Solver

# NOTE:- The logic was straightforward, but my initial solution ran into a Time Limit Exceeded (TLE) error. This final version is my third attempt, where I optimized performance by precomputing empty cells and using sets to track used numbers. These changes made it efficient enough to pass all test cases.
## last solution needed help from chatgpt to think but did it my self.

class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """ 
        self.row = [set() for _ in range(9)]
        self.col = [set() for _ in range(9)]
        self.boxes = [[set() for _ in range(3)] for _ in range(3)]
        self.empty = []
        
        for i in range(9):
            for j in range(9):
                val = board[i][j]
                if val == '.':
                    self.empty.append((i, j))
                else:
                    self.row[i].add(val)
                    self.col[j].add(val)
                    self.boxes[i//3][j//3].add(val)
        
        self.backTrack(board,0)
        
    def backTrack(self,board,idx):
        if idx == len(self.empty):
            return True
        
        i,j = self.empty[idx]
        for num in "123456789":
            if self.isValid(i,j,num):
                board[i][j] = num
                self.row[i].add(num)
                self.col[j].add(num)
                self.boxes[i//3][j//3].add(num)
                
                if self.backTrack(board,idx+1):
                    return True
                
                board[i][j] = '.'
                self.row[i].remove(num)
                self.col[j].remove(num)
                self.boxes[i//3][j//3].remove(num)
        return False

                
    def isValid(self,i,j,num):
        return (num not in self.row[i] and num not in self.col[j] and num not in self.boxes[i//3][j//3])
        

import time
if __name__ == '__main__':
    sol = Solution()
    board = [[".",".",".",".",".",".",".",".","."],[".","9",".",".","1",".",".","3","."],[".",".","6",".","2",".","7",".","."],[".",".",".","3",".","4",".",".","."],["2","1",".",".",".",".",".","9","8"],[".",".",".",".",".",".",".",".","."],[".",".","2","5",".","6","4",".","."],[".","8",".",".",".",".",".","1","."],[".",".",".",".",".",".",".",".","."]]
    start = time.time()
    res = sol.solveSudoku(board)
    end = time.time()

    for row in board:
        print(row)

print(end-start)        

  
## ----------------------------------------------First method---------------------------------------------- 
## ---------------------------------------------- This takes 4.5 - 5.0 second to run in some hard cases---------------------------------------------- 
     
    # def solveSudoku(self, board):
    #     """
    #     :type board: List[List[str]]
    #     :rtype: None Do not return anything, modify board in-place instead.
    #     """
    #     self.backtrack(board)
        
    # def backtrack(self, board):
    #     for i in range(9):
    #         for j in range(9):
    #             if board[i][j]=='.':
    #                 for num in "123456789":
    #                     if self.isValid(board, i, j, num):
    #                         board[i][j] = num
    #                         if self.backtrack(board): 
    #                             return True
    #                         board[i][j] = "."  
    #                 return False
    #     return True         
                            

        
    # def isValid(self, board, row, col, num):

    #     for i in range(9):
    #         if board[row][i] == num or board[i][col] == num:
    #             return False

    #     startRow = 3 * (row // 3)
    #     startCol = 3 * (col // 3)
    #     for i in range(3):
    #         for j in range(3):
    #             if board[startRow + i][startCol + j] == num:
    #                 return False

    #     return True


## ---------------------------------------------- Second method----------------------------------------------
## ---------------------------------------------- This takes 2.0 - 3.0 second to run in some hard cases---------------------------------------------- 
#     def solveSudoku(self, board):
#         """
#         :type board: List[List[str]]
#         :rtype: None Do not return anything, modify board in-place instead.
#         """
#         self.row = [set() for _ in range(9)]
#         self.col = [set() for _ in range(9)]
#         self.boxes = [[set() for _ in range(3)] for _ in range(3)]
        
#         for i in range(9):
#             for j in range(9):
#                 val = board[i][j]
#                 if val!='.':
#                     self.row[i].add(val)
#                     self.col[j].add(val)
#                     self.boxes[i//3][j//3].add(val)
        
#         self.backtrack(board)
        
#     def backtrack(self, board):
#         for i in range(9):
#             for j in range(9):
#                 if board[i][j] == '.':
#                     for num in "123456789":
#                         if self.isVaild(i,j,num):
#                             board[i][j] = num
#                             self.row[i].add(num)
#                             self.col[j].add(num)
#                             self.boxes[i//3][j//3].add(num)
                            
#                             if self.backtrack(board):
#                                 return True
                            
#                             board[i][j] = '.'
#                             self.row[i].remove(num)
#                             self.col[j].remove(num)
#                             self.boxes[i//3][j//3].remove(num)
#                     return False
#         return True
        
#     def isVaild(self,i,j,num):
#         return (num not in self.row[i] and num not in self.col[j] and num not in self.boxes[i//3][j//3])





## ----------------------------------------------Third method----------------------------------------------
## ---------------------------------------------- This takes 1 - 1.6 second to run in some hard cases---------------------------------------------- 
#  def solveSudoku(self, board):
#         """
#         :type board: List[List[str]]
#         :rtype: None Do not return anything, modify board in-place instead.
#         """ 
#         self.row = [set() for _ in range(9)]
#         self.col = [set() for _ in range(9)]
#         self.boxes = [[set() for _ in range(3)] for _ in range(3)]
#         self.empty = []


#         for i in range(9):
#             for j in range(9):
#                 val = board[i][j]
#                 if val == '.':
#                     self.empty.append((i, j))
#                 else:
#                     self.row[i].add(val)
#                     self.col[j].add(val)
#                     self.boxes[i//3][j//3].add(val)

#         self.backtrack(board, 0)

#     def backtrack(self, board, idx):
#         if idx == len(self.empty):
#             return True 

#         i, j = self.empty[idx]
#         for num in "123456789":
#             if self.isValid(i, j, num):
#                 board[i][j] = num
#                 self.row[i].add(num)
#                 self.col[j].add(num)
#                 self.boxes[i//3][j//3].add(num)

#                 if self.backtrack(board, idx + 1):
#                     return True

#                 board[i][j] = '.'
#                 self.row[i].remove(num)
#                 self.col[j].remove(num)
#                 self.boxes[i//3][j//3].remove(num)

#         return False

#     def isValid(self, i, j, num):
#         return (
#             num not in self.row[i] and
#             num not in self.col[j] and
#             num not in self.boxes[i//3][j//3]
#         )