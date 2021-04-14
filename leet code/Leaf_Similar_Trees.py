# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        
        l1 = []
        l2 = []
        
        def compare(node, res):
            if node:
                if not node.left and not node.right:
                    res.append(node.val)
                
                compare(node.left, res)
                compare(node.right, res)
                return res
            
        return (compare(root1, l1) == compare(root2, l2))
