# Problem:- 9. Palindrome Number

class Solution(object):
    def isPalindrome(self,x):
        """
        :type x: int
        :rtype: bool
        """
        return str(x) == str(x)[::-1]

if __name__  == "__main__":
    sol = Solution()
    res = sol.isPalindrome(121)
    print(res)