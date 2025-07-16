# Problem:- 18. 4Sum

#  30 min to solve 

# note:- The only thing that take my time is i was not skiping the duplicates for i and j 

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
            if i > 0 and nums[i] == nums[i - 1]:
                continue  
            for j in range(i + 1, n):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                left = j + 1
                right = n - 1
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