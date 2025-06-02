# Problem:- 58. Length of Last Word
class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        splited = s.split()
        
        return len(splited[-1]) if splited else 0
        
        
        
if __name__ == '__main__':
    sol = Solution()
    s = "Hello World  "
    result = sol.lengthOfLastWord(s)
    print(result)
    