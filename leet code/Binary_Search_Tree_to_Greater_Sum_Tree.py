# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def bstToGst(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        self.sum = 0
        def inorder( root):
            if not root:
                return None
            if root.right:
                inorder(root.right)
            self.sum = self.sum + root.val
            root.val = self.sum
            if root.left:
                inorder(root.left)
            
        inorder(root)
        return root
