### x---------------*****---------------*****--------1.-------*****---------------*****---------------*****---------------x
# # 1. Two sum
# class Solution(object):
#     def twoSum(self, nums, target):
#         """
#         :type nums: List[int]
#         :type target: int
#         :rtype: List[int]
#         """
        
#         numMap = {}
        
#         for i,num in enumerate(nums):
#             complement = target - num
#             if complement in numMap:
#                 return [numMap[complement], i]
#             numMap[num] = i
          
# if __name__ == "__main__":
#     sol = Solution()
#     result = sol.twoSum([2, 7, 11, 15], 9)
#     print(result)

### x---------------*****---------------*****--------2.-------*****---------------*****---------------*****---------------x
# # 4. Median of Two Sorted Array
# class Solution(object):
#     def findMedianSortedArrays(self, nums1, nums2):
#         """
#         :type nums1: List[int]
#         :type nums2: List[int]
#         :rtype: float
#         """
#         num3 = nums1+nums2
#         num3.sort()
        
#         if (len(num3)%2==0):
#             return  (num3[len(num3)//2 -1]+ num3[len(num3)//2] )/2
#         else:
#             return num3[len(num3)//2]
        
# if __name__ == '__main__':
#     s = Solution()
#     nums1 = [1,2]
#     nums2 = [3,4]
#     res = s.findMedianSortedArrays(nums1,nums2)
#     print(res)

### x---------------*****---------------*****---------3.------*****---------------*****---------------*****---------------x
# # 9. Palindrome Number
# class Solution(object):
#     def isPalindrome(self, x):
#         """
#         :type x: int
#         :rtype: bool
#         """
#         return str(x) == str(x)[::-1]

# if __name__  == "__main__":
#     sol = Solution()
#     res = sol.isPalindrome(121)
#     print(res)

### x---------------*****---------------*****--------4.-------*****---------------*****---------------*****---------------x
# # 11. Container With Most Water
# class Solution(object):
#     def maxArea(self, height):
#         """
#         :type height: List[int]
#         :rtype: int
#         """
#         maxArea = 0
#         left = 0
#         right = len(height)-1
        
#         while(left<right):
#             if min(height[left],height[right]) * (right-left) >= maxArea:
#                 maxArea = (min(height[left], height[right])) * (right-left)
#             if height[left]>=height[right]:
#                 right-=1
#             else: 
#                 left+=1
#         return maxArea
                
# if __name__ == '__main__':
#     s = Solution()
#     height = [1,8,6,2,5,4,8,3,7]
#     res = s.maxArea(height)
#     print(res)

### x---------------*****---------------*****--------5.-------*****---------------*****---------------*****---------------x
# # 13. Roman to Integer
# class Solution(object):
#     def romanToInt(self, s):
#         """
#         :type s: str
#         :rtype: int
#         """
#         dict={
#             'I' : 1,
#             'V' : 5,
#             'X' : 10,
#             'L' : 50,
#             'C' : 100,
#             'D' : 500,
#             'M' : 1000
#         }

#         num = 0
#         s = s.replace("IV","IIII")
#         s = s.replace("IX","VIIII")
#         s = s.replace("XL","XXXX")
#         s = s.replace("XC","LXXXX")
#         s = s.replace("CD","CCCC")
#         s = s.replace("CM","DCCCC")
#         for char in s:
#             if char not in dict:
#                 return 'Invalid Input'  
#             num+= dict[char]
#         return num
        
# if __name__ == '__main__':
#     s = Solution()
#     res = s.romanToInt("III")
#     res2 = s.romanToInt('LVIII')
#     res3 = s.romanToInt("MCMXCIV")
#     print(res)
#     print(res2)
#     print(res3)

### x---------------*****---------------*****--------6.-------*****---------------*****---------------*****---------------x
# # 14. Longest Common Prefix
# class Solution(object):
#     def longestCommonPrefix(self, strs):
#         """
#         :type strs: List[str]
#         :rtype: str
#         """
#         # lcp=""
#         # ch = ''
#         # for i in range(len(strs[0])):
#         #     ch += strs[0][i]

#         #     for x in strs:
#         #         if len(x)<len(ch):
#         #             break
#         #         if x[0:i+1] != ch:
#         #             return lcp
#         #     lcp = ch
#         # return lcp            
           
#         # this is first one          
#         strs.sort()
#         i =1
#         while (i<len(strs[0])):
#             if strs[0][:i] == strs[-1][:i]:
#                 i+=1
#             else:
#                 break
#         return strs[0][:i-1]
                
