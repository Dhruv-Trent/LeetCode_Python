# Problem:- 45. Jump Game II

# 30 - 40 min to solve this 
# Note:- It was not that tough question but need to think in a correct way. Anyways its ok question.

class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n= len(nums)
        if n<=1:
            return 0
        jumps = 0
        curr = 0
        maxJump = 0
        
        for i in range(n-1):
            maxJump = max(maxJump,i+nums[i])
            if i == curr:
                jumps+=1
                curr = maxJump
                if curr >= n-1:
                    break
        return jumps




            
if __name__ == '__main__':
    sol = Solution()
    nums = [2,3,1,1,4]
    res = sol.jump(nums)
    print(res)