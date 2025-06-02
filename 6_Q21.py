#  Problem:- 21. Merge Two Sorted Lists

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummylist = ListNode(-1)
        curr = dummylist

        while list1 and list2:
            if list1.val < list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
            curr = curr.next
        
        if list1:
            curr.next = list1
        else:
            curr.next = list2

        return dummylist.next

def to_linked_list(lst):
    dummy = ListNode()
    current = dummy
    for val in lst:
        current.next = ListNode(val)
        current = current.next
    return dummy.next

def from_linked_list(node):
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result


if __name__ == '__main__':
    sol = Solution()
    list1 = to_linked_list([1, 2, 3, 4, 5])
    list2 = to_linked_list([1, 3, 5, 6, 9])
    
    mer = sol.mergeTwoLists(list1,list2)
    print(from_linked_list(mer)) 
    



