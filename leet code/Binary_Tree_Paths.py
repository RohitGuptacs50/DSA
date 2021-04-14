# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if root:
            left = self.binaryTreePaths(root.left)
            right = self.binaryTreePaths(root.right)
            
            if not left + right:
                return [str(root.val)]
            
            res = []
            
            for x in left + right:
                res.append(str(root.val)+ '->' + x)
            return res
        return []
