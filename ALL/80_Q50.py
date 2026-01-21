# Problem:- 50. Pow(x, n)

class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n == 0:
            return 1
        
        if n < 0:
            x = 1 / x
            n = -n
        
        result = 1
        while n > 0:
            if n % 2 == 1:
                result *= x
            x *= x
            n //= 2
        
        return result

        # return x**n

if __name__ == '__main__':
    sol = Solution()
    x = 2.00000
    n = 13
    res = sol.myPow(x,n)
    print(res)