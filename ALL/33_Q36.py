# Problem:- 36. Valid Sudoku

# 45 min to solve 
# note :- took some extra tie because in the starting i was thinking in other way.

class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        #Rule:-1 Each row must contain the digits 1-9 without repetition.
        for row in board:
            seen = set()
            for val in row:
                if val != '.':
                    if val in seen:
                        return False
                    seen.add(val)
           
        
        
        #Rule:-2 Each column must contain the digits 1-9 without repetition.
        for col in range(9):
            seen =set()
            for row in range(9):
                val = board[row][col]
                if val != '.':
                    if val in seen:
                        return False
                    seen.add(val)
        
        #Rule:-3 Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
        for row in range(0,9,3):
            for col in range(0,9,3):
                seen = set()
                for i in range(3):
                    for j in range(3):
                        val = board[row+i][col+j]
                        if val != '.':
                            if val in seen:
                                return False
                            seen.add(val)
        
        return True



if __name__ == '__main__':
    sol = Solution()
    board = [["5","3",".",".","7",".",".",".","."]
    ,["6",".",".","1","9","5",".",".","."]
    ,[".","9","8",".",".",".",".","6","."]
    ,["8",".",".",".","6",".",".",".","3"]
    ,["4",".",".","8",".","3",".",".","1"]
    ,["7",".",".",".","2",".",".",".","6"]
    ,[".","6",".",".",".",".","2","8","."]
    ,[".",".",".","4","1","9",".",".","5"]
    ,[".",".",".",".","8",".",".","7","9"]]
    res = sol.isValidSudoku(board)
    print(res)