# Problem:- 56. Merge Intervals


class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals.sort()
        res  = []
        if not intervals:
            return res

        for curr in intervals:
            
            if res and curr[0] <= res[-1][1] :
                res[-1][1] = max(curr[1], res[-1][1])
            else:
                res.append(curr)
        return res

        
if __name__ == '__main__':
    sol = Solution()
    intervals = [[1,3],[2,6],[8,10],[15,18]]
    # intervals = [[1,4],[4,5]]
    # intervals = [[4,7],[1,4]]
    # intervals = [[1,2],[3,4],[5,6]]
    # intervals = [[1,5],[2,6],[3,7],[4,8]]
    # intervals = [[1,10],[2,3],[4,5],[6,7]]
    intervals = [[1,2],[100,200],[300,400]]
    res = sol.merge(intervals)
    print(res)