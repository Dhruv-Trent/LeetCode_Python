# Problem:- 83. Remove Duplicates from Sorted List
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        curr = head
        while curr and curr.next:
            if curr.val == curr.next.val:
                curr.next = curr.next.next
            else:
                curr = curr.next
                
        return head
    
def list_to_linkedlist(lst):
    if not lst:
        return None
    head = ListNode(lst[0])
    curr = head
    for val in lst[1:]:
        curr.next = ListNode(val)
        curr = curr.next
    return head

def linkedlist_to_list(head):
    res = []
    curr = head
    while curr:
        res.append(curr.val)
        curr = curr.next
    return res


if __name__ == '__main__':
    sol = Solution()
    input_list = [1, 1, 2]
    head = list_to_linkedlist(input_list)
    res_head = sol.deleteDuplicates(head)
    res_list = linkedlist_to_list(res_head)
    print(res_list)


