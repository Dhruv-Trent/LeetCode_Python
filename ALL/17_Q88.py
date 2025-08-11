# Problem:- 88. Merge Sorted Array
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """

        
        for i in range(0,len(nums2)):
            nums1[m] = nums2[i]
            m+=1
            
        nums1.sort()
            
        
        
if __name__ =='__main__':    
    sol = Solution()
    nums1 = [1,2,3,0,0,0]
    m = 3
    nums2 = [2,5,6]
    n = 3
    sol.merge(nums1,m,nums2,n)
    print(f'nums1 => {nums1}')
    print(f'nums2 => {nums2}')
    