# Problem:- 20. Valid Parentheses

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        stack = []
        dict = {
            ")": "(",
            "]": "[",
            "}": "{"
        }
        for ch in s:
            if ch in dict.values():
                stack.append(ch)
            elif ch in dict.keys():
                if ((not stack) or (stack[-1] != dict[ch])):
                    return False
                else:
                    stack.pop()
            else:
                return False
        return not stack





if __name__ == '__main__':
    s = Solution()
    res = s.isValid("([])")
    print(res)