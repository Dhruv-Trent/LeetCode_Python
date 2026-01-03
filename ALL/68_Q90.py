# Problem:- 90. Subsets II

class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        res = [[]]
        prevSize = 0
        
        for i,n in enumerate(nums):
            if i > 0 and nums[i] == nums[i-1]:
                start = prevSize 
            else:
                start = 0
                
            prevSize = len(res)
            
            for j in range(start, prevSize):
                res.append(res[j] + [n])
        return res
    


        
        
        



if __name__ == "__main__":
    sol = Solution()
    nums = [1,2,2]
    nums = [0]
    nums = [4,4,4,1,4]
    res = sol.subsetsWithDup(nums)
    print(res)    