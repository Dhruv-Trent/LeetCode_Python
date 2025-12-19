# Problem:- 78. Subsets

class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = [[]]
        
        for n in nums:
            dupl = []
            for oldList in res:
                dupl.append(oldList + [n])
            res.extend(dupl)
        
        return res






if __name__ == '__main__':
    
    sol = Solution()
    nums = [1,2,3,4,5,6,7,8,9,10]
    res = sol.subsets(nums)
    print(res)
