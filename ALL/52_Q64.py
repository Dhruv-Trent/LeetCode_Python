# Problem:- 64. Minimum Path Sum

class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid[0])
        n = len(grid)
        res = [[0 for _ in range(m)] for _ in range(n)]
        
        res[0][0] = grid[0][0]
        for i in range(1,m):
            res[0][i] += res[0][i-1]+ grid[0][i]
        
        for j in range(1,n):
            res[j][0] += res[j-1][0] + grid[j][0]
            
        for x in range(1,n):
            for y in range(1,m):
                res[x][y] = grid[x][y] + min(res[x][y-1], res[x-1][y])
        
        return res[-1][-1]
            
        
        
                  
        

if __name__ == '__main__':
    sol = Solution()
    grid = [[1,3,1],[1,5,1],[4,2,1]]
    res = sol.minPathSum(grid)
    print(res)