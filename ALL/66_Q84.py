# Problem:- 84. Largest Rectangle in Histogram

class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        stack = []    
        maxArea = 0

        heights.append(0)

        for i in range(len(heights)):

            while stack and heights[i] < heights[stack[-1]]:
                h = heights[stack.pop()]

                if stack:
                    width = i - stack[-1] - 1
                else:
                    width = i

                maxArea = max(maxArea, h * width)

            stack.append(i)

        return maxArea
            
            
            

if __name__ == "__main__":
    sol = Solution()
    heights = [2,1,5,6,2,3]
    # heights = [2,0,2]
    res = sol.largestRectangleArea(heights)
    print(res)