# Problem:- 46. Permutations

class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res  = []
        def backtrack(path, used):
            if len(path) == len(nums):
                res.append(path[:])
                return
            for i in range(len(nums)):
                if i in used:
                    continue
                used.add(i)
                path.append(nums[i])
                backtrack(path,used)
                path.pop()
                used.remove(i)
        backtrack([],set())
        return res


if __name__ == '__main__':
    sol = Solution()
    nums = [1,2,3]
    res = sol.permute(nums)
    print(res)