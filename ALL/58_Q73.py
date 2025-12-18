# Problem:- 73. Set Matrix Zeroes

class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        r,c = set(),set()
        
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    r.add(i)
                    c.add(j)
        
        for r in r:
            for j in range(n):
                matrix[r][j] = 0
        
        for c in c:
            for i in range(m):
                matrix[i][c] = 0
        
        return matrix


        

if __name__ == '__main__':
    sol = Solution()
    # matrix = [[1,1,1],[1,0,1],[1,1,1]]
    matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
    res = sol.setZeroes(matrix)
    print(res)