# if __name__ == '__main__':
#     s = Solution()
#     res = s.longestCommonPrefix(['flower', 'flow', 'flight'])
#     print(res)

### x---------------*****---------------*****--------7.-------*****---------------*****---------------*****---------------x
# # 15. 3Sum
# class Solution(object):
#     def threeSum(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: List[List[int]]
#         """
#         nums.sort()
#         res = []
        
#         for i in range(len(nums)):
#             if i>0 and nums[i] == nums[i-1]:
#                 continue
#             left = i+1
#             right = len(nums)-1
#             while(left<right):
#                 sumofTrio = nums[i]+nums[left]+nums[right]
#                 if sumofTrio == 0:
#                     res.append([nums[i],nums[left],nums[right]])
#                     left +=1
#                     right-=1
#                     while left <right and nums[left] == nums[left-1]:
#                         left +=1
#                     while left < right and nums[right] == nums[right + 1]:
#                         right -= 1
#                 elif sumofTrio<0:
#                     left+=1
#                 else:
#                     right -=1
                
#         return res
            
            
   
# if __name__ == '__main__':
#     sol = Solution()
#     nums = [-1,0,1,2,-1,-4]
#     res = sol.threeSum(nums)
#     print(res) 

### x---------------*****---------------*****--------8.-------*****---------------*****---------------*****---------------x
# # 16. 3Sum Closest
# class Solution(object):
#     def threeSumClosest(self, nums, target):
#         """
#         :type nums: List[int]
#         :type target: int
#         :rtype: int
#         """
#         nums.sort()
#         n = len(nums)
#         closeSum = float('inf')

#         for i in range(n):
#             left = i+1
#             right = n-1
#             while(left <right):
#                 currSum = nums[i]+nums[left]+nums[right]
#                 if abs(currSum-target) <abs(closeSum-target):
#                     closeSum = nums[i]+nums[left]+nums[right]
                
#                 if currSum>target:
#                     right-=1
#                 elif currSum<target:
#                     left+=1
#                 else:
#                     return currSum
#         return closeSum

# if __name__ == '__main__':
#     sol = Solution()
#     nums = [-1,2,1,-4]
#     target = 1
#     res = sol.threeSumClosest(nums,target)
#     print(res)

### x---------------*****---------------*****--------9.-------*****---------------*****---------------*****---------------x
# # 18. 4Sum
# class Solution(object):
#     def fourSum(self, nums, target):
#         """
#         :type nums: List[int]
#         :type target: int
#         :rtype: List[List[int]]
#         """
#         nums.sort()
#         n = len(nums)
#         res = []
        
#         for i in range(n):
#             if i > 0 and nums[i] == nums[i - 1]:
#                 continue  
#             for j in range(i + 1, n):
#                 if j > i + 1 and nums[j] == nums[j - 1]:
#                     continue
#                 left = j+1
#                 right = n-1
#                 while(left<right):
#                     currSum = nums[i]+nums[j]+nums[left]+nums[right]
#                     if currSum == target:
#                         res.append([nums[i],nums[j],nums[left],nums[right]])
#                         left+=1
#                         right-=1
#                         while left<right and nums[left] == nums[left-1]:
#                             left+=1
#                         while left<right and nums[right] == nums[right+1]:
#                             right-=1
#                     elif currSum<target:
#                         left+=1
#                     else:
#                         right-=1
#         return res

# if __name__ == '__main__':
#     sol = Solution()
#     nums = [1,0,-1,0,-2,2]
#     target = 0
#     res = sol.fourSum(nums,target)
#     print(res)

### x---------------*****---------------*****--------10.-------*****---------------*****---------------*****---------------x
# # 20. Valid Parentheses
# class Solution(object):
#     def isValid(self, s):
#         """
#         :type s: str
#         :rtype: bool
#         """
#         stack = []
#         dict = {
#             ")": "(",
#             "]": "[",
#             "}": "{"
#         }
#         for ch in s:
#             if ch in dict.values():
#                 stack.append(ch)
#             elif ch in dict.keys():
#                 if ((not stack) or (stack[-1] != dict[ch])):
#                     return False
#                 else:
#                     stack.pop()
#             else:
#                 return False
#         return not stack
        
# if __name__ == '__main__':
#     s = Solution()
#     res = s.isValid("([])")
#     print(res)

