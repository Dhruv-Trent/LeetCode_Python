# problem:- 26. Remove Duplicates from Sorted Array
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        
        insert_pos = 1

        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                nums[insert_pos] = nums[i]
                insert_pos+=1 
        return insert_pos
    
if __name__ == '__main__':
    nums = [1,1,2]
    s = Solution()
    k = s.removeDuplicates(nums)
    print("k =", k)
    print("Modified nums:", nums[:k])
        
