 # Problem:- 1. Two Sum
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        num_map = {}
        for i, num in enumerate(nums):
            complement = target -num
            if complement in num_map:
                return [num_map[complement], i]
            num_map[num] = i


if __name__ == "__main__":
    sol = Solution()
    result = sol.twoSum([2, 7, 11, 15], 9)
    print(result)