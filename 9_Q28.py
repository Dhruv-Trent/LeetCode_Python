# Problem:- 28. Find the Index of the First Occurrence in a String
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        return haystack.find(needle)

                    
                    
if __name__ == '__main__':
    sol = Solution()
    result = sol.strStr("sadness","sad")
    print(result)
    