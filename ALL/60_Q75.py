# Problem:- 75. Sort Colors

class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        
        low = 0
        mid = 0
        high = len(nums) - 1

        while mid <= high:
            if nums[mid] == 0:
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1
            elif nums[mid] == 1:
                mid += 1
            else:  
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1
                
        
        
if __name__ == '__main__':
    sol = Solution()
    nums = [2,0,2,1,1,0]
    # nums = [2,0,1]
    # nums = [2,1]
    res = sol.sortColors(nums)
    print(nums)






















# # This is very basic straightforward answer but it takes more space 
#  def sortColors(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: None Do not return anything, modify nums in-place instead.
#         """
        
#         if len(nums) < 2:
#             return

#         distNums = {
#             0: 0,
#             1: 0,
#             2: 0
#         }

#         for n in nums:
#             distNums[n] += 1

#         indx = 0
        
#         for _ in range(distNums[0]):
#             nums[indx] = 0
#             indx += 1

#         for _ in range(distNums[1]):
#             nums[indx] = 1
#             indx += 1

#         for _ in range(distNums[2]):
#             nums[indx] = 2
#             indx += 1
        
