# Problem:- 67. Add Binary
class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        result = []
        carry = 0

        maxLen = max(len(a),len(b))
        a = a.zfill(maxLen)
        b = b.zfill(maxLen)
        for i in range(maxLen-1,-1,-1):
            total = carry + int(a[i]) + int(b[i])
            result.append(str(total % 2))
            carry = total // 2

        if carry:
            result.append('1')
            
        return ''.join(reversed(result))

if __name__ == '__main__':
    sol = Solution()
    a = "11"
    b = "1"
    result = sol.addBinary(a,b)
    print(result)