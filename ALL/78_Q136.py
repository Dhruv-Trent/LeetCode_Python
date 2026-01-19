# Problem:- 136. Single Number

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        for n in nums:
            res = n^res
        return res
        
        
if __name__ == '__main__':
    sol = Solution()
    # nums = [2,2,1]
    nums = [1,2,2,4,1,3,4,3,9,8,5,8,5] 
    res = sol.singleNumber(nums)
    print(res)
            