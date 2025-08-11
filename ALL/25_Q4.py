# Problem:- 4. Median of Two Sorted Arrays
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums3 = nums1 + nums2
        nums3.sort()
        
        if(len(nums3)%2!=0):
            return nums3[len(nums3)//2]
        else:
            total = nums3[len(nums3)//2-1] + nums3[len(nums3)//2]
            average = total/2 
            return average
        
        
        
if __name__ == '__main__':
    s = Solution()
    nums1 = [1,2]
    nums2 = [3,4]
    res = s.findMedianSortedArrays(nums1,nums2)
    print(res)
