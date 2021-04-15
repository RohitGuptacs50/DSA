# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    
    def inorder(self, node, res):
        if node:
            self.inorder(node.left, res)
            res.append(node.val)
            self.inorder(node.right, res)
        else:
            return
    
    
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        self.inorder(root, res)
        return res
    
