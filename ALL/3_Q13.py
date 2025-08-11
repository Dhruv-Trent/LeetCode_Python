# Problem:- 13. Roman to Integer

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """

        dict = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        number = 0
        s = s.replace("IV", "IIII").replace("IX", "VIIII")
        s = s.replace("XL", "XXXX").replace("XC", "LXXXX")
        s = s.replace("CD", "CCCC").replace("CM", "DCCCC")
        for char in s:
            number += dict[char]
        return number
if __name__ == '__main__':
    s = Solution()
    res = s.romanToInt("III")
    res2 = s.romanToInt('LVIII')
    res3 = s.romanToInt("MCMXCIV")
    print(res)
    print(res2)
    print(res3)