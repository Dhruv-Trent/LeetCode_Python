# Problem:- 110. Balanced Binary Tree
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        return self.checkHeight(root) != -1
    
    def checkHeight(self, node):
        if not node:
            return 0

        left = self.checkHeight(node.left)
        if left == -1:
            return -1

        right = self.checkHeight(node.right)
        if right == -1:
            return -1

        if abs(left - right) > 1:
            return -1

        return max(left, right) + 1
        
# Helper function to create a height-balanced BST from sorted array
def sortedArrayToBST(nums):
    if not nums:
        return None
    mid = len(nums) // 2
    root = TreeNode(nums[mid])
    root.left = sortedArrayToBST(nums[:mid])
    root.right = sortedArrayToBST(nums[mid+1:])
    return root
        
if __name__ == '__main__':
    sol = Solution()
    nums = [-10, -3, 0, 5, 9]  
    tree_root = sortedArrayToBST(nums)  # Convert list to BST
    res = sol.isBalanced(tree_root)     # Check if the BST is balanced
    print(res)   
