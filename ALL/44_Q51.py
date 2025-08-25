# Problem:- 51. N-Queens

# 40-45 min 
# Note:- This question looked really hard at the first glance but i saw a online video that explained the question really well and i got the idea from the video that i need to use backtracking to solve this and i did it easily after that it was just not that hard.

class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        ans = []
        board = [['.' for j in range(n)] for i in range(n)]
        
        self.nQueens(board,0,0,n,ans)
        return ans
        
    def nQueens(self,board, row, col, n, ans):
        if row == n:
            ans.append([''.join(row) for row in board])
            return
        for j in range(n):
            if self.isSafe(board,row,j,n):
                board[row][j] = 'Q'
                self.nQueens(board,row+1,col,n,ans)
                board[row][j] = '.'

    
    def isSafe(self, board, row, col, n):
        # Horizontal
        for j in range(col):
            if board[row][j] == 'Q':
                return False
        
        # Vertical
        for i in range(row):
            if board[i][col] == 'Q':
                return False
        
        # Diagonal Left Side
        i = row - 1
        j = col - 1
        while(i >= 0 and j >= 0):
            if board[i][j] == 'Q':
                return False
            i -= 1
            j -= 1
            
        # Diagonal Right Side
        i = row - 1
        j = col + 1
        while(i >= 0 and j < n):
            if board[i][j] == 'Q':
                return False
            i -= 1
            j += 1
            
            
        return True


        


if __name__ == '__main__':
    sol = Solution()
    n = 4
    res = sol.solveNQueens(n)
    print(res)
    