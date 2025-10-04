# Problem:- 242. Valid Anagram
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s)!=len(t):
            return False
        data = []
        for l in s:
            data.append(l)
            
        for m in t:
            if m in data:
                data.remove(m)
            else:
                return False
        
        if data:
            return False
        return True
        
        
        
if __name__ == '__main__':
    sol = Solution()
    s = "rat"
    t = "car"
    res = sol.isAnagram(s,t)
    print(res)