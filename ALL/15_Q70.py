# Problem:- 70. Climbing Stairs
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1 or n==2:
            return n
        
        a,b = 1,2
        for i in range(3, n + 1):
            a, b = b, a + b
        return b 

if __name__ == '__main__':
    sol = Solution()
    n = 10000
    res = sol.climbStairs(n)
    print(res)