### x---------------*****---------------*****--------11.-------*****---------------*****---------------*****---------------x
# # 21. Merge Two Sorted Lists
# # Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution(object):
#     def mergeTwoLists(self, list1, list2):
#         """
#         :type list1: Optional[ListNode]
#         :type list2: Optional[ListNode]
#         :rtype: Optional[ListNode]
#         """
#         dummyList = ListNode()
#         curr = dummyList
        
        
#         while list1 and list2:
#             if list1.val <= list2.val:
#                 curr.next = list1
#                 list1 = list1.next
#             else:
#                 curr.next = list2
#                 list2 = list2.next
#             curr = curr.next
#         if list1:
#             curr.next = list1
#             list1 = list1.next 
#         else:
#             curr.next = list2
#             list2 = list2.next
        
#         return dummyList.next 
            
        
# def to_linked_list(lst):
#     dummy = ListNode()
#     current = dummy
#     for val in lst:
#         current.next = ListNode(val)
#         current = current.next
#     return dummy.next

# def from_linked_list(node):
#     result = []
#     while node:
#         result.append(node.val)
#         node = node.next
#     return result

    
# if __name__ == '__main__':
#     sol = Solution()
#     list1 = to_linked_list([1, 2, 3, 4, 5])
#     list2 = to_linked_list([1, 3, 5, 6, 9])
    
#     mer = sol.mergeTwoLists(list1,list2)
#     print(from_linked_list(mer)) 

### x---------------*****---------------*****--------12.-------*****---------------*****---------------*****---------------x
# # 26. Remove Duplicates from Sorted Array
# class Solution(object):
#     def removeDuplicates(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         if not nums:
#             return 0
        
#         pos = 1
#         for i in range(1,len(nums)):
#             if nums[i] != nums[i-1]:
#                 nums[pos] = nums[i]
#                 pos+=1
#         return pos
                

# if __name__ == '__main__':
#     nums = [1,1,2]
#     s = Solution()
#     k = s.removeDuplicates(nums)
#     print("k =", k)
#     print("Modified nums:", nums[:k])

### x---------------*****---------------*****--------13.-------*****---------------*****---------------*****---------------x
# # 27. Remove Element
# class Solution(object):
#     def removeElement(self, nums, val):
#         """
#         :type nums: List[int]
#         :type val: int
#         :rtype: int
#         """
#         k= 0
#         for i in range(len(nums)):
#             if nums[i] != val:
#                 nums[k] = nums[i]
#                 k += 1
#         #  this is extra no need to do this 
#         # n = len(nums)
#         # m = n-k
#         # l =-1
#         # while m!=0:
#         #     nums[l] = '_'
#         #     m-=1
#         #     l-=1
        

#         return k
# if __name__ == '__main__':
#     sol = Solution()
#     nums = [3,2,2,3]
#     res = sol.removeElement(nums,3)
#     print(res)
#     print(nums)
    
#     nums2 = [0,1,2,2,3,0,4,2]
#     res2 = sol.removeElement(nums2,2)
#     print(res2)
#     print(nums2)

### x---------------*****---------------*****--------14.-------*****---------------*****---------------*****---------------x
# # 28. Find the Index of the First Occurrence in a String 
# class Solution(object):
#     def strStr(self, haystack, needle):
#         """
#         :type haystack: str
#         :type needle: str
#         :rtype: int
#         """
#         return haystack.find(needle)

# if __name__ == '__main__':
#     sol = Solution()
#     result = sol.strStr("sadness","sad")
#     print(result)

### x---------------*****---------------*****--------15.-------*****---------------*****---------------*****---------------x
# # 31. Next Permutation
# class Solution(object):
#     def nextPermutation(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: None Do not return anything, modify nums in-place instead.
#         """
#         i = len(nums) - 2
#         j = len(nums) - 1
#         while i >= 0:
#             if nums[i] < nums[i+1]:
#                 while j >= 0:
#                     if nums[j] >= nums[i]:
#                         nums[i], nums[j] = nums[j], nums[i]
#                         break
#                     j -= 1
#                 break
#             i -= 1

#         i += 1
#         j = len(nums) - 1
#         while j > i:
#             nums[i], nums[j] = nums[j], nums[i]
#             i += 1
#             j -= 1
                      
# import random
# import time
# if __name__ == '__main__':
#     sol = Solution()
#     start = time.time()
#     nums = [1,2,3 ,4,10,9,8,7,6,5]
#     # nums = [3,2,1]
#     # nums = list(range(1000000, 0, -1))
#     sol.nextPermutation(nums)
#     end = time.time()
#     # print(nums)
#     elapsed = end - start
#     print(f"{elapsed:.8f} seconds")

### x---------------*****---------------*****--------15.-------*****---------------*****---------------*****---------------x
# 