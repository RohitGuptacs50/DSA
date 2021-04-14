# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    
    def check(self, root1, root2):
        if root1 and root2 and root1.val == root2.val:
            return self.check(root1.left, root2.left) and self.check(root1.right, root2.right)
        elif not root1 and not root2:
            return True
        else:
            return False
        
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        return self.check(p, q)
        
