# Problem:- 31. Next Permutation

#   1 and half day to solve 
# notes it was very tough question when started I was not thinking in a this area. Now I got it
#   must do it again 

class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        
        i = len(nums)-2
        
        while i>=0 and nums[i]>= nums[i+1]:
            i-=1
            
        if i >= 0:
            j = len(nums) - 1
            while nums[j] <= nums[i]:
                j -= 1
                
            nums[i], nums[j] = nums[j], nums[i]   
             
        left=i + 1
        right = len(nums) - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1

        
        
        
        
if __name__ == '__main__':
    sol = Solution()
    nums = [1,2,3 ,4,7,6,5]
    # nums = [3,2,1]
    sol.nextPermutation(nums)
    print(nums)