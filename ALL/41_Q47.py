# Problem:- 47. Permutations II

class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        res = []
        used = [False] * len(nums)
        
        def backtrack(path):
            if len(path) == len(nums):
                res.append(path[:])
                return 
            for i in range(len(nums)):
                if used[i]:
                    continue
                if i > 0 and nums[i] == nums[i-1] and not used[i-1]:
                    continue
                used[i] = True
                path.append(nums[i])
                backtrack(path)
                path.pop()
                used[i] = False
        backtrack([])
        
        return res


if __name__ == '__main__':
    sol = Solution()
    nums = [1,1,2]
    res = sol.permuteUnique(nums)
    print(res)