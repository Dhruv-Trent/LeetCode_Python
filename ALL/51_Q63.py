# Problem:- 63. Unique Paths II

class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        
        if obstacleGrid[0][0] == 1 or obstacleGrid[m-1][n-1] == 1:
            return 0
        
        mat = [[0] * n  for _ in range(m)]
        mat[0][0] = 1
        
        for i in range(1,n):
            if obstacleGrid[0][i] == 0:
                mat[0][i] = mat[0][i-1]
            else:
                mat[0][i] = 0
                
        
        for j in range(1,m):
            if obstacleGrid[j][0] == 0:
                mat[j][0] = mat[j-1][0]
            else:
                mat[j][0] = 0
        
        for i in range(1,m):
            for j in range(1,n):
                if obstacleGrid[i][j] == 0:
                    mat[i][j] = mat[i-1][j]+ mat[i][j-1]
                else:
                    mat[i][j] = 0
        
        return mat[m-1][n-1]
                
            
        

if __name__ == '__main__':
    sol = Solution()
    obstacleGrid = [[0,0],[1,1],[0,0]]
    res = sol.uniquePathsWithObstacles(obstacleGrid)
    print(res)