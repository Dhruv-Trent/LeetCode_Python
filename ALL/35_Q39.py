# Problem:- 39. Combination Sum   


class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        self.result = []
        self.candidates = candidates
        self.target = target
        self.backtrack(0, [], 0)
        return self.result

    def backtrack(self, start, current_combination, current_sum):
        if current_sum == self.target:
            self.result.append(list(current_combination))
            return
        if current_sum > self.target:
            return

        for i in range(start, len(self.candidates)):
            current_combination.append(self.candidates[i])
            self.backtrack(i, current_combination, current_sum + self.candidates[i])
            current_combination.pop()

        
        
        
        
import time
if __name__ == '__main__':
    sol = Solution()
    candidates = [2,3,6,7]
    target = 7
    start = time.time()
    res = sol.combinationSum(candidates,target)
    end = time.time()
    print(res)
    print(end-start)