# Problem:- 119. Pascal's Triangle II

class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        
        # triangle = []
        # numRows = rowIndex+1
        
        # for i in range(numRows):
        #     row = [1] * (i + 1)
            
        #     for j in range(1, i):
        #         row[j] = triangle[i-1][j-1] + triangle[i-1][j]
            
        #     triangle.append(row)
            
        # return triangle[rowIndex]
        
        row = [1] * (rowIndex + 1)

        for i in range(1, rowIndex):
           
            for j in range(i, 0, -1):
                row[j] = row[j] + row[j - 1]

        return row
      

            
        
            
            
            

if __name__ == "__main__":
    sol = Solution()
    rowIndex = 5
    res = sol.getRow(rowIndex)
    print(res)