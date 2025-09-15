# Problem:- 59. Spiral Matrix II

class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        if n == 1:
            return [[n]]
        
        matrix = [['.'] * n for _ in range(n)]

        
        top =0
        bottom = n-1
        left = 0
        right = n-1
        num = 1
        
        while(num<= n*n):
            # 1. top row
            for i in range(left, right + 1):
                matrix[top][i] = num
                num+=1
            top += 1
            
            # 2. right column
            for i in range(top,bottom+1):
                matrix[i][right] = num
                num+=1
            right -=1
            
            # 3. bottom row 
            for i in range(right,left-1,-1):
                matrix[bottom][i] = num
                num+=1
            bottom-=1
            
            # 4. left column
            for i in range(bottom,top-1,-1):
                matrix[i][left] = num
                num+=1
            left+=1
            
        return matrix
            
        
                

if __name__ == '__main__':
    sol = Solution()
    n = 1
    res = sol.generateMatrix(n)
    print(res)