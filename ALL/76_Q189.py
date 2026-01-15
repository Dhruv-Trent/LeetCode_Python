# Problem:- 189. Rotate Array

class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k%n
        nums[k:], nums[:k] = nums[:n - k], nums[n - k:]



if __name__ == '__main__':
    sol = Solution()
    nums = [1,2,3,4,5,6,7]
    k = 3
    # nums = [-1,-100,3,99]
    # k = 2
    # nums = [1]
    # k =1
    # nums =[-1]
    # k =2
    sol.rotate(nums,k)
    print(nums)