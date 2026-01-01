# Problem:- 80. Remove Duplicates from Sorted Array II


class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        i = 0
        j = 1
        while True:
            if i >= len(nums) or j >= len(nums) or nums[i] == "_" or nums[j]=="_":
                return j
            if nums[i] == nums[j]:
                if j-i > 1:
                    del nums[j]
                    nums.append("_")
                else:
                    j+=1
            else:
                i=j
                j+=1
                
            
                
            
        
        
        
if __name__ == "__main__":
    sol = Solution()
    nums = [1,1,1,2,2,3]
    # nums = [0,0,1,1,1,1,2,3,3]
    # nums = [1]
    res = sol.removeDuplicates(nums)
    print(res,nums)
