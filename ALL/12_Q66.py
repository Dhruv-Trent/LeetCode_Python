# Problem:- 66. Plus One
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        n = len(digits)
        for i in range(n-1,-1,-1):
            print(i)
            if digits[i]<9:
                digits[i]+=1
                return digits
            digits[i] = 0
        return [1] + digits
                
        
if __name__ == '__main__':
    sol = Solution()
    digits = [1,2,3]
    result = sol.plusOne(digits)
    print(result)
    