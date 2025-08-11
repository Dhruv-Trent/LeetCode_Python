# Problem:- 16. 3Sum Closest

# 18 min to solve 
# note:- i did everything perfect what took my time was just closeSum i used 0 insted of float('inf') which colud get wrong answers in some case but overall its preety mush very straight question. 


class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        nums.sort()
        n = len(nums)
        closeSum = float('inf')
        for i in range(n):
            left = i+1
            right = n-1
            
            while left<right:
                CurrSum = nums[i] + nums[left] + nums[right]
                
                if abs(target-CurrSum)< abs(target-closeSum):
                    closeSum = CurrSum
                    
                if CurrSum>target:
                    right-=1
                elif CurrSum<target:
                    left+=1
                else:
                    return CurrSum
            
        return closeSum
                
        
        


if __name__ == '__main__':
    sol = Solution()
    nums = [-1,2,1,-4]
    target = 1
    res = sol.threeSumClosest(nums,target)
    print(res)