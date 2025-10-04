# Problem:- 121. Best Time to Buy and Sell Stock


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        smallest = float('inf')   
        maxDiff = 0            

        for price in prices:
            if price < smallest:
                smallest = price
            
            profit = price - smallest
            if profit > maxDiff:
                maxDiff = profit

        return maxDiff
            
        
        

if __name__ == '__main__':
    sol = Solution()
    prices = [7,1,5,3,6,4]
    res = sol.maxProfit(prices)
    print(res)
