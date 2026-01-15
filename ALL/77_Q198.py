# Proobblem:- 198. House Robber

class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        rob1=0
        rob2=0
        for n in nums:
            temp = max(rob1+n,rob2)
            rob1 = rob2
            rob2 =temp
        return rob2    
if __name__ == '__main__':
    sol = Solution()
    nums = [1,2,3,1]
    nums = [2,7,9,3,1]
    # nums = [2,1,1,2]
    res = sol.rob(nums)
    print(res)