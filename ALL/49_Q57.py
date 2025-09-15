# Problem:- 57. Insert Interval

class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        left = 0
        right = len(intervals)-1
        
        while(left<=right):
            mid = (left+right)//2
            if(intervals[mid][0] >= newInterval[0]):
                right = mid-1
            else:
                left = mid+1
        
        intervals.insert(left, newInterval)
        
        res = []
        for interval in intervals:
            if not res or res[-1][1]< interval[0]:
                res.append(interval)
            else:
                res[-1][1] = max(res[-1][1],interval[1])
        return res
        
                

if __name__ == '__main__':
    sol = Solution()
    intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
    newInterval = [4,8]
    res = sol.insert(intervals,newInterval)
    print(res)