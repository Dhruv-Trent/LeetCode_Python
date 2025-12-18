# Problem:- 74. Search a 2D Matrix

class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        m = len(matrix)
        n = len(matrix[0])
        
        if target < matrix[0][0] or target > matrix[m-1][n-1]:
            return False
        
        for i in range(m):
            if matrix[i][0] <= target <= matrix[i][n-1]:
                left =0
                right =n-1
                while left<=right:
                    mid = (left+right) // 2
                    if matrix[i][mid] == target:
                        return True
                    elif matrix[i][mid]> target:
                        right = mid-1
                    else:
                        left = mid+1
                return False
        
        return False
        
        

if __name__ == '__main__':
    sol = Solution()
    # matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
    # target = 3
    matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
    target = 13
    # matrix = [[1]]
    # target = 1
    res = sol.searchMatrix(matrix,target)
    print(res)
