# Problem:- 27. Remove Element

class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        k = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        
        return k
            
            
        
if __name__ == '__main__':
    sol = Solution()
    nums = [3,2,2,3]
    res = sol.removeElement(nums,3)
    print(res)
    print(nums)
    
    nums2 = [0,1,2,2,3,0,4,2]
    res2 = sol.removeElement(nums2,2)
    print(res2)
    print(nums2)
    