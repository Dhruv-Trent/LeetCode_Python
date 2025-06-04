# Problem:- 101. Symmetric Tree
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        return isMirror(root.left, root.right)
    
def isMirror(p,q):
    if not p and not q:
        return True
    if not p or not q:
        return False
    if p.val!= q.val:
        return False
    return isMirror(p.left,q.right) and isMirror(p.right, q.left)
        

if __name__ == '__main__':
    
    p = TreeNode(1)
    p.left = TreeNode(2)
    p.left.left = TreeNode(3)
    p.left.right = TreeNode(4)
    p.right = TreeNode(2)
    p.right.left = TreeNode(4)
    p.right.right = TreeNode(3)
    
    sol = Solution()
    print(sol.isSymmetric(p))