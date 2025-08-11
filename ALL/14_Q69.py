# Problem:- 69. Sqrt(x)
class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        
        
        left = 0
        right = x
        ans = 0
        
        while left <= right:
            mid = (left+right) // 2
            if mid * mid == x:
                return mid
            elif mid*mid < x:
                ans = mid
                left = mid + 1
            else:
                right = mid - 1
        return ans
            
            
        
        
if __name__ == '__main__':
    sol = Solution()
    x = 8
    res = sol.mySqrt(x)
    print(res)
    