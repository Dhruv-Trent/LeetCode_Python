# Problem:- 5. Longest Palindromic Substring

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        max = ""

        def helper(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1:right]

        for i in range(len(s)):
            odd = helper(i, i)      
            even = helper(i, i + 1)  

            if len(odd) > len(max):
                max = odd
            if len(even) > len(max):
                max = even

        return max
        
                
        
        
if __name__ == "__main__":
    sol = Solution()
    s = "babad"
    res = sol.longestPalindrome(s)
    print(res)