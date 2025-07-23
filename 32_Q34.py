# Problem:- 34. Find First and Last Position of Element in Sorted Array

# 15 mins to solve this 
# note it was very straight forward question.


class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        left = 0
        right = len(nums)-1
        
        while (left<=right):
            mid = (left+right)//2
            if nums[mid]==target:
                left = mid 
                right=mid
                while left >= 0 and nums[left]==target:
                    left-=1
                while right < len(nums) and nums[right] == target:
                    right +=1
                
                return [left+1,right-1]
                    
            elif nums[mid]<target:
                left = mid+1
            else:
                right = mid -1    
        return [-1,-1]


if __name__ == '__main__':
    sol = Solution()
    nums = [5,7,7,8,8,10]
    target = 8
    
    res = sol.searchRange(nums,target)
    print(res)