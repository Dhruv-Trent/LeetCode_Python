# Problem:- 3. Longest Substring Without Repeating Characters

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        soFar = set()
        left = 0
        maxLen = 0

        for right in range(len(s)):
            while s[right] in soFar:
                soFar.remove(s[left])
                left += 1

            soFar.add(s[right])
            maxLen = max(maxLen, right - left + 1)

        return maxLen
        
if __name__ == "__main__":
    sol = Solution()
    s = "abcabcbb"
    s = "dvdf"
    res = sol.lengthOfLongestSubstring(s)
    print(res)