# Problem:- 53. Maximum Subarray

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
  
        maxSum = float('-inf')
        currSum = 0
        for num in nums:
            currSum += num
            
            if maxSum<currSum:
                maxSum = currSum
            
            if currSum < 0:
                currSum = 0
        
        return maxSum
        


if __name__ == '__main__':
    sol = Solution()
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    res = sol.maxSubArray(nums)
    print(res)
    