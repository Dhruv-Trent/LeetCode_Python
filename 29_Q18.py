# Problem:- 18. 4Sum

#  min to solve 

class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        n = len(nums)
        res = []
        for i in range(n):
            for j in range(n):
                if i!= j:
                    left = i+1
                    right = n-1
                    while(left<right):
                        totalNow = nums[i] + nums[j] + nums[left] + nums[right]
                        if totalNow>target:
                            right-=1
                        elif totalNow<target:
                            left+=1
                        else:
                            res.append([nums[i], nums[j], nums[left], nums[right]])
                            left+=1
                            right-=1
                            
                            while left <right and nums[left] == nums[left - 1]:
                                left+=1
                            while left < right and nums[right] == nums[right + 1]:
                                right -= 1
                            
            
        return res
        

if __name__ == '__main__':
    sol = Solution()
    nums = [1,0,-1,0,-2,2]
    target = 0
    res = sol.fourSum(nums,target)
    print(res)