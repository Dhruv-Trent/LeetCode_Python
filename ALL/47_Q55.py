# Problem:- 55. Jump Game

# 10-20 min to solve 
# Note:- This Question is also very strat forward if greedy solution clicked in ur mind than its very easy.


class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        i = 0
        maxJump = 0
        n = len(nums)
        
        if n<2:
            return True
        
        while(i <= maxJump and i < n):
            maxJump = max(maxJump, i+nums[i])
            if maxJump >= n-1:
                return True
            i+=1
        return False


if __name__ == '__main__':
    sol = Solution()
    nums = [2,0]
    res = sol.canJump(nums)
    print(res)