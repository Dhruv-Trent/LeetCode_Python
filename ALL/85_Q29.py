# Problem:-29. Divide Two Integers

class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        
        max = 2**31 - 1
        min = -(2**31)

        if dividend == min and divisor == -1:
            return max

        neg = (dividend < 0) != (divisor < 0)

        dividend = abs(dividend)
        divisor = abs(divisor)

        quotient = 0

        while dividend >= divisor:
            newdivisor = divisor
            multiple = 1

            while dividend >= (newdivisor << 1):
                newdivisor <<= 1
                multiple <<= 1

            dividend -= newdivisor
            quotient += multiple

        return -quotient if neg else quotient

if __name__ == '__main__':
    sol = Solution()
    dividend = -1
    divisor = 1
    res = sol.divide(dividend,divisor)
    print(res)
