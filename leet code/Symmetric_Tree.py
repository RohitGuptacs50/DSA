# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sym(self, p, q):
        if p is None and q or q is None and p:
            return False
        elif p is None and q is None:
            return True
        elif p.val != q.val:
            return False
        return self.sym(p.left, q.right) and self.sym(p.right, q.left)
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.sym(root, root)
        
