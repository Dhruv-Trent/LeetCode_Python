# Problem:- 15. 3Sum 

# 55 min to solve in total two apprach the final one is 35 min
# note i did solved this in 20 min but my approch was wrong becasue it takes O(n^3) time complexity so i have to do it again with different approch what my aprroch was i used three nedsted loop to get i j and k which is not optimal 

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # sumZeroTuple = []
        # for i in range(len(nums)):
        #     for j in range(len(nums)):
        #         for k in range(len(nums)):
        #             if i!=j and i!=k and j!=k:
        #                 if nums[i] + nums[j] + nums[k] == 0:
        #                     newTrio = [ nums[i] , nums[j] , nums[k]]
        #                     newTrio.sort()
        #                     newTrio = tuple(newTrio)
        #                     sumZeroTuple.append(newTrio)
        #                     # print(f'i = {i}, {nums[i]}\t j = {j}, {nums[j]}\t k = {k}, {nums[k]}')
        #                     # print(f'newTrio = {newTrio}')
        
        # sumZeroTupleSet = set(sumZeroTuple)
        # return list(map(list, sumZeroTupleSet))
        # # print(f'SumZero = {sumZeroTupleSet}')
        
        nums.sort()  
        res = []
        n = len(nums)
        
        for i in range(n):
            if i>0 and nums[i] == nums[i-1]:
                continue
            
            left = i+1
            right = n-1
            while(left<right):
                sumOfTrio = nums[i] + nums[left] + nums[right]
                if sumOfTrio<0:
                    left+=1
                elif sumOfTrio>0:
                    right-=1
                else:
                    res.append([nums[i],nums[left],nums[right]])
                    left = left+1
                    right = right-1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                        
            
        return res

        
        

if __name__ == '__main__':
    sol = Solution()
    nums = [-1,0,1,2,-1,-4]
    res = sol.threeSum(nums)
    print(res)