# Problem:- 14. Longest Common Prefix

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        strs.sort()
        print(strs)
        i = 1
        while i <= len(strs[0]):
            if strs[0][:i] == strs[-1][:i]:
                i += 1
            else:
                break
        return strs[0][:i-1]

if __name__ == '__main__':
    s = Solution()
    res = s.longestCommonPrefix(['flower', 'flow', 'flight'])
    print(res)




# this is second solution 
# class Solution(object):
#     def longestCommonPrefix(self, strs):
#         """
#         :type strs: List[str]
#         :rtype: str
#         """
#         lcp=""
#         ch = ''
#         for i in range(len(strs[0])):
#             ch += strs[0][i]

#             for x in strs:
#                 if len(x)<len(ch):
#                     break
#                 if x[0:i+1] != ch:
#                     return lcp
#             lcp = ch
#         return lcp     