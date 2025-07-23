# Problem:- 33. Search in Rotated Sorted Array

# Note: This question was a bit easy for me because I'm comfortable with binary search. It just involved a small twist—understanding how to adjust the search boundaries in a rotated sorted array.

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        left = 0
        right = len(nums)-1
        
        while (left<=right):
            mid = (left+right)//2
            
            if nums[mid] == target:
                return mid
            
            if nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1    
                    
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
            
        return -1
                
        
        
if __name__ == '__main__':
    sol = Solution()
    nums = [4,5,6,7,0,1,2]
    target = 0
    res = sol.search(nums,target)
    print(res)