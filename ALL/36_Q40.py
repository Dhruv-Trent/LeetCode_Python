# Problem:- 40. Combination Sum II

class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        self.result = []
        self.target = target
        self.candidates = candidates
        self.backTrack(0,[],0)
        return self.result
        
    def backTrack(self,start,curr_combination,curr_sum):
        if curr_sum == self.target:
            self.result.append(list(curr_combination))
            return
        for i in range(start,len(self.candidates)):
            if i >start and self.candidates[i] == self.candidates[i-1]:
                continue
            
            candidate = self.candidates[i]
            if candidate + curr_sum >self.target:
                break
            curr_combination.append(candidate)
            self.backTrack(i+1,curr_combination,curr_sum+candidate)
            curr_combination.pop()
            
            
                
                


                
                
        

if __name__ == '__main__':
    sol = Solution()
    candidates = [10,1,2,7,6,1,5]
    target = 8
    res = sol.combinationSum2(candidates,target)
    print(res)
