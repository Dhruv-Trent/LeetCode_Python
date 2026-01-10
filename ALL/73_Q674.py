# Problem:- 674. Longest Continuous Increasing Subsequence

class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        currSeq = 1
        lastSeq = 0
        for i in range(1,len(nums)):
            if nums[i-1]<nums[i]:
                currSeq+=1
            else: 
                if currSeq>lastSeq:
                    lastSeq = currSeq
                currSeq=1
                
                
        return currSeq if currSeq>lastSeq else lastSeq

        
        
if __name__ == '__main__':
    sol = Solution()
    nums = [2]
    res = sol.findLengthOfLCIS(nums)
    print(res)