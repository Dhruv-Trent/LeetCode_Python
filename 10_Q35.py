# Problem:- 35. Search Insert Position
class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        left = 0
        right = len(nums) - 1
        
        while left <= right:
            mid = (left+right)//2
            if nums[mid] == target:
                return mid
            elif nums[mid]>target:
                right = mid - 1
            else:
                left = mid + 1
        return left
            
    
        
if __name__ == '__main__':
    sol = Solution()
    nums = [1,3,5,6]
    target = 5
    result = sol.searchInsert(nums,target)
    print(result)
    