# Problem:- 100. Same Tree
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: Optional[TreeNode]
        :type q: Optional[TreeNode]
        :rtype: bool
        """
        if not p and not q:
            return True
        if not p or not q:
            return False
        
        if p.val != q.val:
            return False
        
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)


if __name__ == '__main__':

    p = TreeNode(1)
    p.left = TreeNode(2)
    p.right = TreeNode(3)
    
    q = TreeNode(1)
    q.left = TreeNode(2)
    q.right = TreeNode(3)

    sol = Solution()
    print("Trees are the same:", sol.isSameTree(p, q))  