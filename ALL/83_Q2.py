# Problem:-2. Add Two Numbers

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        extra = ListNode(0)
        current  = extra
        carry = 0
        
        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            
            total = val1+val2+carry
            carry = total//10
            
            current.next = ListNode(total%10)
            current = current.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        
        
        return extra.next

        
        
        
        
def build_linked_list(arr):
    dummy = ListNode(0)
    current = dummy
    for num in arr:
        current.next = ListNode(num)
        current = current.next
    return dummy.next


def print_linked_list(node):
    result = []
    while node:
        result.append(str(node.val))
        node = node.next
    print(" -> ".join(result))

    
if __name__ == "__main__":
    sol = Solution()
    l1 = build_linked_list([2, 4, 3])
    l2 = build_linked_list([5, 6, 4])
    res = sol.addTwoNumbers(l1,l2)
    print_linked_list(res)