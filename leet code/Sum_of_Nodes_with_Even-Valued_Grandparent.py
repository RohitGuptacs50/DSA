# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumEvenGrandparent(self, root,parent = None,gp = None):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        
        sum = 0
        
        if gp and (gp.val % 2 == 0):
            sum = root.val
            
        return sum + (self.sumEvenGrandparent( root.left,root,parent)) +                               self.sumEvenGrandparent( root.right,root,parent)
