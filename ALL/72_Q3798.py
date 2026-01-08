# Problem:- 3798. Largest Even Number

class Solution(object):
    def largestEven(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        if s[n-1]== '2':
            return s
        i=n-1
        while i>=0:
            if s[i]== '2':
                return s[:i+1]
            else:
                i-=1
        return ""

if __name__ == "__main__":
    sol = Solution()
    s = "221111111221"
    res = sol.largestEven(s)
    print(res)