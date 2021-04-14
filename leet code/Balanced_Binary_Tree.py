# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    
    def Helper(self, node):
        if not node:
            return 0
        left = self.Helper(node.left)
        right = self.Helper(node.right)
        
        if left == -1 or right == -1 or abs(left - right) > 1:
            return -1
        
        return 1 + max(left, right)
        
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.Helper(root) != -1
        
