# Problem:- 41. First Missing Positive

class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        missingNum=1
        for i in range(len(nums)):
            if nums[i] <=0:
                continue
            if i > 0 and nums[i] == nums[i - 1]: 
                continue
            if nums[i] == missingNum:
                missingNum+=1
            else:
                return missingNum



            
            if nums[i] == missingNum:
                missingNum += 1
            elif nums[i] > missingNum:
                return missingNum
        return missingNum
        


if __name__ == '__main__':
    sol = Solution()
    nums = [1,1]
    res = sol.firstMissingPositive(nums)
    print(res)
