# Problem:- 81. Search in Rotated Sorted Array II

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        
        left  = 0
        right = len(nums)-1
        while left<=right:
            mid = (left+right)//2
            
            if nums[mid] == target:
                return True

            if nums[left] == nums[mid] == nums[right]:
                left+=1
                right-=1
                
            
            elif nums[left] <= nums[mid]:
                if nums[left]<= target < nums[mid]:
                    right = mid-1
                else:
                    left = mid+1
                    
            else:
                if nums[right] >= target > nums[mid]:
                    left = mid+1
                else:
                    right = mid-1
        return False
        
        
        
if __name__ == "__main__":
    sol = Solution()
    nums = [2,5,6,0,0,1,2] 
    target = 0
    res = sol.search(nums,target)
    print(res,nums)
