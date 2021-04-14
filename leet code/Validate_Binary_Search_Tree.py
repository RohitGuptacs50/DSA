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
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        res = []
        if not root:
            return True
        self.inorder(root, res)
        
        for i in range(len(res) - 1):
            if res[i] >= res[i + 1]:
                return False
        return True
