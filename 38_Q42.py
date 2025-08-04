# Problem:- 42. Trapping Rain Water

class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left = 0
        right = len(height) - 1
        leftMax = 0
        rightMax = 0
        waterArea = 0

        while left < right:
            if height[left] < height[right]:
                if height[left] >= leftMax:
                    leftMax = height[left]
                else:
                    waterArea += leftMax - height[left]
                left += 1
            else:
                if height[right] >= rightMax:
                    rightMax = height[right]
                else:
                    waterArea += rightMax - height[right]
                right -= 1

        return waterArea
                
                
                
                
        
        
        
if __name__ == '__main__':
    sol = Solution()
    height = [0,1,0,2,1,0,1,3,2,1,2,1]
    res = sol.trap(height)
    print(res)
    