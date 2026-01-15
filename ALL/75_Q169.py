# Problem:- 169. Majority Element

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        majEl = None
        CurrNum = 0

        for num in nums:
            if CurrNum == 0:
                majEl = num
                CurrNum+=1
            elif num == majEl:
                CurrNum+=1
            else:
                CurrNum-=1
                
        return majEl
        
        
if __name__ == '__main__':
    sol = Solution()
    # nums = [3,2,3]
    # nums = [2,2,1,1,1,2,2]
    nums = [3,3,4]
    
    res = sol.majorityElement(nums)
    print(res)