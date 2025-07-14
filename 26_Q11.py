# Problem:- 11. Container With Most Water  

# 28 min to solve 



class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        maxArea = 0
        left = 0
        right = len(height)-1
        # maxAreaLeft = 0
        # maxAreaRight = 0
        
        while left<right:
            if (min(height[left], height[right])) * (right-left) >= maxArea:
                # maxAreaLeft = left
                # maxAreaRight = right
                maxArea = (min(height[left], height[right])) * (right-left)
                
            if (height[left]>=height[right]):
                right = right-1
            else:
                left = left+1
        
        return maxArea
                
                
                
        


if __name__ == '__main__':
    s = Solution()
    height = [1,8,6,2,5,4,8,3,7]
    res = s.maxArea(height)
    print(res)

